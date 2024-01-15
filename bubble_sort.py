nlist = input('Proszę podać ciąg liczb naturalnych \n')
nlist1 = list(map(int, nlist.split()))

def bubbleSort(nlist1):
    for num in range(len(nlist1)-1,0,-1):
        for i in range(num):
            if nlist1[i]>nlist1[i+1]:
                x = nlist1[i]
                nlist1[i] = nlist1[i+1]
                nlist1[i+1] = x

bubbleSort(nlist1)
print(nlist1)
