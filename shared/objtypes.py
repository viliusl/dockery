import os
import subprocess

class AppType:
    HTTP = 1,
    SSH = 2,
    OTHER = 3

class Container(object):
    """ Represents single docker container/machine. """
    def __init__(self, name, basePort, services):
        self.name = name
        self.basePort = basePort
        self.services = services

class Environment(object):
    """ Single multi-container environment. """
    def __init__(self, alias, machines):
        self.alias = alias
        self.machines = machines