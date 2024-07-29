a = int(input('Please enter a catheter a '))

b = int(input('Please enter a catheter b '))

hyp_value = float(((a ** 2) + (b ** 2)) ** (1 / 2))

right_tri_area = float((a * b) / 2)

print(f"Length of the hypotenuse with catheters a and b is: (({a}**2) + ({b}**2)) ** (1/2) = {hyp_value}")

print(f"Area of a right triangle with catheters a and b is: sqrt of ({a}*{b})/2 = {right_tri_area}")
