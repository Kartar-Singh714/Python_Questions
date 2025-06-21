#WAP
# User input - "my name is kartar singh" O/P -> "YM EmaN SI RatraK HgniS"


n = "my name is kartar singh"
name_list= n.split()
formatted = ''
reversed_word = ''
output_string = ''
length_name_list = len(name_list)

####### Approach 1 #######
for name in range(length_name_list):
    first_word= name_list[name]
    word_length = len(first_word)
    for alphabet in range(word_length-1, -1, -1):
       if alphabet == 0 or alphabet == word_length-1:
           alpha = first_word[alphabet].upper()
           formatted = formatted +alpha
       else:
            alpha = first_word[alphabet].lower()
            formatted = formatted + alpha
    formatted += " "


####### Approach 2 #######
# for name in range(length_name_list):
#     first_word= name_list[name]
#     word_length = len(first_word)
#     for alphabet in range(word_length):
#        if alphabet == 0 or alphabet == word_length-1:
#            alpha = first_word[alphabet].upper()
#            formatted = formatted +alpha
#        else:
#             alpha = first_word[alphabet].lower()
#             formatted = formatted + alpha
#     formatted += " "
#
#
# reversed_word = formatted[::-1].lstrip()
# ind_word = reversed_word.split()
# for words in ind_word:
#     output_string =  words + " " + output_string

print(n)
print(formatted)
#print(reversed_word)
#print(output_string)