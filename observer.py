########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
from abc import ABCMeta, abstractmethod

########################################################################
# Abstract base class. Requires the implementing class to implement the
# update method, which is called by the observee.
########################################################################
class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass



