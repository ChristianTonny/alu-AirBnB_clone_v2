#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the web_static folder.

    All files in the folder web_static must be added to the final archive.
    All archives must be stored in the folder versions (your function
    should create this folder if it doesn't exist).
    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive
    has been correctly generated. Otherwise, it should return None.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive name with timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)

        print("Packing web_static to {}".format(archive_path))

        # Create the .tgz archive from the web_static directory
        # The command assumes 'web_static' is a directory in the current path.
        result = local("tar -cvzf {} web_static".format(archive_path))

        if result.succeeded:
            file_size = os.path.getsize(archive_path)
            print("web_static packed: {} -> {}Bytes".format(
                archive_path, file_size))
            return archive_path
        else:
            return None
    except Exception:
        # Catch exceptions (e.g., tar issues, folder not found)
        # and return None as per requirements.
        return None


if __name__ == "__main__":
    # This part is for local testing.
    # Fabric normally calls functions like do_pack() directly.
    # Example for local test: python3 1-pack_web_static.py
    # Fabric's way to run: fab -f 1-pack_web_static.py do_pack
    path = do_pack()
    if path:
        print("Archive created successfully: {}".format(path))
    else:
        print("Failed to create archive.") 