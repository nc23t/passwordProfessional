# strong password is 20 characters long, DONE
# with at least 1 uppercase letter, 1 number, DONE
# and 3 special characters DONE
# gives points for length# gives points for character variety (lower/upper/digit/symbol) DONE
# maps to labels: weak / ok / strong

import re
import string
from utils import length, upper, number, special, scoring


print('Welcome to passwordProfessional, lets see how strong your password is!')


user_password = input('Input your password:')
score_length = length(user_password)
score_upperCase = upper(user_password)
score_number = number(user_password)
score_special = special(user_password)

#NEED to tweak the scoring system, 'FU' as a password gets an 'OK' score which is should definitely not get.


total = score_length + score_upperCase + score_number + score_special
print("Your total score is " + str(total) + '/40')

scoring(total)











    