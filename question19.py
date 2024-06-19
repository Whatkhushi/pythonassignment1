import string
input_string = "Hello, world! This is a test string."
no_punctuation_string = ''.join(char for char in input_string if char not in string.punctuation)
print(no_punctuation_string)
