palabra = input("Ingrese una palabra: ")
vocales = ["a", "e", "i", "o", "u"]
contador = [palabra.count(v) for v in vocales]

for i in range(len(vocales)):
    print(f"la vocal {vocales[i]} aparece {contador[i]}")