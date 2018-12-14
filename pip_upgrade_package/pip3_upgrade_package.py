#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# source: https://stackoverflow.com/a/50207498/4395759

# setting up module being used in the program
import subprocess as sbp
import pip

pkgs = eval(str(sbp.run("pip3 list -o --format=json", shell=True,
                         stdout=sbp.PIPE).stdout, encoding='utf-8'))
for pkg in pkgs:
    sbp.run("pip3 install --upgrade " + pkg['name'], shell=True)