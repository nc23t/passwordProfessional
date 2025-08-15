# strong password is 20 characters long, 
# with at least 1 uppercase letter, 1 number, 
# and 3 special characters
# gives points for length# gives points for character variety (lower/upper/digit/symbol)
# clamps to 0 - 100
# maps to labels: weak / ok / strong

import re
import string
from utils import length, upper, number

print('Welcome to passwordProfessional, lets see how strong your password is!')
print('Rule of thumb: 20 chararacters long, at least 1 upper case character and 1 number')


user_password = input('Input your password:')
length(user_password)
upper(user_password)
number(user_password)








    