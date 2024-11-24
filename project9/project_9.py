while True:
    first=input("please input the first number")
    second=input("please input the second number")
    try:
        num1=int(first)
        num2=int(second)
    except ValueError:
        print("error")
    else:
        print(num1+num2)
        break


from pathlib import Path
flag=True
while flag:
    print("Please give me two numbers and I will divide them!")
    print("you can press 'q' to quit the program")
    first_number=input("give me the first number")
    second_number=input("give me the second number")
    if(first_number=="q" or second_number=="q"):
        flag=False
    else:
        try:
            outcome = int(first_number)/int(second_number)      #最开始吸收的是字符数字，需要将其转换为int型
        except ZeroDivisionError:
            print("You can't divide zero")
        else:
            print(outcome)


path=Path("C:\\Users\\48163\\Desktop\\file1.txt")
def read(path):
    try:
        content=path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("we can't find this file")
    else:
        content=content.split()
        print(content)
        print(f"this text contains {len(content)} words")
read(path)


def write(path,content):
    try:
        path.write_text(content)
    except FileNotFoundError:
        print("we cant't find the file")
    else:
        print(f"we write the \"{content}\" successfully")
content=input("what you want to say")
write(path,content)


from pathlib import Path
def file_read(path):
    try:
        content=path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print("we failed to find the file")
    else:
        print(content)
files=["file1.txt","file2.txt","file3.txt","file4.text"]
for file in files:
    file_read(Path(file))