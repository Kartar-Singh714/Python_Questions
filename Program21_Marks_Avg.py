# Write Python program that accepts marks in 5 subjects and outputs average marks.
eng_marks = input("Enter the marks for the English: ")
hindi_marks = input("Enter the marks for the Hindi: ")
sci_marks = input("Enter the marks for the Science: ")
maths_marks = input("Enter the marks for the Maths: ")
social_marks = input("Enter the marks for the Social Science: ")


if eng_marks.replace(".", "").isdigit() and hindi_marks.replace(".", "").isdigit() and sci_marks.replace(".", "").isdigit() and maths_marks.replace(".", "").isdigit() and social_marks.replace(".", "").isdigit():
    avg = (float(eng_marks)+float(hindi_marks)+float(sci_marks)+float(maths_marks)+float(social_marks))/5
    print(f"\nThe average marks is {avg}")
else:
    print("\nPlease enter the valid numbers")
