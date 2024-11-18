#基础知识：input()   int()   while   break   continue    列表间移动元素    删除列表中特定元素    使用用户输入填充字典


number=input("tell me the number\n")
print(number,"\n")

name=input("What is your name?")
print(f"hello {name.title()},welcome to our class\n")

word="do you know it?"+"yes or no?"
judge=input(word)
print(judge,"\n")

num=input("please input number")
num=int(num)
if num>100:
    print("so big\n")
else:
    print("so small\n")

pizzas=[]
add=""
while add!="quit":
    add=input("what do you want?")
    pizzas.append(add)
pizzas.remove("quit")
for pizza in pizzas:
    print(f"your pizza have {pizza}")
print("\n")

unconfirmed=["jack","mack","lucy","jerry"]
confirmed=["Mike","Leo"]
while len(unconfirmed)>0:
    name=unconfirmed.pop()
    confirmed.append(name)
print("all users:")
for all in confirmed:
    print(all)
print("\n")

animals=["cat","fish","dog","elephant","dog","rabbit","cat","cat"]
while "cat" in animals:
    animals.remove("cat")
print("剩余的动物")
for animal in animals:
    print(animal)
print("\n")

responses={}
flag=True
while flag:
    name=input("what is your name?")
    response=input("where do you want to go?")
    responses[name]=response
    repeat=input("someone else? yes or no?")
    if repeat !="yes":
        flag=False
for name,place in responses.items():
    print(f"{name} wants to visit {place}")