#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
import os.path

env.hosts = ['54.162.15.4', '3.87.58.1']
env.user = 'ubuntu'


def do_pack():
    """
    Generates a .tgz archive from the web_static folder

    Returns:
        str: Archive path if generated correctly, otherwise None
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)

        result = local("tar -cvzf {} web_static".format(archive_path))

        if result.succeeded:
            return archive_path
        else:
            return None
    except Exception:
        return None


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
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.replace(".tgz", "")
        remote_tmp_path = "/tmp/{}".format(archive_filename)
        release_path = "/data/web_static/releases/{}/".format(folder_name)

        if put(archive_path, remote_tmp_path).failed:
            return False
        if run("mkdir -p {}".format(release_path)).failed:
            return False
        if run("tar -xzf {} -C {}".format(remote_tmp_path, release_path)).failed:
            return False
        if run("rm {}".format(remote_tmp_path)).failed:
            return False
        if run("mv {}web_static/* {}".format(release_path, release_path)).failed:
            return False
        if run("rm -rf {}web_static".format(release_path)).failed:
            return False
        if run("rm -rf /data/web_static/current").failed:
            return False
        if run("ln -s {} /data/web_static/current".format(release_path)).failed:
            return False

        return True

    except Exception:
        return False


def deploy():
    """
    Creates an archive and deploys it to web servers

    Returns:
        bool: True if packing and deployment succeed, False otherwise
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
