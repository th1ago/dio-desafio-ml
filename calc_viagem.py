speed = float(input("Velocidade media "))
time = float(input("O tempo gasto da viagem "))
KM_LITRO = 12

if time > 0:
    litros = (speed * time) / KM_LITRO
    print(f"A velocidade 'e de {litros:.3f}")
else:
    print("Erro! O valor deve ser poditivo ")