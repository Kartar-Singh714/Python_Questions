# def format_name(fname, lname):
#     corrected_name = fname.title()
#     corrected_lname= lname.title()
#     return corrected_name, corrected_lname
#result = format_name("kaRTar", "SinGH")

#without function
n = input("Please enter the name to be standardised formatted: ")
name_list= n.split()
formatted = ''
length_name_list = len(name_list)

for name in range(length_name_list):
    first_word= name_list[name]
    word_length = len(first_word)
    for alphabet in range(word_length):
       if alphabet == 0:
           alpha = first_word[alphabet].upper()
           formatted = formatted + alpha
       else:
            alpha = first_word[alphabet].lower()
            formatted = formatted + alpha
    formatted+= " "

print (formatted)
