# The distance between two cities is input through keyboard. 
# Write a program to convert and print this distance in feet, meter, inch and centimeter.

distance_km = float(input("Enter the distance between two cities in kilometers: "))

feet = 3280 
meter = 1000  
inch = 39370.1  
centimeter = 100000  

print("\n------------------------------------------------- \n")
print("Distance in feet:", distance_km * feet)
print("Distance in meters:", distance_km * meter)
print("Distance in inches:", distance_km * inch)
print("Distance in centimeters:", distance_km * centimeter)

 