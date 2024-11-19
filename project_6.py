#函数
animals={}
def ani(brand,owners,age):
    animals[brand]=[owners,age]
for number in range(1,5):
    brand=input("what is the animal?")
    owners=input("who is the owner?")
    age=input("what is the age?")
    ani(brand,owners,age)
for key,values in animals.items():
    print(key)
    for value in values:
        print(value)
print("\n")


def name(first_name,middle_name="",last_name=""):
    if middle_name:
        user_name=f"{first_name} {middle_name} {last_name}"
    else:
        user_name=f"{first_name} {last_name}"
    print(user_name)
name("wang",middle_name="zi",last_name="wen")
name("wang",last_name="wen")
print("\n")


albums=[]
def make_album(singer_name,song_name,extra=None):
    album={}
    if extra:
        album[singer_name]=f"{song_name} {extra}"
    else:
        album[singer_name]=f"{song_name}"
    return album
while True:
    singer_name=input("What is your singer_name?")
    song_name=input("What is your song_name?")
    result=input("Do you want to add more? Yse or No?")
    if singer_name.lower()!="quit" and song_name.lower()!="quit" and result.lower()!="quit":
        if result.title()=="Yes":
            number=input("number")
            album_1=make_album(singer_name,song_name,number)
        elif result.title()=="No":
            album_1=make_album(singer_name,song_name)
        albums.append(album_1)
    else:
        break
print(albums)
print("\n")


completed_users=["lin","yang"]
new_users=["wang","liu","zhang","zhao"]
def show_users(new):
    while len(new):
        current_user=new.pop()
        print(current_user)
        completed_users.append(current_user)
show_users(new_users)
print(completed_users)#传递原列表，使列表在函数中改变
print(new_users)
completed_users=["lin","yang"]
new_users=["wang","liu","zhang","zhao"]
show_users(new_users[:])#传递列表副本，禁止原列表在函数中改变
print(completed_users)
print(new_users)
print("\n")


def pizzas(*ingredients):
    for ingredient in ingredients:
        print(f"pizza has {ingredient}")
pizzas("pepper","pork","cheese","salt")
print("\n")


def user(first_name,last_name,**information):
    information["first_name"]=first_name
    information["last_name"]=last_name
    return information
user_profile=user("Wang","zi wen",wage="100million",carrer="computer engineer",age=38)
print(user_profile)
print("\n")