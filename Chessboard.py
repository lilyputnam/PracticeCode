#This is a program that can tell you if the square youve chosen from a chessboad is black or white


row_letter = 0

choice_row = (input("Enter the row letter of the square\n\n"))

if choice_row.lower() == ("a" or "c" or "e" or "g"):
    row_letter = 1

choice_colour = int(input("Enter the column number of the square\n\n"))
coordinate_reference = choice_colour + row_letter

if coordinate_reference % 2 == 0:
    print("\nThe square is black""\n\n")
else:
    print("\nThe square is white""\n\n")

'''
print("I believe that:''
    "\nchoice_row = a, choice_colour = 1, output = black"
    "\nchoice_row = f, choice_colour = 3, output = white")'''

