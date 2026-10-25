
#? Convert temperature from Celsius to Fahrenheit and back.

#* converting C -> F  
#* F =(C*1.8)+32
celsius = float(input("Enter the celsius temperature for converting : "))
# celsius = float(input("Enter the fahrenheit temperature for converting : "))
#? Fahrenheit
fahrenheit = (celsius * 1.8)+32
celsius = (fahrenheit - 32)*5/9
print(f" for given celsius converting into fahrenheit is : {fahrenheit} F")
print(f" for given fahrenheit converting into celsius is : {celsius} C")

