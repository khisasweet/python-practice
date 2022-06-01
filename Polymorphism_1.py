### The ability to change the superclass' behavior is called polymorphism #####

class Tracks:
  def change_direction(self, left, on):
    print("tracks: ", left, on)

class Wheels:
  def change_direction(self, left, on):
    print("wheels: ", left, on)

class Vehicle:
  def __init__(self, controller):
    self.controller = controller
  def turn(self, left):
    self.controller.change_direction(left, True)
    timer.sleep(0.25)
    self.controller.change_direction(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
    
    
