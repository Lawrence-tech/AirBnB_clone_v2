#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers.

This Fabric script provides functionality to distribute an archive
to the specified web servers for deployment.
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["54.209.198.21", "52.91.125.243"]
env.user = "ubuntu"


def do_pack():
    """
    Return the archive path if the archive has been generated correctly.

    This function creates a compressed .tgz archive of the web_static
    folder and stores it in the "versions" directory. The archive name
    includes the current date and time.

    Returns:
        str: The path of the created archive file or None if archiving fails.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distribute the archive to the web servers for deployment.

    This function distributes the specified archive to the web servers
    and performs the necessary steps to deploy the new version of the
    web_static folder.

    Args:
        archive_path (str): The path of the archive file to be deployed.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    archived_file = archive_path.split("/")[-1]
    no_ext_filename = archived_file.split(".")[0]
    release_path = "/data/web_static/releases/{}/".format(no_ext_filename)
    tmp_path = "/tmp/{}".format(archived_file)

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(release_path))
        run("sudo tar -xzf {} -C {}".format(tmp_path, release_path))
        run("sudo rm {}".format(tmp_path))
        run("sudo mv {}web_static/* {}".format(release_path, release_path))
        run("sudo rm -rf {}web_static".format(release_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except Exception:
        return False
