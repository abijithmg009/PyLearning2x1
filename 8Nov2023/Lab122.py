# Multiple level inheritence

#Level = GF -> F -> S
# reverse method is not possible it's only one direction

class GrandParent:
    def Grandparent_method(self):
        return "Grand parent Method"

class Parent(GrandParent):
    def Parent_method(self):
        return "Parent Method"

class Child(Parent):
    def child_method(self):
        return "Child Method"
child = Child()
print(child.Grandparent_method())
print(child.Parent_method())
print(child.child_method())