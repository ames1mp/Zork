class Observable:

    def __init__(self):
        self.observers = []


    def addObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def removeAllObserver(self, observer):
        self.observers = []

    def update(self, observed):
        for observer in self.observers:
            observer.update(observed)

