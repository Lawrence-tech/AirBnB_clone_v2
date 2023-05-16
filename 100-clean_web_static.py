#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.

This Fabric script provides functionality to delete unnecessary archives
based on the specified number of archives to keep.
"""

from fabric.api import *
import os

env.hosts = ["54.209.198.21", "52.91.125.243"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): Number of archives to keep (including the most recent).

    """
    number = int(number)

    if number < 1:
        number = 1

    archives_dir = "versions"
    releases_dir = "/data/web_static/releases"

    with lcd(archives_dir):
        local("ls -1t | tail -n +{} | xargs -I {{}} rm -- {}".format
              (number + 1, "{}"))

    with cd(releases_dir):
        run("ls -1t | tail -n +{} | xargs -I {{}} rm -rf -- {}".format
            (number + 1, "{}/{}"))
