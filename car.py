class Car(object):

    def __init__(self, price, speed, fuel, mileage, tax=.12):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.milage=mileage
        if self.price>=10000:
            self.tax=.15
        else:
            self.tax=tax


    def display_all(self):
        print 'Price: ${} \n Top Speed: {}mph \n Fuel: {} \n Mileage: {}mpg \n Tax: {}'.format(self.price, self.speed, self.fuel, self.milage, self.tax)


car1=Car(15999, 30, 'full', 0)
car2=Car(1999, 120, 'empty', 0)

car1.display_all()
car2.display_all()
