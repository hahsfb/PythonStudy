class OnlyOne:
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(OnlyOne)
        return cls.singleton

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


if __name__ == "__main__":
    test1 = OnlyOne("Willock")

    if OnlyOne.singleton:
        test2 = OnlyOne.singleton
    else:
        test2 = OnlyOne("NONONONO")
    print(id(test1))
    print(id(test2))
    test1.print_name()
    test2.print_name()
    assert test1 == test2
