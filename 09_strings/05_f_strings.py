#String formatting with f-strings

invetetion = "Hey {} your are very smart welcome to our company take the token money {}$"

a = "Sumit"
a1 = 10000
b = "Harry"
b1 = 1000
c = "Rohan" 
c1 = 500

v = invetetion.format(a, a1)

print(v)

print(f"Hey {a} your are doing great work keep it up and take this money {a1}$")
print(f"Hey {b} your are doing great work keep it up and take this money {b1}$")
print(f"Hey {c} your are doing great work keep it up and take this money {c1}$")