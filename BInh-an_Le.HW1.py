
class Location : 
    def __init__(self,x,y) -> None:
        self.x = 0
        self.y = 0
    
    def __str__(self) -> str:
        return (self.x,self.y)
    
class Car :
    def __init__(self,name,location,cpm):
        self.nameb= 0
        self.location = 0
        self.cpm = 0

class Passenger :
    def __init__(self,name, location):
        self.name = 0
        self.location = 0

class RideSharingApp: 
    def __init__(self,cars,passengers) :
        self.cars = 0
        self.passengers = 0
