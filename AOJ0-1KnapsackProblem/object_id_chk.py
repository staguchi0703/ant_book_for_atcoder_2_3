def id_chk(a):
    print('-----------------------------')
    print(a)
    print(id(a))

a = 1

id_chk(a)

print('+++++++++++++++++++++++')

list1 = [[0] * 3] * 3


id_chk(list1)

for j in list1:
    id_chk(j)
    for k in j:
        id_chk(k)

list1[2][2] = 1

for j in list1:
    id_chk(j)
    for k in j:
        id_chk(k)

id_chk(list1)

print('++++++++++++++++++++++++++++++++++++++++')

list2 = [[0 for _ in range(3)] for _ in range(3) ]

id_chk(list2)

for j in list2:
    id_chk(j)
    for k in j:
        id_chk(k)

list2[2][2] = 1

for j in list2:
    id_chk(j)
    for k in j:
        id_chk(k)

id_chk(list2)

print('++++++++++++++++++++++++++++++++++++++++')
import numpy as np

list3 = np.zeros((3, 3), dtype='int')

id_chk(list3)

for j in list3:
    id_chk(j)
    for k in j:
        id_chk(k)

list3[2][2] = 1

for j in list3:
    id_chk(j)
    for k in j:
        id_chk(k)

id_chk(list3)