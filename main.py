import math

def calcular_recipes(recipe, qnt):

    print('-----------------------------------------------------------')
    print(f'Para craftar {qnt} {recipe['nome']} voce vai precisar de: ')
    for ingrediente in recipe['ingredientes']:
        print(f"{ingrediente['nome']}: {math.ceil(ingrediente['qnt'] * (qnt / recipe['resultado']))}")
        
    print('-----------------------------------------------------------')
    return
        
def escolha_calcular_recipe(lista_itens):
    #interface ---------------------
    print('Escolha o item que deseja calcular: ')
    for i, item in enumerate(lista_itens):
            print(f'{i + 1} - {recipes[item]['nome']}')
            
    escolha = int(input(""))
    qnt_craft = int(input(f"Quantos {recipes[lista_itens[escolha - 1]]['nome']} voce deseja craftar? "))
    #logica --------------------------

    calcular_recipes(recipes[lista_itens[escolha - 1]], qnt_craft)
    return        
    
opcoes_itens = ["placa_de_metal", "placa_de_cobre", "fio_de_cobre", "motor_eletrico"]
recipes = {
        "placa_de_metal": {
            "nome": "Placa de Metal",
            "ingredientes": [
                {
                    "nome": "minerio_de_ferro",
                    "qnt": 2    
                }
            ],
            "resultado": 1
        },
        "placa_de_cobre": {
            "nome": "Placa de Cobre",
            "ingredientes": [
                {
                    "nome": "minerio_de_cobre",
                    "qnt": 2    
                }
            ],
            "resultado": 1
        },
        "fio_de_cobre": {
            "nome": "Fio de Cobre",
            "ingredientes": [
                {
                    "nome": "placa_de_cobre",
                    "qnt": 1    
                }
            ],
            "resultado": 2
        },
        "motor_eletrico": {
            "nome": "Motor Eletrico",
            "ingredientes": [
                {
                    "nome": "placa_de_ferro",
                    "qnt": 4    
                },
                {
                    "nome": "fio_de_cobre",
                    "qnt": 4    
                },
            ],
            "resultado": 3
        },
        
    }

while True:
    #Interface -------------------
    print("Digite a acao desejada: ")
    print("1 - Calcular recipe")
    escolha = int(input(" "))
    #Verificacao da escolha ------
    match escolha:
        case 1:
            escolha_calcular_recipe(opcoes_itens)
            break

teste = 'motor_eletrico'
calcular_recipes(recipes[teste], 10)