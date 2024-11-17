#进一步补充列表的相关知识
#for循环的使用   range(m,n)  range(m,n,s)    list()  min()   max()   sum()   [:]    [m:]    [:n]    [number for number in numbers]     (num1,num2,num3,~~~)     (num1,)

cars=["audi","tesla","bmw","benz","prosche"]
for car in cars:
    print(car)
print("\n")
numbers=[7,3,5,1,8,2,4,0]
number1=[num for num in numbers]
print(number1)
number2=numbers[:]
print(number2)
number3=numbers
print(number3)
print("\n")
numbers.append(9)
print(number1)
print("\n")
print(number2)
print("\n")
print(number3)
print("\n")
number4=[num**2 for num in numbers]
print(number4)
print("\n")
for num in number4[:5]:
    print(num)
print("\n")
for num in number4[2:6]:
    print(num)
print("\n")
for num in number4[:]:
    print(num)
print("\n")
min=min(numbers)
max=max(numbers)
sum=sum(numbers)
print(f"最小值为{min},最大值为{max},总和为{sum}")
print("\n")
num=(1,3,5,7,9,8,6,4,2,0)
print(num)
num=(2,)
print(num)
print(num[0])
print("\n")
for value in range(1,5):
    print(value)
print("\n")
for value in range(1,8,2):
    print(value)
print("\n")
value=list(range(1,5))
print(value)
value=list(range(1,8,2))
print(value)