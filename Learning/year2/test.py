##Closures - Functions that remember where they are from 
def my_fun(name):
    def my_fun_2(okay):
        return f"Hey there {name} i hope you have a good {okay}"
    return my_fun_2
my_fun


stu_1 = my_fun("Elijah")
stu_2 = my_fun("James")

print(my_fun("time"))
print(my_fun("day"))


