import sys, argparse

class MyParser(argparse.ArgumentParser): 

    def error(self, message):
        '''Wraps error and prints in a shorter way'''
        sys.stderr.write('error: %s\n' % message)
        #self.print_help()
        sys.exit(2)
