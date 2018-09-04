# coding: utf-8

n = input()

s = input()

k = v = 0
k_win = v_win = 0

for i in s:
    if i == 'K':
        k += 1
    elif i == 'V':
        v += 1
    if k >= 11 and (k - v) == 2:
        print(1)
        k_win += 1
        k = v = 0
    if v >= 11 and (v - k) == 2:

        print(2)
        v_win += 1
        k = v = 0
    print(4)
print('{}:{}'.format(k_win, v_win))
print("Коля: {}\nВася:{}".format(s.count('K'), s.count("V")))
if v != 0 or k != 0:
    print('{}:{}'.format(k, v))
