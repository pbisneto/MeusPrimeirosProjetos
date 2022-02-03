import random


acpf = random.randint(100000000, 999999999)
acpf = str(acpf)
x = 10
j = 11
k = 0
c = 0
for n in acpf:
    a = int(n)
    b = a * x
    c = c + b
    x -= 1
d1 = 11 - (c % 11)
if d1 > 9:
    d1 = 0

xcpf = str(acpf) + str(d1)

for n2 in xcpf:         # x=j c=k a=l b=m
    l = int(n2)
    m = l * j
    k = k + m
    j -= 1
d2 = 11 - (k % 11)
if d2 > 9:
    d2 = 0

cpf_c = xcpf + str(d2)
print(cpf_c)