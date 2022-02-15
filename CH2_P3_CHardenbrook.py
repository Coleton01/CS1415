"""
Chapter 2_Project 3: video rental calculator
date: 09/10/2020
This program will calculate total value of media to be rented
and billed to client.
"""
#initialize constants
oldmedia= float(2.00)
newmedia= float(3.00)

#request inputs
totalnew= int(input("enter the number of new items: "))
totalold= int(input("enter the number of old items: "))

#calculations
Total= (totalnew*newmedia) + (totalold*oldmedia)

#output
print("$",Total, "is your total cost for renting.")
