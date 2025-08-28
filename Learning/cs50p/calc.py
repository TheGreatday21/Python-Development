#this is a calculator that handles errors of a user inputing data that is not digits

x = input("First number: ")
y = input("Second number: ")


if x.isdigit() and  y.isdigit():
    z = int(x) + int(y)
    print(f"Your answer is {z}")

    #therer is a way to specify our output to have commas over long numbers 
    print(f"{z:,}") #we first place inthe : then we specify the format after 
    #or
    print(f"{z:.4f}") #this prints the output rounded to 4 decimal places
else:
    print("The input has to be whole numbers ")


#round function 
decimalNum = round((float(x) / float(y)),2)#rounding this to 2decimal places 
print(decimalNum)