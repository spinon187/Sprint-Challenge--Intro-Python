# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class
class Vehicle:
  def __init(self):
    pass

#vehicle subclass
class FlightVehicle(Vehicle):
  def __init(self):
    super().__init__()

#flight vehicle subclass
class Starship(FlightVehicle):
  def __init(self):
    super().__init__()

#flight vehicle subclass
class Airplane(FlightVehicle):
  def __init(self):
    super().__init__()

#vehicle subclass
class GroundVehicle(Vehicle):
  def __init(self):
    super().__init__()

#ground vehicle subclass
class Car(GroundVehicle):
  def __init(self):
    super().__init__()

#ground vehicle subclass
class Motorcycle(GroundVehicle):
  def __init(self):
    super().__init__()