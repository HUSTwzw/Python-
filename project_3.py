#基础知识：and   or    if    elif    else    in    not in
#检查新名字和旧名字是否重复（不区分大小写），若重复，不允许创建此名字
current_users=["Mack","Jack","Leo","Lucy","Jessy"]
new_users=["Trump","Biden","JACK","LEO","Taylor","Donald"]
current_small=[]
for name in current_users:
    current_small.append(name.lower())
for name in new_users:
    if name.lower() in current_small:
        print(f"we already have {name},you have to change it!")
    if name.lower() not in current_small:
        print(f"OK, your name will be {name}")
