#This is a login programme

print('\nLogin')

login_details = {'user1':'lily123', 'user2':'aiden123', 'user3':'momo123'}

print('\nHi! Please enter your login details. You have 3 attempts')
attempt = 0
while attempt < 3:
    print('\nEnter your username and password')
    user_name = input('\nUsername: ')
    password = input('Password: ')

success = False
for key, value in login_details.items():
    if (key == user_name
        and value == password):
        success = True
        break
attempt += 1
if not success:
    if attempt < 3:
        print('\nSorry your login details are incorrect. Please try again\n')
    else:
        print('\nSorry your three attempts have been used')
else:
        break

if success:
        print('\nYou are now logged in')