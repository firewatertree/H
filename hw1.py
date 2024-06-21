#1-1
a=7.4
b=5
c=21.7
d=0.5**0.5+7*3






m1 =input('the mass of m1: ')
m2 =input('the mass of m2: ')
r =input('the distance: ')
G =input('graverity: ')
# Calculate the force using the formula
F = G * m1 * m2 / (r ** 2)

# Print the calculated force
print(F)



m1 = float(input('the mass of m1: '))
m2 = float(input('the mass of m2: '))
u1 = float(input('the velocity before: '))
u2 = float(input('the velocity before: '))
v1 = float(input('the velocity after: '))
v2 = float(input('the velocity after: '))

initial_energy = 0.5 * m1 * u1**2 + 0.5 * m2 * u2**2
final_energy = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2

if initial_energy == final_energy:
    print("Kinetic energy is conserved.")
else:
    print("Kinetic energy is not conserved.")





