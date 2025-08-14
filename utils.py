import re
import string




def length(user_password):
    if len(user_password) <= 6:
        print("Your password is only", len(user_password), "characters long, add a lot more!")
        # gets 2 pts
    elif 6 < len(user_password) <= 10:
        print('Your password length is', len(user_password), 'characters, you could add more')
        #gets 3 pts
    elif 11 <= len(user_password) <= 16 :
        print('Your password is', len(user_password), 'characters, add just a little more!')
         # gets 5 pts
    elif 17 <= len(user_password) < 20:
        print('Your password is', len(user_password), 'characters, you can make it to 20!')
        #gets 7 pts
    elif len(user_password) == 20:
        print('Your password is', len(user_password), 'characters long, perfect length!')
        #gets 9 pts
    elif len(user_password) > 20:
        print('Your password is', len(user_password), "characters, this is too long!")
        #gets 7 pts
        
def upper(user_password):
    upperCounter = 0
    for char in user_password:
        if char.isupper():
            upperCounter += 1
            if (upperCounter <= 1):
                print("You need more uppercase letters!")
                # gets 1 pt
            elif(upperCounter <= 2):
                print("You still need more uppercase letters")
            elif(upperCounter >= 3):
                print("Perfect amount of uppercase letters!")         
    print("The total number of uppercase in your password is:", upperCounter)
        
    








 
      