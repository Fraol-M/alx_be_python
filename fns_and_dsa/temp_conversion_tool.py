FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsisu = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsisu

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


temp = float(input("Enter the temperature to convert: "))
check = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
match check:
    case "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C") 
    case "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    case _:
        print("Invalid temperature. Please enter a numeric value.")
        
        
