# LISTA
notas = []

# LOOP
for i in range(4):
    entrada_notas = float(input(f"Digite aqui {i + 1} notas:"))
    notas.append(entrada_notas)

# CALCULANDO A MÉDIA
med = sum(notas)
media = med / 4

# RESULTADO
print(f"A média das 4 notas é {media:.2f}")