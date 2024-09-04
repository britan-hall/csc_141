# previous program from "04_09_cube_comprehension"
cubes = [base**3 for base in range (1,11)]
print(cubes)

print('-----------------------------------------------------------------')
print(f'The first three items in the list are: {cubes[:3]}')
print(f'Three items from the middle of the list are: {cubes[3:7]}')
print(f'The last three items in the list are: {cubes[7:]}')
print('-----------------------------------------------------------------')