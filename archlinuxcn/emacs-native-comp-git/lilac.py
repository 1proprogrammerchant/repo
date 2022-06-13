#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build('emacs-git', maintainers=['toropisco'])
    checks = ''
    for line in edit_file('PKGBUILD'):
        if line.startswith('  pkgname="emacs-git"'):
            line = '  pkgname="emacs-native-comp-git"'
            checks = checks + '1'

        if line.startswith('replaces='):
            checks = checks + '2'
            continue

        if line.startswith('JIT='):
            line = 'JIT="YES"'
            checks = checks + '3'
        if line.startswith('AOT='):
            line = 'AOT="YES"'
            checks = checks + '4'

        if line.startswith('XWIDGETS='):
            line = 'XWIDGETS="YES"'
            checks = checks + '5'

        if line.startswith('PGTK='):
            line = 'PGTK="YES"'
            checks = checks + '6'

        if line.startswith('install='):
            line = 'install=emacs-git.install'
            checks = checks + '7'

        #if line.startswith('source='):
        #    line = 'source=("emacs-git::git+https://github.com/emacs-mirror/emacs.git")'
        #    checks = checks + '3'

        print(line)

    # make sure PKGBUILD is modified
    if len(checks) != 7:
        raise ValueError('PKGBUILD editing not completed. checks=' + checks)
