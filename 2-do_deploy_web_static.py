#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""

from fabric.api import env, put, run
import os.path

# Define server details
# Replace with your actual web server IPs if different
env.hosts = ['54.162.15.4', '3.87.58.1']
env.user = 'ubuntu'
# To use a specific SSH key, pass it with -i on the command line:
# fab -f <file> do_deploy:archive_path=... -i /path/to/your/key


def do_deploy(archive_path):
    """
    Distributes an archive to web servers

    Args:
        archive_path (str): Path to the archive to deploy

    Returns:
        bool: True if all operations were successful, False otherwise
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Get archive filename and create folder name
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace(".tgz", "")
        remote_tmp_path = "/tmp/{}".format(archive_filename)
        release_path = "/data/web_static/releases/{}/".format(folder_name)

        # Upload the archive to the /tmp/ directory
        if put(archive_path, remote_tmp_path).failed:
            return False

        # Create the release directory
        if run("mkdir -p {}".format(release_path)).failed:
            return False

        # Uncompress the archive
        if run("tar -xzf {} -C {}".format(remote_tmp_path, release_path)).failed:
            return False

        # Delete the archive from the web server
        if run("rm {}".format(remote_tmp_path)).failed:
            return False

        # Move contents from uncompressed web_static folder to release_path
        if run("mv {}web_static/* {}".format(release_path, release_path)).failed:
            return False

        # Remove the now-empty web_static folder
        if run("rm -rf {}web_static".format(release_path)).failed:
            return False

        # Delete the current symbolic link
        if run("rm -rf /data/web_static/current").failed:
            return False

        # Create a new symbolic link
        if run("ln -s {} /data/web_static/current".format(release_path)).failed:
            return False

        return True

    except Exception:
        return False
