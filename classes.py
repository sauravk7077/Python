class LazyPerson():
    def __init__(self,name):
        #Constructor
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        #validation here
        self.__name = value

    def say_name(self):
        print(f'Hello {self.name}')


