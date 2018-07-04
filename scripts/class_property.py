# Final Note that, the actual Temperature is stored in the private variable _temperature & the attribute temperature
# is a property which provides interface to this private variable.


class Celsius(object):
    def __init__(self, temperature=0):
        #self.set_temperature(temperature)
        self.temperature = temperature
    
    def to_fahrenheit(self):
        print "Convert to Fahrenheit"
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print "Temperature:"
        return self._temperature
    
    def set_temperature(self, value):
        print "Setting Value... "
        self._temperature = value
    
    temperature = property(get_temperature, set_temperature)

c = Celsius()
print c.temperature
c.get_temperature()

c.temperature = 1020
c.get_temperature()

print c.get_temperature()