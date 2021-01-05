
class Person:

    def __init__(self, name):
        self.name = name


    def __eq__(self, other):

        if isinstance(other, Person):
            return self.name == other.name

        else:
            return False

    
    def __hash__(self):
        return hash(self.name)
        


if __name__ == "__main__":

    p1 = Person("John")
    p2 = Person("Alex")
    p3 = Person("John")

    print(f"p1 == p2 : {p1 == p2}")
    print(f"p1 is p2 : {p1 is p2}")

    print(f"p1 == p3 : {p1 == p3}")
    print(f"p1 is p3 : {p1 is p3}")

    print(f"hash(p1) == hash(p2) : {p1 == p2}")
    print(f"hash(p1) == hash(p3) : {hash(p1) == hash(p3)}")




