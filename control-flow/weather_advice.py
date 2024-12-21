# Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.
# Description: Create a Python script named weather_advice.py. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

# Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
weather = input("What's the weather like today? (sunny,rainy,cold) : ").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
