from abc import ABC, abstractmethod


# Interface for working
class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


# Interface for eating
class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass








class Human(Workable, Eatable):

    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")
    



class Robot(Workable):

    def work(self):
        print("Robot is working")




human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()



# Which Problem Does ISP Solve?
# Fat interfaces

# Unnecessary methods

# Forced implementations

# Difficult maintenance

# ISP ke baad👌👌👌👌:

# Small interfaces

# Clean design

# Easy maintenance

# Better flexibility