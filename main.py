import random
import fractions

class MainCar():
    def __init__(self, gastank=None, wheels=None, engine=None):
        self.gastank = gastank
        self.wheels = wheels
        self.engine = engine

    class GasTank():
        def __init__(self, storage=None):
            self.storage = str(random.randint(45, 60)) + " litres"

        def showStorageSize(self):
            try:
                print("Tank Size: ", self.storage)
            except NameError as exc:
                raise Exception('Unexpected fault creating volume.')

    class Engine():
        def __init__(self, horsepower=None):
            self.horsepower = str(random.randint(120, 450)) + " hp"

        def showHorsePower(self):
            try:
                print("Horsepower: ", self.horsepower)
            except NameError:
                raise Exception('Unexpected fault creating horsepower.')

    class Wheels():
        brands = ['Michelin', 'Good Year', 'Bridgestone', 'Continental', 'BFGoodrich', 'Dunlop', 'Firestone']
        def __init__(self, treadDepth=None, Brand=None, YearsUsed=None, brandList=brands):
            # new tire tread - 10/32
            self.treadDepth = "".join(str(random.randint(2,8)) + "/32")
            self.brand = random.choice(brandList)
            self.YearsUsed = random.randint(3,7)

        def getTreadDepth(self):
            try:
                print("Tire Thread Depth: ", self.treadDepth)
            except NameError:
                raise Exception('Unexpected fault creating Thread Depth.')

        def getBrand(self):
            try:
                print("Brand: ", self.brand)
            except NameError:
                raise Exception('Unexpected fault creating Brand.')

        def getYearsUsed(self):
            try:
                print("Years Used: ", self.YearsUsed)
                # print(self.treadDepth.split('/')[0])
                # print(self.treadDepth.split('/')[1])
                print("Thread Depth Diteration Rate: ", fractions.Fraction(self.treadDepth.split('/')[0] + '/' + self.treadDepth.split('/')[1]) / 10/32))
            except NameError:
                raise Exception('Unexpected fault creating Years Used.')


    gastank = GasTank()
    engine = Engine()

car = MainCar()

car.GasTank().showStorageSize()
car.Engine().showHorsePower()
car.Wheels().getYearsUsed()
car.Wheels().getBrand()
car.Wheels().getTreadDepth()