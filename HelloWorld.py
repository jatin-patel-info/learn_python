
import dataclasses

data = [
		{'L1': 1, 'L3': 3, 'R2': 20, 'R3': 30, 'T1': 5, 'T2': 4, 'T3': 8}, 
		{'L1': 4, 'L2': 9, 'R1': 54, 'R2': 19, 'T1': 63, 'T2': 42}
	]

# print(data[0].values().__len__())

def process(e): 
    n = int(e.values().__len__()/3+1)
    result = tuple()
    for i in range(1,n+1):
        # print(e['L'+ i.__str__()])
        L = e['L'+ i.__str__()] if 'L'+ i.__str__() in e  else 0
        R = e['R'+ i.__str__()] if 'R'+ i.__str__() in e  else 0
        T = e['T'+ i.__str__()] if 'T'+ i.__str__() in e  else 0
        sum = int(L+R-T)
        # result.__add__(sum)
        y = list(result)
        # print(y)
        y.append(sum)
        # print(y)
        result = tuple(y)

    print(result)

process(data[0])
