#TEMPERATURE CONVERSION 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

try:
    degrees = int(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()  # Exit the program if the input is invali

type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{degrees}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{degrees}°C is {fahrenheit}°F")

if type == 'F':
    convert_to_celsius(degrees)

elif type == 'C':
    convert_to_fahrenheit(degrees)

else:
    print("Enter only celsius or farhrenheit.")
