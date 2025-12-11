class love:
    def status(self):
        print("We broken")

class love2:
    def status2(self):
        print("We Patched up")

class Subu(love, love2):
    def India(self):
        print("Subu : I am in India")

class Suba(Subu):
    def UK(self):
        print("Suba: I am in UK")

s=Subu()
s.status()
s.status2()
s.India()

s=Suba()
s.status()
s.status2()
s.UK()
s.India()





