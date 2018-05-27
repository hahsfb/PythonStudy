class Car:
    """一次模拟汽车的简单测试"""

    def __init__(self, make, model, year, odometer=0):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer

    def get_descriptive(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer")


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year,  odometer=0):
        """初始化父类属性"""
        super().__init__(make, model, year, odometer)

my_tesla = ElectricCar('tesla', 'model s', 2016, 2000)
print(my_tesla.get_descriptive())
my_tesla.read_odometer()

my_tesla.update_odometer(100)
my_tesla.read_odometer()
