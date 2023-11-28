# Class and Object in Pytthon

# Person
# Attribute - name, age, ph no, height, weight, gender, proffession
# Methods/ Functions - Run(), Sleep(), sing(), talk(), eat(), fight(), learn()

# Object
# Amit
# Durga
# Santhosh

class Person:
    # Attribute
    name = None
    Age = None
    Phno = None
    Height = None
    Weight = None
    Gender = None
    Profession = None

    # Methods
    def talk(self):
        print("Talk")

    def sleep(self):
        print("Sleep")

    def walk(self):
        return "I'm walking"



amit_obj = Person()
amit_obj.name = "Amit"
amit_obj.age = 59
amit_obj.Phno = 6726742847
amit_obj.sleep()

print(amit_obj)

durga_obj = Person()
durga_obj.name = "Durga"
print(durga_obj)
durga_obj.sleep()