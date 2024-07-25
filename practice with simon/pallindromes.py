def is_palindrome(text):
    cleaned_text = ''.join([c for c in text if c.isalnum()]).lower()#'' means  that we are to get a string  , .join means joining the strings and we create a list with a for loop in it where we tell it that the input must be text and not number. And we then convert everything to lower with the .lower function 
    print("""Cleaned text : {}""".format(cleaned_text))#the double """" is a way of formatting to tel python to 
    return cleaned_text == cleaned_text[::-1]#reverse function
print(is_palindrome("A man, a plan, a canal, Panama"))









