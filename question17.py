def to_title_case(input_string):
    title_cased_string = input_string.title()
    return title_cased_string

input_string = "hello world, this is a test string."
title_cased = to_title_case(input_string)
print(title_cased)