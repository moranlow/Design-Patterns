#Facade
#I will use facade pattern here to delegate most of the work to other classes
#I have 4 classes each of which must do his job
#With this design pattern I will put all the logic in one class

class Investor:
    def invest(self):
        print("Investing...")


class Vendor:
    def give(self):
        print("Giving the materials...")


class Builder:
    def build(self):
        print("Building...")


class Visitor:
    def visit(self):
        print("Visiting...")


class BuildingFacade:
    def __init__(self):
        self.investor = Investor()
        self.vendor = Vendor()
        self.builder = Builder()

    def build_project(self):
        for i in range(3):
            self.investor.invest()

        for i in range(50):
            self.vendor.give()

        for i in range(200):
            self.builder.build()

        print("Project finished!")


class Facade:
    def __init__(self):
        self.building_facade = BuildingFacade()
        self.visitor = Visitor()

    def start_project(self):
        self.building_facade.build_project()
        for i in range(100):
            self.visitor.visit()


if __name__ == '__main__':
    facade = BuildingFacade()
    facade.build_project()
