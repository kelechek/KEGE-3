from timeit import timeit
import re

def Maya1(data):
    phones = []
    for i in range(len(data.split())):
        if data[i] == '+7':
            phone = data[i] + ' ' + data[i + 1] + ' ' + data[i + 2]
            phones.append(phone)


def Maya2(data):
    phones = []
    for line in data.split('  '):
        if '+7' in line:
            phones.append(line)


def Tim(data):
    phones = []
    for i in range(len(data)):
        if data[i] == "+":
            phones.append(data[i:i + 18])

def regex(data):
    pattern = r'\+7 \(...\) ...-..-..'
    re.findall(pattern, data)

with open('UserData.txt', encoding='utf-8') as file:
    text = file.read()

time1 = timeit('Maya1(text)', globals=globals(), number=10)
time2 = timeit('Maya2(text)', globals=globals(), number=10)
time3 = timeit('Tim(text)', globals=globals(), number=10)
time4 = timeit('regex(text)', globals=globals(), number=10)

print(time1)
print(time2)
print(time3)
print(time4)