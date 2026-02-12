class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car = Vehicle("Tesla", "Model 3")
# print(my_car.make)
# print(my_car.model)
my_car.moves()
my_car.get_make_model()

your_car = Vehicle("cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("flies along...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class Golf_Cart(Vehicle):
    def moves(self):
        pass


cessna = Airplane("cessna", "skyhawk", "N-2452628")
mack = Truck("mack", "pinnacle")
golf_wagon = Golf_Cart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golf_wagon.get_make_model()
golf_wagon.moves()

# polyM

print("\n\n")
for v in (my_car, your_car, cessna, mack, golf_wagon):
    v.get_make_model()
    v.moves()
