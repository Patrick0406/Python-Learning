# -*- coding: utf-8 -*-
class Car():

    def __init__(self, maker, model, year):
        self.maker=maker
        self.model=model
        self.year=year
        self.odometer_reading= 0

    def get_descriptive_name(self):
        long_name= str(self.year)+' '+ self.maker+ ' '+ self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading)+" miles on it.")

    def update_odometer(self):
        flag=1                                                             #用于判断用户是否需要继续输入
        mileage=0                                                          #初始化里程数为0
        while(flag):
            while(float(mileage)<=float(self.odometer_reading)):                  
                mileage=input("Please enter mileage: ")
                if float(mileage)<=float(self.odometer_reading):
                    print("You can't roll back the odometer")
            self.odometer_reading=mileage
            self.read_odometer()
            flag=0
            a=input("Do you want to change the odometer, if so, enter 'Yes': ")
            if a=='Yes':
                flag=1


my_new_car= Car('Audi', 'a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer()