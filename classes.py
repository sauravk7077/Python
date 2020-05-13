class LazyPerson():
    def __init__(self,name):
        #Constructor
        self.name = name

    @property
    def name(self):
        print("In the getter")
        return self.__name
    
    @name.setter
    def name(self, value):
        print("In setter")
        #validation here
        self.__name = value

    def say_name(self):
        print(f'Hello {self.name}')


