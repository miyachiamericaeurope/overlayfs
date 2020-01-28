#!/usr/bin/env python3
import subprocess
import time
import sys
import os
import  shutil
import datetime

PATH = '/media/ramdisk'
USAGE_LIMIT = 90 #%
POLL_FREQ = 1 #s
BACKUP_PATH = '/home/tyson/ramdiskBAK'

def run_cmd(cmdlist):
    # function for running shell commands
    try:
        stdout = subprocess.check_output(cmdlist)
    except subprocess.CalledProcessError:
           pass
    else:
        if stdout:
            return  stdout.decode('utf-8')

def backup_ramdisk():
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)
    files = os.listdir(PATH)
    print('backup_ramdisk() called. moving {} files.'.format(len(files)))
    print(datetime.datetime.now(), '\n\n')
    for file in files:
        filePathSrc = os.path.join(PATH, file)
        filePathDst = os.path.join(BACKUP_PATH, file)
        shutil.move(filePathSrc, filePathDst)

while True:
    fsUsage = run_cmd( 'df {} --output=pcent'.format(PATH).split() )
    print(fsUsage)
    if int(fsUsage.split('\n')[1].strip().split('%')[0]) >= USAGE_LIMIT:
        backup_ramdisk()
    time.sleep(POLL_FREQ)
