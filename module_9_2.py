first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >  5]
second_result = [(string_1, string_2) for string_1 in first_strings
                 for string_2 in second_strings if len(string_1) == len(string_2)]
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)