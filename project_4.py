#基础知识：添加键值对    删除键值对    .get()     .items()    .values()   .keys()     列表与字典的嵌套


people={"lucy":"2billion","mack":"9million","jack":"1trillion"}
print(f"mack has earned {people["mack"].upper()} dollors")
print("\n")


cars={"audi":30,"tesla":20,"bmw":33,"benz":40}
for key,value in cars.items():
    print(key)
    print(value)
cars["audi"]=25
for name,price in cars.items():
    print(name)
    print(price)
del cars["tesla"]
for name,price in cars.items():
    print(name,price)
print("\n\n")


lakes={"nile":"egypt","yangzi":"china","henghe":"india"}
for lake in lakes.keys():
    print(lake)
for lake in lakes.values():
    print(lake)
print("\n\n")


cars=[]
car1={"color":"red","price":5,"speed":200}
car2={"color":"white","price":6,"speed":220}
car3={"color":"black","price":4,"speed":180}
cars.append(car1)
cars.append(car2)
cars.append(car3)
for car in cars:
    for key,value in car.items():
        print(key,value)
print("\n\n")


countries={}
countries["china"]=["beijing",14,"east"]
countries["america"]=["newyork",3,"west"]
countries["france"]=["paris",0.8,"west"]
for country,information in countries.items():
    print(country)
    for inform in information[:]:
        print(inform)
print("\n\n")


Con=countries.get("india","i can't find this country")
print(Con)
print("\n\n")


people={"lucy":["C","Python"],"jack":["Java","C++","Python"],"mack":["C++"]}
for person,language in people.items():
    if len(language)==1:
        print(f"{person.title()}'s favourite language is")
        for lan1 in language:
            print(lan1)
    if len(language)>1:
        print(f"{person.title()}'s favourite language are")
        for lan2 in language:
            print(lan2)