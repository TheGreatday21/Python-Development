### frequency##calculates how many times a word is repeated in a sentence

sentence = input("Enter a sentence")

word_freq = {}

for word in sentence.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


print(word_freq)



