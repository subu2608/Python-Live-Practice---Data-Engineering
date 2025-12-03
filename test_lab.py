#L > E > G > B

#Local

def job():
    job="Abroad Job"
    print(job)
job()

#Enclosed

def job2():
    job="Abroad Job"

    def checkout():
        print("No alternatives:", job)
    checkout()
job2()

#Global

target=('UK or Germany')
def job3():
    print(target)
def job4():
    print(target)
job3()
job4()

#build in variable
print(__file__)

#Final version
dream='Secure job in 90 days from now'
def drea():
    skill='improve skill'
    def target():
        print('My intention is',skill, 'and', dream)
    target()
drea()
print(dream)

