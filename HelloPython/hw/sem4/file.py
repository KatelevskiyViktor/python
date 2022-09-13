# ex1:
# d = 0.001
# p = 3.1415926535
# dTemp = str(d).split('.')
# print(round(p, len(dTemp[1])))
# or
# print(str(round(p, len(dTemp[1])+1))[:-1])


# ex2:
# def primfacs(n):
#    i = 2
#    primfac = []
#    while i * i <= n:
#        while n % i == 0:
#            primfac.append(i)
#            n = n / i
#        i = i + 1
#    if n > 1:
#        primfac.append(round(n))
#    return primfac
# 
# print(primfacs(20))


# ex3:
# from operator import index
# 
# myList = [1, 1, 2, 3, 4, 5, 5]
# resList = []
# mark = 0
# for i in myList:
#     for y in range(myList.index(i)+1, len(myList)):
#         if myList[y] == i:
#             mark = 1
#             break        
#     if mark == 1:
#         mark = 0
#         continue
#     resList.append(i)
# 
# print(resList)


# ex4, ex5:
from random import randint
import itertools
import re
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)


with open('33_Polynomial.txt', 'w') as data:
    data.write(polynom1)

k = randint(2, 5)

ratios = get_ratios(k) 
polynom2 = get_polynomial(k, ratios)


with open('33_Polynomial2.txt', 'w') as data:
    data.write(polynom2)


file1 = '33_Polynomial.txt'
file2 = '33_Polynomial2.txt'
file_sum = '34_Sum_polynomials.txt'


def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol


def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res


def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print("Первый многочлен: " + pol1)
print("Второй многочлен: " + pol2)
print("Сумма многоленов: " + pol_sum)