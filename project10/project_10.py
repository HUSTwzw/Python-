
from pathlib import Path
import json
numbers=[1,2,3,4,5,6,7,8]
path1 =Path("number1.json")
contents=json.dumps(numbers)        #将数据转化为json格式，以便写入json文件
path1.write_text(contents)
content=path1.read_text()
number=json.loads(content)          #将数据转化为python常规格式，以便在终端输出
print(number)
print("\n")


from pathlib import Path
import json
path2=Path("username1.json")
try:
    content_json=path2.read_text()          #若没有创建用户名相关信息，就报错并进行创建
    username1=json.loads(content_json)
except FileNotFoundError:
    content_py=input("we failed to find your username,please write it again!")
    content_js=json.dumps(content_py)
    path2.write_text(content_js)
else:
    print(f"hello {username1},we will remember you!")
print("\n")


from pathlib import Path
import json
path2=Path("username1.json")
if path2.exists():          #等效于上一个程序的try-except
    name=path2.read_text()
    username=json.loads(name)
    print(f"hello {username},i am glad to meet you!")
    print("I will always remember you")
else:
    username=input("we failed to find you,please tell me your name!")
    username=json.dumps(username)
    path2.write_text(username)
print("\n")


from pathlib import Path
import json
def get_path():
    path_name=input("tell me the path.")
    path=Path(path_name)
    return path

def write_name(path):
    username=input("tell me your name.")
    username=json.dumps(username)
    path.write_text(username)
    return username

def read_name(path):
    username=path.read_text()
    username=json.loads(username)
    username=username["username"]
    print(f"welcome {username}")
    return username

def add_information(path,username):
    birthday=input("tell me your birthday")
    address=input("tell me your address")
    dict={"username":username}
    dict["birthday"]=birthday
    dict["address"]=address
    content=json.dumps(dict)
    path.write_text(content)

def say_hello():
    path=get_path()
    if path.exists():
        username=read_name(path)
    else:
        username=write_name(path)
    add_information(path,username)

say_hello()
print("\n")