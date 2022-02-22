#!/usr/bin/env python3

from lilaclib import *


def pre_build():
    update_pkgrel()
    vcs_update()


def post_build():
    git_add_files("PKGBUILD")
    git_commit()
    update_aur_repo()
