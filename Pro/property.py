class Celsius:
    def __init__(self,temperature=0):
        self.__temperature=temperature #automatically calls the set_temperature
    def get__Temperature(self):
        print("getting the value")
        return self.__temperature
    def set__Temperature(self,value):
        print("setting the value")
    def to_farenheit(self):
        return (self.__temperature *1.8) +32

    __temperature=property(get__Temperature,set__Temperature)
    #here the temperature is the propetrty object
obj=Celsius()
obj.to_farenheit()
