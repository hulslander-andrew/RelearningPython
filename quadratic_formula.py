#Andrew Hulslander
#23 December 2020
#Python3
#Quadratic Equation / Formula


A = float(input("A ? : " ))
B = float(input("B ? : " ))
C = float(input("C ? : " ))

root_1 = (B * -1 + ((B ** 2) - 4 * A * C) ** 0.5) / (2 * A) 
root_2 = (B * -1 - ((B ** 2) - 4 * A * C) ** 0.5) / (2 * A) 

print("x = " + str(root_1)) 
print("x = " + str(root_2))

#I do not know how to include complex numbers yet so imaginary numbers cause an error
