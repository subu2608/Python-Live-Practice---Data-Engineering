class broken:
    def status(self):
        print("We broke up")

class Subu(broken):
    def status(self):
        print("I Still believe Universe Holds Something for us")

class Suba(broken):
    def status(self):
        print("I can't get my love back")

# Polymorphic behavior
for s in [Suba(), Subu()]:
    s.status()
