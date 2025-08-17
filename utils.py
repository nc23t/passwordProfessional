import re
import string



def length(user_password):
    if len(user_password) <= 6:
        print("Your password is only", len(user_password), "characters long, add a lot more!")
        ptsL = 2
        print('Your score for length is', ptsL,'points')
        return ptsL
    elif 6 < len(user_password) <= 10:
        print('Your password length is', len(user_password), 'characters, you could add more')
        ptsL = 3
        print('Your score for length is', ptsL,'points')
        return ptsL
    elif 11 <= len(user_password) <= 16 :
        print('Your password is', len(user_password), 'characters, add just a little more!')
        ptsL = 5
        print('Your score for length is', ptsL,'points')
        return ptsL
    elif 17 <= len(user_password) < 20:
        print('Your password is', len(user_password), 'characters, you can make it to 20!')
        ptsL = 7
        print('Your score for length is', ptsL,'points')
        return ptsL
    elif len(user_password) == 20:
        print('Your password is', len(user_password), 'characters long, perfect length!')
        ptsL = 10
        print('Your score for length is', ptsL,'points')
        return ptsL
    elif len(user_password) > 20:
        print('Your password is', len(user_password), "characters, this too long!")
        ptsL = 7
        print('Your score for length is', ptsL,'points')
        return ptsL
      
      
        
def upper(user_password):
    upperCounter = 0
    for char in user_password:
        if char.isupper():
            upperCounter += 1
    if (upperCounter < 1):
        print("The total number of uppercase in your password is:",upperCounter)
        print("Add at least 1 uppercase character.")
        ptsU = 0
        print('Your score for uppercase is', ptsU,'points') 
        return ptsU                
    elif(upperCounter >= 1):
        print("The total number of uppercase in your password is:",upperCounter)
        print('Good amount of uppercase characters.')   
        ptsU = 8   
        print('Your score for uppercase is', ptsU,'points')
        return ptsU                  
    
    
def number(user_password):
    numberCounter = 0
    for num in user_password:
        if num.isnumeric():
            numberCounter += 1
    if(numberCounter >= 1):
        print('You have', numberCounter,"numbers in your password.")
        print('Valid amount of numbers') 
        ptsN = 8
        print('Your score for numbers is', ptsN,'points')
        return ptsN 
    elif(numberCounter < 1):
        print('You have', numberCounter,"numbers in your password.")
        print("Add at least one number to your password")  
        ptsN = 0
        print('Your score for numbers is', ptsN,'points')
        return ptsN
        
        
def special(user_password):
    pattern = r'[^a-zA-Z0-9\s]'
    specialCharacters = re.findall(pattern, user_password)
    count = len(specialCharacters)
    if(count >= 3):
        print(count,"speical characters contained in your password")
        print('Valid amount of special characters.') 
        ptsS = 10
        print('Your score for special characters is', ptsS, 'points')
        return ptsS
    elif(count < 3):
        print(count,"speical characters contained in your password")
        print("Add more special charcaters to your password.")
        ptsS = 0
        print('Your score for special characters is', ptsS, 'points')
        return ptsS
    
    
def scoring(total):
    if (total >= 30):
        print('You have a strong password!')
    elif(total <= 20):
        print('Your password is WEAK')
    elif(20 < total <30):
        print('Your password is OK')

      

    

        
        
        

    








 
      