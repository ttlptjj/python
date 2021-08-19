"""9-9"""
class car():

    def __init__(self,make,model,year):
        self.make = make
	self.model = model
	self.year = year
	self.odometer_reading = 0


    def get_descriptive_name(self):
	long_name = str(self.year) + ' ' + self.make + ' ' + self.model
	return long_name

    def read_odometer(self):
	print("This car has " + str(self.odometer_reading) + " miles on it.")
 
    def update_odometer(self, milegeage):
	if milegeage >= self.odometer_reading:
	    self.odometer_reading = milegeage
	else:
	    print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
	self.odometer_reading += miles

class Battery():

     def __init__(self, battery_size=70):
	self.battery_size = battery_size

     def describe_battery(self):
         print("This car has a " + str(self.battery_size) + "-kWh battery")

     def upgrade_battery(self):
         if self.battery_size != 100:
	      self.battery_size = 100

     def get_range(self):
	if self.battery_size == 70:
	    range = 240
	elif self.battery_size == 100:
	    range = 400
	message = "This car can go approximately " + str(range)
		
	print(message)
	self.upgrade_battery()

class ElectricCar(Car):
	

     def __init__(self, make, model, year):
	super().__init__(make, model, year)
	self.battery_size = Battery()
	
    def describe_battery(self):
	self.battery_size.battery_size()

    def get_range(self):
	self.battery_size.get_range()


Car = ElectricCar('dazhong', 'S', 2021)
Car.get_range()
Car.get_range()
      
