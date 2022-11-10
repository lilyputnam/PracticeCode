#This is a program that tells you whether a triangle is isoceles, scalar, or equilateral

side_1 = int(input("Enter the length of the first side\n\n"))
side_2 = int(input("Enter the width of the second side\n\n"))
side_3 = int(input("Enter the height of the third side\n\n"))

if side_1 == side_2 == side_3:
    print("The triangle is equilateral")

if side_1 == side_2 and side_1 != side_3\
    or side_1 == side_3 and side_1 != side_2 \
    or side_2 == side_3 and side_2!= side_1:
  print("The triangle is isoceles")

if side_1 != side_2 != side_3 :
    print("The triangle is scalar")

'''
print("I believe that:"
    "\nside_1 = 6, side_2 = 6, side_3 = 6, output = equilateral"
    "\nside_1 = 6, side_2 = 5, side_3 = 5, output = isoceles"
    "\nside_1 = 5, side_2 = 6, side_3 = 5, output = isodeles"
    "\nside_1 = 5, side_2 = 5, side_3 = 6, output = isoceles"
    "\nside_1 = 6, side_2 = 5, side_3 = 4, output = scalar")
    '''
