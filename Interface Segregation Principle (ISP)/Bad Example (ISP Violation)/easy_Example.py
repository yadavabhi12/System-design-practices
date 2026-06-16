from abc import ABC, abstractmethod


class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):    
        pass





class Robot(Worker):

    def work(self):
        print("Robot is working")

    def eat(self):
        # Problem!
        raise NotImplementedError(
            "Robot does not eat"
        )

r=Robot()
r.work()
r.eat()    # This will raise an error because Robot does not implement the eat method properly, violating the Interface Segregation Principle (ISP).



# Robot can work

# But Robot cannot eat

# Still forced to implement eat()

# This violates ISP