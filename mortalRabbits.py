__author__ = 'Ales'

n, k = 100, 19


list = [1, 1]
novi = [1, 0]

for i in range(n+1):
    if i < 2:
        continue

    if i > k:
        born = list[i-2] - novi[i-k-1]
        list.append(list[i-1] - novi[i-k] + born)
        novi.append(born)
    elif i == k:
        born = list[i-2]
        list.append(list[i-1] - 1 + born)
        novi.append(born)
    else:
        list.append(list[i-2] + list[i-1])
        novi.append(list[i-2])


print list
print novi
print list[n-1]

