# ↓↓↓ GETTING HEIGHT & WEIGHT ↓↓↓

height = input("Please enter your height in meters: ")
weight = input("Please enter your weight in kilograms: ")

# ↓↓↓ BMI CALCULATING ↓↓↓

bmi = int(weight) / float(height) ** 2
bmi_convert = int(bmi)

# ↓↓↓ PRINTING RESULTS ↓↓↓

print(bmi_convert)
from PIL import Image
