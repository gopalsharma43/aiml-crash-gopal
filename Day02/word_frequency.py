# This program counts how many times each word appears in a sentence.

def word_frequency(sentence):

    words = sentence.lower().split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

    return frequency


sentence = "Python is great and Python is easy and Python is powerful"

result = word_frequency(sentence)

sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)

print("Word Frequency:\n")

for word, count in sorted_result:
    print(f"{word} : {count}")