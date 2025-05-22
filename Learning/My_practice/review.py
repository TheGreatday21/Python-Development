import time
def count(secs):
    print("les get-it ")

    while secs > 0 :
        print(f"T-minus{secs}")
        secs -= 1
        time.sleep(1)
    print("Horray you did it my nigga")

A = int(input("How many seconds can you plank"))
count(A)






