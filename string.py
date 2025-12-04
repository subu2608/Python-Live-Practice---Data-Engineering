name='subRamanian @ vicky vignesh'
mbl='9442400341'
print(name.lower())
print(name.upper())
print(name.title() + ' - ' + mbl)
print(name.capitalize())
print("*******"+mbl[-3])
print(name.split("vicky")[1].strip())

promomsg='Hello, You got your offer, Enjoy your ride'
if "got your offer" in promomsg:
    print(promomsg+"\n\n")
else:
    print("You dont have offer")
print("Offer Position is:", promomsg.find("offer"))
print([word[0].upper() for word in name.split()])
print(len(promomsg.split('your')))
