#Car
#Object - Tesla, Lambo

class Car:
    name = None
    color = None
    model = None
    speed = None
    engine_type = None

    # self is a special variable that is used within the context of
    # object-oriented programming (OOP).
    # It is a reference to the instance of a class
    # access and manipulate the attributes and methods of that instance / Object

    def Start(self):
        print("Starting Engine")

    def Drive(self):
        print("Drive")

    def Stop(self):
        print("Break")

    def who_is_driving(self):
        print("I'm driving ->" + self.name)

tesla = Car()
lambo = Car()
tesla.name = "Tesla"
lambo.name = "Lambo"
tesla.Start()
tesla.Drive()
tesla.Stop()
tesla.who_is_driving()
lambo.who_is_driving()