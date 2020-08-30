'''n = int(input())
x = input()
seq = set()
for i in x:
    if i != " ":
        seq.add(int(i))
comp = set()
for i in range(1, n+1):
    comp.add(i)
result = (list(comp-seq))
print(int(result[0]))'''



parts = int(input())
seq = list(map(int, input().split()))
total = (len(seq)*(len(seq)+1))/2
print(total)
