#这个程序主要介绍一些关于列表的基础操作
#.append('字符')  insert(number,'字符')  del(元素)  .pop()  .pop(number)  .remove('字符')  .sort()  .sort(reverse=True)  sorted(列表名)  .reverse()  len(列表名)
word=['man','what can i say','out !','hahaha','孩子们','牢大']
print(word)
print(word[-2])
word.append('xixixi')
print(word)
word.insert(3,'bu xixi')
print(word)
del word[1]
print(word)
bridge=word.pop()
print(word)
print(bridge)
bridge=word.pop(2)
print(bridge)
print(word)
word.remove('孩子们')
print(word)
word.sort()
print(word)
word.sort(reverse=True)
print(word)
print(sorted(word))
print(word)
word.reverse()
print(word)
lenth=len(word)
print(lenth)