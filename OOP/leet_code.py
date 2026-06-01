from abc import abstractmethod 
class animal:
    # @abstractmethod
    def make_sound(self):
        print("Some generic animal sound")
    def r(self):
        print("Some generic animal sound")

class dog(animal):
    def make_sound(self):
        print("Bark")

class cat(animal):
    def make_sound(self):
        print("Meow")
l:cat=cat()
l.make_sound()
# print(l.make_sound())
# m:dog=dog()
# print(m.make_sound())
# print(animal().make_sound())
t:animal=cat()
# t.make_sound()
# t.r()
m:cat=cat(animal())
m.make_sound()

