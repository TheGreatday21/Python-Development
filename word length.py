def count (word):
    num = word.split()
    kee = len(num)
    print(f"Your statement has {kee} words")
user = input("Write a word :\t")
count(user)
