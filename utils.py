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
    if (upperCounter < 1):
        print("The total number of uppercase in your password is:",upperCounter)
        print("Add at least 1 uppercase character.")
    elif(upperCounter >= 1):
        print("The total number of uppercase in your password is:",upperCounter)
        print('Good amount of uppercase characters.')                       
    
    
def number(user_password):
    numberCounter = 0
    for num in user_password:
        if num.isnumeric():
            numberCounter += 1
    if(numberCounter >= 1):
        print('You have', numberCounter,"numbers in your password.")
        print('Valid amount of numbers') 
    elif(numberCounter < 1):
        print('You have', numberCounter,"numbers in your password.")
        print("Add at least one number to your password")   
        
        
def special(user_password):
    pattern = r'[^a-zA-Z0-9\s]'
    specialCharacters = re.findall(pattern, user_password)
    count = len(specialCharacters)
    if(count >= 3):
        print(count,"speical characters contained in your password")
        print('Valid amount of special characters.')
    elif(count < 3):
        print(count,"speical characters contained in your password")
        print("Add more special charcaters to your password.")
        
      
        
        
        

    








 
      