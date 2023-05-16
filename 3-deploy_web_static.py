#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers.

This Fabric script provides functionality to create an archive of the web_static
folder and distribute it to the specified web servers for deployment.
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["54.209.198.21", "52.91.125.243"]
env.user = "ubuntu"


def do_pack():
    """
    Create a compressed archive of the web_static folder.

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


def deploy():
    """
    Create and distribute an archive to the web servers.

    Returns:
        bool: True if the deployment is successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
