#!/usr/bin/env python

import sys, os, os.path, argparse

from shared.config import *
from objects.myparser import MyParser

GIT_REPO="https://github.com/viliusl/dockery"

class Dockery(object):

    def handle_init(self, *args):
        """ Initialize configured docker images - just pull them.
        """

    def handle_selfupdate(self, *args):
        """ Update myself from git repo + update configured docker images - latest and greatest:)
        """

    def handle_start(self, *args):
        """ [alias] Start provided environment.
        """

    def handle_stop(self, *args):
        """ [alias] Stop provided environment.
        """

    def handle_restart(self, *args):
        """ [alias] Stop/Start provided environment.
        """

    def handle_status(self, *args):
        """ Get status on configured environments.
        """

    def handle_ssh(self, *args):
        """ [alias] connect to one of the machines from provided environments.
        """

    def handle_http(self, *args):
        """ [alias] Open endpoint from provided machines via browser.
        """

    def __init_parser(self, arg_count=3):
        """ Initialize parser for single -i argument and n positional arguments."""
        parser = MyParser()
        parser.add_argument("-i", dest="keep", action='store_true')
        parser.add_argument("keys", nargs=arg_count)
        return parser

def main():
    program_name, args = sys.argv[0], sys.argv[1:]
    if not args or 'help' in args:
        print 'Usage: %s command' % program_name
        print_usage()
        sys.exit(1)

    app = Dockery()
    command = args[0]
    method = 'handle_%s' % command.replace(':', '_')
    if hasattr(app, method):
        getattr(app, method)(*args[1:])
    else:
        print 'No such command: %s' % command
        print_usage()


def print_usage():
    app = Dockery()
    methods = [name for name in dir(app) if name.startswith('handle_')]
    print 'Known commands:'
    for method in methods:
        command = method[7:].replace('_', ':')
        print '%10s\t%s' % (command, getattr(app, method).__doc__)

if __name__ == '__main__':
    main()
