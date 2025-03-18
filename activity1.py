# Import necessary Modules
from abc import ABC, abstractmethod

# creat base class
class Absclass(ABC):

    # Function to print a value
    def print(self,x):
        print("passed value: ", x)

    # Abstract method
    @abstractmethod
    def task(self):
        print("we are inside Absclass task")

# creat sub class
class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")

# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)