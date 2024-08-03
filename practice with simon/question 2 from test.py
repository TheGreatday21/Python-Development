''''
#2. Conditional Statements & Lists: # type: ignore
# Write a Python program that asks the user to input their grades for five different subjects. Store these grades in a list. 
#Then, use conditional statements to determine if the student has passed or failed. (Assume a passing grade is 50 or higher.)
#Print "Pass" if the student has passed all subjects, otherwise print "Fail." # type: ignore



A = int(input("What did you get in  Math : "))
B = int(input("What did you get in  Chemistry : "))
C = int(input("What did you get in  Physics : "))
D = int(input("What did you get in General Paper : ")) 
E = int(input("What did you get in  Computer studies : "))
D = [A,B,C,D,E]

print(D)

count = 0 
for num in D :
    if num < 50:
        count += 0
    else :
        count += 1
if count >=5:
    print("Congratulations nigga ,\n\t ....PASSED.....")
else:
    print("Iam sorry to say but try again next time, \n\t...FAILED...")

'''

#3. Loops & Strings:
#At Uganda Christian University, students are assigned unique IDs consisting of the prefix "UCU" followed by a number (e.g., UCU12345). 
#Write a Python program that generates a list of 10 student IDs starting from "UCU10001" to "UCU10010" using a loop. 
# Then, print each ID on a new line.

for i in range (1,11):
    a = list((f"UCU100{i}"))
    print(a)



#4. Tuples, Sets, & Dictionaries:
#Uganda Christian University offers various programs in different faculties. 
# Create a tuple containing three faculties. For each faculty, create a set of three programs offered. 
# Finally, create a dictionary where the keys are the faculty names and the values are the corresponding sets of programs.
#  Write a Python program to display the programs offered in the "Faculty of Science and Technology."



