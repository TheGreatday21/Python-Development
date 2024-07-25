#creating an email regestration program
print("                            Hello and welcome to Google") 
print("          Please follow the prompts to have a quick and succesful sign up process Thank you (:")
#Asking for their personal details
print("Please type in your First _Name")
kil = input()
print("Please type in your Last name")
bil = input()
print("....................Nice to meet you", kil , bil ,"...................")
print("You can now create an email accout forexample name@gmail.com ")
zil = input()
print("Now create a strong password with atleast one capital Letter")
dil = input()
print("                   You have succesfully created your gmail account")
print("                   Now  start your sign in process")
#Asking for a sign in from the user
print("Please place in your newly created gmail account")
gil = input()
#Putting conditions
if gil == zil:
     print("Please insert your password")
     hil = input()
else:
    print("Sorry your email is incorrect try again later Thank You")

#Creating another variable for the passowrd
   
if hil == dil:
    print("Congratulations",bil,"....... You have succesfully signed into your google account")
else:
    print("Wrong password please try again")

