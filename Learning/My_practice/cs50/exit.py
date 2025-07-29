#The exit status in pyton is got  in the sys library 

import sys 

if len(sys.argv) != 2:
    print("Missing command line argument.")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)#exiting the program with exit status 0

