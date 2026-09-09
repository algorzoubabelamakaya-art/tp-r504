import fonctions as f
print("Hello, World!")

# question 2.1
while True:
    nombre = int(input("Entrez un nombre : "))
    print(nombre ** 2)

#2.3
a = int(input("Premier nombre : "))
b = int(input("Deuxième nombre : "))
res = f.puissance(a, b)
print(res)
