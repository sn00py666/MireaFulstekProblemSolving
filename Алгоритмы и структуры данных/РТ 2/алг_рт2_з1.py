from sys import stdin


def nod_del_thee(*args):
    args = list(args)
    while 0 in args:
        args[args.index(0)] = max(args)
    args = list(map(lambda x: abs(x), args))
    nums = sorted(args)
    vrem_nod = nums[-1]
    for i in range(len(nums)-1, -1, -1):
        ost1 = nod_del_two(max(nums[i], vrem_nod), min(nums[i], vrem_nod))
        vrem_nod = ost1
    return vrem_nod


def nod_del_two(num1, num2):
    ost = num2
    while num1 % num2 != 0:
        ost = num1 % num2
        num1 = num2
        num2 = ost
    return ost


def nod_subt_four(*args):
    args = list(args)
    while 0 in args:
        args[args.index(0)] = max(args)
    args = list(map(lambda x: abs(x), args))
    nums = sorted(args)
    
    vrem_nod = nums[-1]
    for i in range(len(nums)-1, -1, -1):
        ost1 = nod_subt_two(max(nums[i], vrem_nod), min(nums[i], vrem_nod))
        vrem_nod = ost1
    return vrem_nod
    

def nod_subt_two(num1,num2):
    ost = num2
    while num1 != num2:
        ost = num1 - num2 
        num1 = max(num2, ost)
        num2 = min(num2, ost)
    return num1


lines = []
for line in stdin:
    lines.append(int(line))
    
if lines == [0, 0, 0, 0] or lines == [0, 0, 0]: print("NOD не существует")
else:
    if len(lines) == 3:
        print("NOD методом деления: " + str(nod_del_thee(*lines)))
    elif len(lines) == 4:
        print("NOD методом вычетания: " + str(nod_subt_four(*lines)))

# Наборы для тестов
# print(nod_del_thee(30, 60, 15))
# print(nod_del_thee(3, 7, 11))
# print(nod_del_thee(6, 8, 14))
# print(nod_subt_four(30, 60, 15, 120))
# print(nod_subt_four(3, 7, 11, 13))
# print(nod_subt_four(6, 8, 14, 22))

