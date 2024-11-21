
class Users:
    def __init__(self,first_name,last_name,information=None):
        self.first_name=first_name
        self.last_name=last_name
        if information:
            self.information=information
        else:self.information=None
    def describe(self):
        print(f"{self.first_name.title()} {self.last_name}'s information:")
        print(f"{self.information}")
    def greet_users(self):
        print(f"Hello,{self.first_name.title()} {self.last_name},I am glad to meet you!")

customer1=Users("wang","zi wen","age=18")
customer2=Users("shan","shuai chao","age=17")
customer3=Users("yang","xi lei","age=18")
print(customer1.first_name,customer1.last_name,customer1.information)
print(customer2.first_name,customer2.last_name,customer2.information)
print(customer3.first_name,customer3.last_name,customer3.information)
print("\n")
customer1.describe()
customer1.greet_users()
customer2.describe()
customer2.greet_users()
customer3.describe()
customer3.greet_users()
print("\n")


class Restaurant:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
        self.number=0
    def show(self):
        print(f"{self.name} payed {self.pay}$")
    def served_number(self,num):
        self.number+=num
day1=Restaurant("Trump's family","10000")
day2=Restaurant("Biden's family","5000")
day1.show()
day1.served_number(5)
day2.show()
day2.served_number(3)
print(day1.number)
print(day2.number)
print("\n")


class Cars:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def introduction(self):
        print(f"{self.brand} {self.model} {self.year}")
class Battery:
    def __init__(self,battery=40):
        self.battery_size=battery
    def introduct(self):
        print(f"we still have {self.battery_size}kwh power,don't worry")
class Electric_cars(Cars):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)
        self.battery=Battery()
my_car=Electric_cars("audi","A7","2024")
my_car.introduction()
my_car.battery.introduct()