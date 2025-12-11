class access:
    def __init__(self):
        self.public=("This is Public")
        self.__private=("This is Private")
        self._protected=("This is Protected")

    def access_specifier2(self):
        print("Access from Parent or Main Class")
        print("---------------------------")
        print(self.public)
        print(self.__private)
        print(self._protected)
        print("---------------------------")



class access2(access):
    def access_specifier3(self):
        print("Access from Child or Sub Class:")
        print("---------------------------")
        print(self.public)
        print(self._protected)
        try:
            print(self._access__private)
            print("---------------------------")
        except AttributeError:
            print("Cannot Access")
            print("---------------------------")


class access3():
    def access_specifier4(self,obj):
        print("Access from Outside Class:")
        print("---------------------------")
        print(obj.public)
        print(obj._protected)
        try:
            print(obj._access__private)
            print("---------------------------")
        except AttributeError:
            print("Cannot Access")

a=access()
a.access_specifier2()

b=access2()
b.access_specifier3()

c=access3()
c.access_specifier4(a)