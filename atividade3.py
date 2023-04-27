# A
num_a = 1

print("Exercício A: ")
while num_a < 8:
    print(num_a)
    num_a = num_a + 2

# B
num_b = 2
resultado = 2
cont = 2

print("Exercício B: ")
while num_b < 64:
    print(num_b)
    num_b = num_b + cont
    cont = num_b

# C
print("Exercício C: ")

for i in range(7):
    print(i**2)

# D
print("Exercício D: ")

for i in range(2, 9, 2):
    print(i**2)

# E
print("Exercício E:")

a, b = 1, 1
print(a)
print(b)
for i in range(5):
    c = a + b
    print(c)
    a = b
    b = c

