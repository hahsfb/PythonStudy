from MyStudy.electric_car import Car


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
