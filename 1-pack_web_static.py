#!/usr/bin/python3
"""
A module for Fabric script that generates a .tgz archive.

This module provides functionality to create a compressed .tgz archive
of the static files using Fabric.
"""

import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """
    Archives the static files.

    This function creates a compressed .tgz archive of the static files
    in the "versions" directory. The archive name includes the current
    date and time.

    Returns:
        str: The path of the created archive file or None if archiving fails.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )

    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None

    return output
