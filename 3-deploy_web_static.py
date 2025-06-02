#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers.
Combines functionality of 1-pack_web_static.py and 2-do_deploy_web_static.py
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os.path

# Define server details
env.hosts = ['54.162.15.4', '3.87.58.1'] # web-01 and web-02 IPs
env.user = 'ubuntu'
# For SSH key, use -i /path/to/your/key with fab command


def do_pack():
    """Generates a .tgz archive from the web_static folder.
    Identical to do_pack in 1-pack_web_static.py
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)

        print("Packing web_static to {}".format(archive_path))
        result = local("tar -cvzf {} web_static".format(archive_path))

        if result.succeeded:
            file_size = os.path.getsize(archive_path)
            print("web_static packed: {} -> {}Bytes".format(
                archive_path, file_size))
            return archive_path
        else:
            return None
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to web servers.
    Identical to do_deploy in 2-do_deploy_web_static.py
    """
    if not os.path.exists(archive_path):
        print(f"Archive path {archive_path} does not exist locally.")
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace(".tgz", "")
        remote_tmp_path = f"/tmp/{archive_filename}"
        release_path = f"/data/web_static/releases/{folder_name}/"

        if put(archive_path, remote_tmp_path).failed:
            print(f"Failed to upload {archive_path} to {remote_tmp_path}")
            return False
        if run(f"mkdir -p {release_path}").failed:
            print(f"Failed to create release directory {release_path}")
            return False
        if run(f"tar -xzf {remote_tmp_path} -C {release_path}").failed:
            print(f"Failed to uncompress archive to {release_path}")
            return False
        if run(f"rm {remote_tmp_path}").failed:
            print(f"Failed to delete archive {remote_tmp_path} from server.")
            return False
        if run(f"mv {release_path}web_static/* {release_path}").failed:
            print(f"Failed to move content from {release_path}web_static/*")
            return False
        if run(f"rm -rf {release_path}web_static").failed:
            print(f"Failed to remove directory {release_path}web_static")
            return False
        if run("rm -rf /data/web_static/current").failed:
            print("Failed to delete current symbolic link.")
            return False
        if run(f"ln -s {release_path} /data/web_static/current").failed:
            print(f"Failed to create new symbolic link to {release_path}")
            return False

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"An deployment exception occurred: {e}")
        return False


def deploy():
    """Creates an archive and deploys it to web servers.

    Calls do_pack() to create an archive, then calls do_deploy()
    to distribute this archive to the servers.

    Returns:
        bool: True if packing and deployment succeed, False otherwise.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

# If you want to be able to run this directly for some reason (though Fabric is the typical way)
# if __name__ == "__main__":
# print("Running deploy function via direct script execution (not typical for Fabric)")
# success = deploy()
# if success:
# print("Deployment finished successfully.")
# else:
# print("Deployment failed.") 