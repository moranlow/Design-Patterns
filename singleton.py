#Singleton
#Singleton is a generative design pattern that ensures that a class has only one instance, and provides a global access point to it.
#Singleton allows you to access a single instance of it from any point in the client code 
#Instance creation is done by the principle of delayed initialization

# creating main class with a dictionary which checks for the presence of a singleton and, if it is not present, adds it
class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]


#This is our singleton which is inherited through the metaclass and some variables
class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self):
        self.name = "Singleton"
        self.value_a = 3
        self.value_b = 5

    def add_a_b(self) -> int:
        return self.value_a+self.value_b

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


if __name__ == "__main__":
    my_singleton1 = MySingleton()
    my_singleton2 = MySingleton()
    print("Singleton1 name: " + my_singleton1.get_name())
    my_singleton1.set_name("New Singleton")
    print("Singleton2 name: " + my_singleton2.get_name())
    print(my_singleton1)
    print(my_singleton2)
    print(id(my_singleton1) == id(my_singleton2))