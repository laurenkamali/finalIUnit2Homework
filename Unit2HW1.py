'''
Name: Lauren Kamali
Date: 10/01/24
Description: Unit 2 Homework 1
'''

print('Problem 1'.center(20,'-'))
print('Fantasy')
print('Heros Journey')
print('Dream World')

print('Problem 2'.center(20,'-'))
print(""" _______  __   __  _______  _______  _______  _______    __   __  _______  __   __  ______      _______  _     _  __    _    _______  ______   __   __  _______  __    _  _______  __   __  ______    _______  __  
         |       ||  | |  ||       ||       ||       ||       |  |  | |  ||       ||  | |  ||    _ |    |       || | _ | ||  |  | |  |   _   ||      | |  | |  ||       ||  |  | ||       ||  | |  ||    _ |  |       ||  | 
         |       ||  |_|  ||   _   ||   _   ||  _____||    ___|  |  |_|  ||   _   ||  | |  ||   | ||    |   _   || || || ||   |_| |  |  |_|  ||  _    ||  |_|  ||    ___||   |_| ||_     _||  | |  ||   | ||  |    ___||  | 
         |       ||       ||  | |  ||  | |  || |_____ |   |___   |       ||  | |  ||  |_|  ||   |_||_   |  | |  ||       ||       |  |       || | |   ||       ||   |___ |       |  |   |  |  |_|  ||   |_||_ |   |___ |  | 
         |      _||       ||  |_|  ||  |_|  ||_____  ||    ___|  |_     _||  |_|  ||       ||    __  |  |  |_|  ||       ||  _    |  |       || |_|   ||       ||    ___||  _    |  |   |  |       ||    __  ||    ___||__| 
         |     |_ |   _   ||       ||       | _____| ||   |___     |   |  |       ||       ||   |  | |  |       ||   _   || | |   |  |   _   ||       | |     | |   |___ | | |   |  |   |  |       ||   |  | ||   |___  __  
         |_______||__| |__||_______||_______||_______||_______|    |___|  |_______||_______||___|  |_|  |_______||__| |__||_|  |__|  |__| |__||______|   |___|  |_______||_|  |__|  |___|  |_______||___|  |_||_______||__| """)

print('Problem 3'.center(20,'-'))
seattle_distance = 173.8
mpg = int(input("How many miles per gallon does your car get? "))
ppg = float(input("How much does a gallon of gas cost near your house? "))
gas_capacity = int(input("How many gallons of gas does your car hold? "))
fraction_filled = float(input("What fraction of your tank did you fill up? (for example, 0.5 for half, 1 for full) "))
gallons_needed = seattle_distance/mpg
cost_of_trip = (gallons_needed * ppg) * fraction_filled
print(f"The cost to drive from Portland to Seattle is approximately ${cost_of_trip}")
