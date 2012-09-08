#!/usr/bin/env python
import os
import sys
import json
import urllib2

def fetch_all(username, path=None):
    if not path:
        path = os.path.expanduser("~/projects/")

    os.chdir(path)

    url = "https://api.github.com/users/%s/repos" % username
    data = json.load(urllib2.urlopen(url))
    for repo in  data:
        clone_repo(repo)

def clone_repo(repo):
    if os.path.exists(repo['name']):
        print 'already cloned %(name)s' % repo
        return
    print 'cloning %(name)s' % repo
    uri = "git@github.com:%(full_name)s.git" % repo
    os.system('git clone %s' % uri)

if __name__ == "__main__":
    path = None
    username = sys.argv[1]
    if len(sys.argv) == 3:
        path = sys.argv[2]
    fetch_all(username, path)
