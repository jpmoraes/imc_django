# home/utils.py

def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return 1  # Abaixo do peso
    elif 18.5 <= imc < 24.9:
        return 2  # Peso normal
    elif 25.0 <= imc < 29.9:
        return 3  # Sobrepeso
    elif 30.0 <= imc < 34.9:
        return 4  # Obesidade grau I
    elif 35.0 <= imc < 39.9:
        return 5  # Obesidade grau II
    else:
        return 6  # Obesidade grau III ou mórbida

