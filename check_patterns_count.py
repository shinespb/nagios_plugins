#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
import argparse
import sys, os
import datetime, time

# set default values
warning = 100
critical = 50
time = 5

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="path to directory")
    parser.add_argument("-w", "--warning", type=int, default=False, help="warning files count")
    parser.add_argument("-c", "--critical", type=int, default=False, help="critical files count")
    parser.add_argument("-t", "--time", type=int, default=False, help="Time count")
    return parser.parse_args()


def getdirlist(path, time):
    files = []

    for minutes in range(0, time):
        #print("min: {}".format(minutes))
        mov = datetime.timedelta(seconds=(minutes)*60)
        now = datetime.datetime.now() - mov
        # print("moving time: {}".format(now))
        nm = now.strftime('%Y/%m/%d/%H/%M')
        cdir = "{}/{}".format(path, nm)
        # print("Path: {}".format(cdir))
        if os.path.isdir(cdir):
            [files.append(cdir+name) for name in os.listdir(cdir) if os.path.isfile(os.path.join(cdir, name))]
    return files

def main(warning, critical, time):
    args = args_parse()

    if args.warning:
        warning = args.warning
    if args.critical:
        critical = args.critical
    if args.time:
        time = args.time
    if args.path:
        path = args.path

    """ check base path """
    if not os.path.isdir(path):
        print("PATTERNS CRITICAL: Directory {} does not found".format(path))
        sys.exit(2)

    totalfiles = getdirlist(args.path, time)
    if len(totalfiles) < critical:
        print("PATTERNS CRITICAL: Total patterns {} for last {} minutes".format(len(totalfiles), time))
        sys.exit(2)
    elif len(totalfiles) < warning:
        print("PATTERNS WARNING: Total patterns {} for last {} minutes".format(len(totalfiles), time))
        sys.exit(2)
    else:
        print("PATTERNS OK: Total patterns {} for last {} minutes".format(len(totalfiles), time))

 
    # print("Totalfiles: {}".format(len(totalfiles)))
   

    # print("Current date and time: {}".format(datetime.datetime.now()))

    # print("W: {}; C: {}; T: {}; P: {}".format(warning, critical, time, path))
    # print("args: {}".format(args))




if __name__ == "__main__":
    main(warning, critical, time)