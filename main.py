import math

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


def calcular_recipes(recipe, qnt):

    print('-----------------------------------------------------------')
    print(f'Para craftar {qnt} {recipe['nome']} voce vai precisar de: ')
    for ingrediente in recipe['ingredientes']:
        print(f"{ingrediente['nome']}: {math.ceil(ingrediente['qnt'] * (qnt / recipe['resultado']))}")
        
    print('-----------------------------------------------------------')
    return

teste = 'motor_eletrico'
calcular_recipes(recipes[teste], 10)