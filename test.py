fila = []

for i in range(30):
    while True:
        try:
            valor = float(input(f"Digite o valor {i+1}: "))
            fila.append(valor)
            break
        except ValueError:
            print("Por favor, digite um número válido.")

soma = sum(fila)
suavizacao = soma / 30

print("Valores:", fila)
print("Suavização (média):", suavizacao)