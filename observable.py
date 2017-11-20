########################################################################
# @author Mike Ames
# @author Phil Garza
########################################################################
class Observable:

    ####################################################################
    # Constructor. Generates a list to hold observers.
    ####################################################################
    def __init__(self):
        self.observers = []

    #####################################################################
    # Adds observers to the list of observers.
    #####################################################################
    def addObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    #####################################################################
    # Removes observers from the list of observers.
    #####################################################################
    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    #####################################################################
    # Removes all observers from the list of observers.
    #####################################################################
    def removeAllObserver(self, observer):
        self.observers = []

    #####################################################################
    # When the observee's state changes it calls this method to notify
    # the observer by calling the observer's update method.
    #####################################################################
    def update(self, observed):
        for observer in self.observers:
            observer.update(observed)

