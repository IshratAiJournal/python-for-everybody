import re

with open('regex_sum_2257064.txt') as f:
    text = f.read()

numbers = re.findall(r'[0-9]+', text)
total = sum(int(num) for num in numbers)

print('sum of numbers:', total)

Output:
sum of numbers: 361603
