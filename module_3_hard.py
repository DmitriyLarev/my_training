data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    summ = 0
    if isinstance(data, list):
        for i in data:
            summ += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for i in data:
            summ += len(i) + data[i]
    elif isinstance(data, tuple):
        for i in data:
            summ += calculate_structure_sum(i)
    elif isinstance(data, set):
        for i in data:
            summ += calculate_structure_sum(i)
    elif isinstance(data, int):
        summ += data
    elif isinstance(data, str):
        summ += len(data)
    return summ

result = calculate_structure_sum(data_structure)
print(result)
