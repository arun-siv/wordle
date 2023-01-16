from pprint import pprint
import re
# open a file for reading
with open(r'C:\Users\arunsiva\Downloads\words.txt', 'r') as f:
    # read the entire file as a single string
    data = f.read().split()


data = [ w.lower() for w in data if 
len(w) == 5 and w.isalpha()
# and w[0] == 'l'
# and w[1] == 'i'
and w[2] == 's'
and w[3] == 't' 
and w[4] == 'y'
 ]

###################################################################################

# data = [ w for w in data if w[0] == 'm']

# # data = [ w for w in data if not re.search('n\Z',w,re.I)]
# # data = [ w for w in data if not re.search('on\Z',w,re.I)]
# # data = [ w for w in data if not re.search('lon\Z',w,re.I)]
################################################################################

x = 'pricebu'
x = list(x)
check_char_not_present = lambda word: lambda x: True if x not in word.lower() else False

##########################################################################################
# def check_char_not_present(word):
#     def char_not_in_word(char):
#         return char not in word
#     return char_not_in_word

############################################################################################

data = [ w for w in data if 
all(list(map(check_char_not_present(w),x)))
]
##########################################################################################
# letters_to_avoid = 'lscdk' #eliminate all words  which doesnt have the alphabets l,s,c,d,k 

# filtered_words = [
#                  word for word in words
#                  if all(letter not in word for letter in letters_to_avoid)
#                  ]


#--------------------------------------------------------------------------------------
# filtered_words = [
#                  w for w in words if 
#                  all(letter not in w for letter in x)
#                  ] 
# # words is already filtered list of words which has length 5
############################################################################################






#-----------------not required----------------------------------------------------------------

# data = [ w for w in data if all(letter not in w for letter in x ) ]

# y ='pe'
# check_char_present = lambda word: lambda x: True if x  in word else False
# data = [ w for w in data if 
#  all(list(map(check_char_present(w),list(y))))
#  ]

# y = 'r'
# data = [ w for w in data if all(letter in w for letter in y)]

# # data = [ w for w in data if not re.search('on$',w,re.I)]

# # pprint(data)
