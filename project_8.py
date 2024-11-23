#文件读写


from pathlib import Path
path=Path("C:Users\\48163\\Desktop\\file1.txt")     #绝对路径
contents=path.read_text()
print(contents)
print(contents.rstrip())
lines=contents.splitlines()     #将文本按行转化为列表
print(lines)
for line in lines:
    print(line)
path2=Path("hello_python.txt")      #相对路径
content2=path2.read_text()
print(content2)
str=""
for line in lines:
    str+=line
print(str)
content2=content2.replace("PYTHON","C")
print(content2)
content3=path2.read_text().splitlines()
print(content3)
content4="i love Python\ni love C too\n"
path2.write_text(content4)      #write_text()会删除文件原本内容并写入新内容
output=path2.read_text()
print(output)