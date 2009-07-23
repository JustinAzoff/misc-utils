#!/usr/bin/env python
import os, sys

import gzip

URL = "http://popcon.debian.org/by_inst.gz"
FN = os.path.basename(URL)

def header():
    print "#rank name                            inst  vote   old recent no-files (maintainer)"

def fetch():
    if not os.path.exists(FN):
        os.system("wget -c %s" % URL) #be lazy

def get_pop(packages):
    fetch()
    for l in gzip.open(FN):
        if l.startswith("#"): continue
        if l.startswith("-"): return
        package = l.split()[1]
        if package in packages:
            yield package, l.strip()

def get_packages(q):
    cmd = "apt-cache search %s" % q
    for line in os.popen(cmd):
        package = line.split()[0]
        yield package, line.strip()

def main(q):
    packages = {}
    for name, line in get_packages(q):
        packages[name] = line

    header()
    for name, line in get_pop(packages):
        print line, packages[name]

if __name__ == "__main__":
    q = ' '.join(sys.argv[1:])
    main(q)
