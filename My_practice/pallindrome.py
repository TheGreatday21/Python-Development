user1 = input("Write a palyndrome here")
user2 = user1[::-1]
if user1 == user2:
    print(f"{user1} is a pallindrome")
else:
    print(f"{user1} is not a pallindrome")