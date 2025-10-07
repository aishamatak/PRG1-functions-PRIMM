def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(100))


# Changing the function to work out Farenheit into Celsius 
def farenheit_to_celsius(farenheit): 
    celsius = (farenheit - 32) / 9/5 
    return celsius 

# Converting from kilometers to miles 
def kilometers_to_miles(kilometers):  
    miles = kilometers * 0.621371
    return miles 

# Converting from miles to kilometers 
def miles_to_kilometers(miles):
    kilometers = miles / 0.621371
    return kilometers 