#!/usr/bin/env python

import sys

def parse_aliases():
    aliases = {}
    try:
        with open('/etc/aliases', 'r') as f:
            for line in f:
                spltd = line.split(':')
                if len(spltd) < 2:
                    continue
                aliases[spltd[0]] = spltd[1].split()
    except IOError:
        pass
    return aliases

def realnames(aliases, alias):
    names = []
    if not alias in aliases.keys():
        return [alias]
    for a in aliases[alias]:
        names += realnames(aliases, a)
    return names

def forwardof(name):
    try:
        with open('/home/%s/.forward' % name, 'r') as f:
            return f.read().strip()
    except IOError:
        return ""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "USAGE: %s <username or mailing list name>" % sys.argv[0]
        exit(1)

    mailid = sys.argv[1]
    aliases = parse_aliases()
    reals = realnames(aliases, mailid)
    for r in reals:
        print forwardof(r)
