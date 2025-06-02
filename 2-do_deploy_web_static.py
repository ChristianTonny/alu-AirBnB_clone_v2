#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers.
Based on 1-pack_web_static.py
"""

from fabric.api import env, put, run, local
import os.path

# Define server details
# Replace with your actual web server IPs if different
env.hosts = ['54.162.15.4', '3.87.58.1']
env.user = 'ubuntu'
# To use a specific SSH key, pass it with -i on the command line:
# fab -f <file> do_deploy:archive_path=... -i /path/to/your/key


def do_deploy(archive_path):
    """Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        print(f"Archive path {archive_path} does not exist locally.")
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        # folder_name is archive_filename without .tgz extension
        folder_name = archive_filename.replace(".tgz", "")
        remote_tmp_path = f"/tmp/{archive_filename}"
        release_path = f"/data/web_static/releases/{folder_name}/"

        # Upload the archive to the /tmp/ directory
        if put(archive_path, remote_tmp_path).failed:
            print(f"Failed to upload {archive_path} to {remote_tmp_path}")
            return False

        # Create the release directory
        if run(f"mkdir -p {release_path}").failed:
            print(f"Failed to create release directory {release_path}")
            return False

        # Uncompress the archive
        if run(f"tar -xzf {remote_tmp_path} -C {release_path}").failed:
            print(f"Failed to uncompress archive to {release_path}")
            return False

        # Delete the archive from the web server
        if run(f"rm {remote_tmp_path}").failed:
            print(f"Failed to delete archive {remote_tmp_path} from server.")
            return False

        # Move contents from the uncompressed web_static folder to release_path
        # Assumes do_pack creates an archive with a 'web_static' root folder
        if run(f"mv {release_path}web_static/* {release_path}").failed:
            print(f"Failed to move content from {release_path}web_static/*")
            # This might also mean web_static was empty or not found.
            # For robustness, one might add a check, but following example structure.
            return False

        # Remove the now-empty web_static folder inside the release directory
        if run(f"rm -rf {release_path}web_static").failed:
            print(f"Failed to remove directory {release_path}web_static")
            return False

        # Delete the current symbolic link
        if run("rm -rf /data/web_static/current").failed:
            print("Failed to delete current symbolic link.")
            return False

        # Create a new symbolic link
        if run(f"ln -s {release_path} /data/web_static/current").failed:
            print(f"Failed to create new symbolic link to {release_path}")
            return False

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"An deployment exception occurred: {e}")
        return False 