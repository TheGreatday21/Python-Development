def count_characters(s):
    # Initialize an empty dictionary to store the count of each character
    char_count = {}

    # Iterate through each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, initialize its count to 1
        else:
            char_count[char] = 1

    return char_count

# Test the function
input_string = input("Write a name ")
result = count_characters(input_string)
print("Occurrences of each character in '{}' are:\n{}".format(input_string, result))
