a = int(input('Please enter a '))

b = int(input('Please enter b '))

arith_mean = float((a + b) / 2)

geom_mean = float((a * b) ** (1/2))

print(f"Arithmetic mean of a and b is: ({a}+{b})/2 = {arith_mean}")

print(f"Geometric mean of a and b is: sqrt of ({a}*{b}) = {geom_mean}")
