from inheritance import love, Subu, Suba

class Kauvya(love, Suba):
    def KMU(self):
        print("Kauvya Supporting Suba")

class Aaru(love, Subu):
    def TVL(self):
        print("Aaru Supporting Subu")
check=Kauvya()
check.status()
check.KMU()
check.Suba()

check2=Aaru()
check2.status()
check2.TVL()

