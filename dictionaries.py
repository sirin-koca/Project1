"""
A dictionary in Python is a collection of key-value pairs, where each key is associated with a value.
Dictionaries are also known as associative arrays, maps, or hash tables in other programming languages.

Dictionaries are commonly used in Python for tasks such as counting the frequency of words in a text,
storing configuration data, and organizing information in a more flexible way than lists or arrays.
"""

# Example1
city_population = {
    "New York": 8336697,
    "London": 8908081,
    "Paris": 2142430
}

print(city_population["New York"])
# Output: 8336697

# Example2
text = "This is a sample text for counting the frequency of words in a text using a dictionary in Python"

# Split the text into words
words = text.split()
print(words)

# Initialize an empty dictionary to store the word frequencies
word_frequency = {}

# Iterate over the words
for word in words:
    # If the word is already in the dictionary, increment its frequency
    if word in word_frequency:
        word_frequency[word] += 1
    # Otherwise, add the word to the dictionary with a frequency of 1
    else:
        word_frequency[word] = 1

# Print the word frequencies
print(word_frequency)

exit()
