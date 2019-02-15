def kelvin(temperature):
    assert(temperature>=0),'colder than absolute'
    return((temperature-273)*1.8)+32
try:
    print(kelvin(273))
    print(kelvin(505.78))
    print(kelvin(-5))
except(AssertionError):
    print("error occured")
    
