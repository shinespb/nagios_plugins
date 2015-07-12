#!/usr/bin/python3

import argparse
import datetime
import os, sys
from random import randint

path = '/events_storage/phishing_detected'
time = 5 

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str, help="path to directory")
    parser.add_argument("-n", "--num", type=int, default=False, help="Number of files to generate")
    parser.add_argument("-t", "--time", type=int, default=False, help="Generate files for last N minutes")    
    return parser.parse_args()


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)
        print("Creating file in {}".format(path))

def makefiles(path, time, count=0):
    files = []
    dirs = []
    if not int(count):
        count = randint(0,200)

    print("{} files to create".format(count))
    for minutes in range(0, time):
        mov = datetime.timedelta(seconds=(minutes)*60)
        now = datetime.datetime.now() - mov
        # print("moving time: {}".format(now))
        nm = now.strftime('%Y/%m/%d/%H/%M')
        cdir = "{}/{}".format(path, nm)
        print("Creating dir: {}".format(cdir))
        if not os.path.isdir(cdir):
            os.makedirs(cdir)
            dirs.append(cdir)

    if len(dirs) > 0:
        print(dirs)
        for d in dirs:
            count = count - randint(0,count)
            for c in range(0,count):
                p = "{}/{}.test".format(d,c)
                print("create {}".format(p))
                touch(p)
                files.append(p)
    return files


def main(path, time):
    args = args_parse()

    if args.directory:
        path = args.directory
    if args.time:
        time = args.time

    if not os.path.isdir(path):
        print("Directory {} not found".format(path))
        sys.exit()
    tot = makefiles(path, time, args.num)
    print("total files created: {}".format(len(tot)))

if __name__ == "__main__":
    main(path, time)