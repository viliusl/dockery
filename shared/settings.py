import os, sys
from ConfigParser import SafeConfigParser

CONFIG_DIR = os.getenv("HOME") + "/.dockery"
CONFIG_FILE = "default.config"

CREDENTIALS_FILE_CONTENT = """\

[xap.default]
username=gigaspace

[xap.prod]
username=vilu02
"""

class Settings(object):

    def __init__(self, environment):
        self.environment = environment
        self.credentials_file = os.path.join(CONFIG_DIR, CONFIG_FILE)
        self.username = None

    def load(self):
        """ Loads data from credentials file
        """
        if not os.path.exists(self.credentials_file):
            self.__create_creadentials_file()

        try:
            config = SafeConfigParser()
            config.readfp(open(self.credentials_file))
            self.username = config.get(self.environment, "username")

        except Exception as e:
            print "Error occured when parsing credentials file %s:\n%s" % (self.credentials_file, e)
            sys.exit(1)

        return self

    def __create_creadentials_file(self):
        """ Creates credentials file in ~/.devops directory
        """
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)

        print "Creating %s file" % self.credentials_file

        file = open(self.credentials_file, 'w')
        file.write(CREDENTIALS_FILE_CONTENT)
        file.close()

        print "Fill your credentials in %s file and run command again" % self.credentials_file
        sys.exit(1)