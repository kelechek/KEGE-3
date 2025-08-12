# Task 1
# import re
#
# with open('reg_exp_task_1.txt') as file:
#     data = file.readline()
#
# pattern = r'\d+'
# matches = re.findall(pattern, data)
# print(matches)

# Task 2
# import re
#
# with open('reg_exp_task_2.txt') as file:
#     data = file.readline()
#
# pattern = r'-?\d+\.?\d*'
# matches = re.findall(pattern, data)
# print(matches)

# Task 3
# import re
#
# text = input()
# pattern = r'a+b{2,}c+'
# res = re.sub(pattern, 'HELLO', text)
# print(res)

# Task 4
# import re
#
# with open('reg_exp_task_4.txt') as file:
#     text = file.readline()
#
# pattern = r'\w+@\w+\.[a-z]{2,}'
# res = re.findall(pattern, text)
# print(res)

import re
from timeit import timeit


def regexp(data):
    pattern = '(NPO|PNO)+'
    matches = [match.group() for match in re.finditer(pattern, data)]
    # print(len(max(matches, key=len)) / 3)


def iterate(data):
    counts = []
    cnt = 0
    triple_wf = 3
    for i in range(len(data) - 2):
        if triple_wf in [1, 2]:
            triple_wf += 1
            continue
        if triple_wf == 3:
            if data[i:i + 3] in ['NPO', 'PNO']:
                cnt += 1
                triple_wf = 1
            else:
                counts.append(cnt)
                cnt = 0
    # print(max(counts))


def standart(data):
    line = data.replace('NPO', '*').replace('PNO', '*')
    for i in 'NPO':
        line = line.replace(i, ' ')
    line = line.split()
    # print(len(max(line, key=len)))


with open(r'files\2400.txt') as file:
    text = file.readline()

time1 = timeit('regexp(text)', globals=globals(), number=10)
time2 = timeit('iterate(text)', globals=globals(), number=10)
time3 = timeit('standart(text)', globals=globals(), number=10)

print(time1)
print(time2)
print(time3)