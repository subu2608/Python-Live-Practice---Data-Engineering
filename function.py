def cal(*args):
    total=0
    for n in args:
        total += n
    return(total)
print(cal(1,2,3,4,5,6,7,8,9,141))

#KWargs

def create_profile(**kwargs):
    print("User Profile:")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
create_profile(name="", age=30, height=100)
