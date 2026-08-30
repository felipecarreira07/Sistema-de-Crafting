import math

def calcular_recipes(recipe, qnt):

    print('-----------------------------------------------------------')
    print(f'Para craftar {qnt} {recipe['nome']} voce vai precisar de: ')
    for ingrediente in recipe['ingredientes']:
        
        print(f"{ingrediente['nome']}: {math.ceil(ingrediente['qnt'] * (qnt / recipe['resultado']))}")
        
    print('-----------------------------------------------------------')
    
    print("O que deseja fazer agora? ")
    print("1 - Verificar disponibilidade de fabricacao")
    print("2 - Sair")
    escolha = int(input(""))
    match escolha:
        case 1:
            verificar_disponibilidade_fabric(recipe, qnt)
        case 2:
            print('Saindo...')
            return
        case _:
            print("Opcao invalida!")
            
    return
        
def escolha_calcular_recipe(lista_itens):
    #interface ---------------------
    print('Escolha o item que deseja calcular: ')
    for i, item in enumerate(lista_itens):
            print(f'{i + 1} - {recipes[item]['nome']}')
            
    #logica --------------------------
    while True:
        escolha = int(input(""))
        if(escolha > 0 and escolha <= len(lista_itens)):
            break
        else:
            print("Selecione uma opcao valida!")
    
    while True:  
        qnt_craft = int(input(f"Quantos {recipes[lista_itens[escolha - 1]]['nome']} voce deseja craftar? "))
        
        if(qnt_craft > 0):
            break
        else:
            print('Selecione um numero mais que 0!')
    
    
    calcular_recipes(recipes[lista_itens[escolha - 1]], qnt_craft)
    return        
    
def verificar_disponibilidade_fabric(recipe, qnt):
    
    pode_fazer = True
    
    for ingrediente in recipe['ingredientes']:
        #Informa se da pra craftar baseado na quantidade presente no inventario
        nome_ingrediente = ingrediente['nome']
        num_calculado = math.ceil(ingrediente['qnt'] * (qnt / recipe['resultado'])) 
        
        if inventario[nome_ingrediente]['qnt'] >= ingrediente['qnt']:
            
            status = f'Disponivel (Restarao {inventario[nome_ingrediente]['qnt'] - num_calculado})'
            
        else:
            
            status = f'Em falta (faltam {num_calculado - inventario[nome_ingrediente]['qnt']})'
            pode_fazer = False
        
        print(f'{inventario[nome_ingrediente]['nome']}: {status}')
    
    while True:
        if pode_fazer:
            print("Pode fazer!") #Depois vira uma funcao pra realmente craftar
            break
        else:
            print("Nao pode fazer!")
            break
        
    return


inventario = {
    #Minerios Brutos -----------
    "minerio_de_ferro":{
        "nome": "Minerio de Ferro",
        "qnt": 0
    },
    "minerio_de_cobre":{
        "nome": "Minerio de Cobre",
        "qnt": 0
    },
    #Placas ----------------
    "placa_de_ferro": {
        "nome": "Placa de Ferro",
        "qnt": 1400
    },
    #Cabos ------------------
    "fio_de_cobre": {
        "nome": "Fio de Cobre",
        "qnt": 14452
    },
    #Itens importantes
    "circuito_basico": {
        "nome": "Circuito Basico",
        "qnt": 0
    },
}

recipes = {
    #Placas -----------------
    "placa_de_ferro": {
        "nome": "Placa de Metal",
        "ingredientes": [
            {
                "nome": "minerio_de_ferro",
                "qnt": 2    
            }
        ],
        "resultado": 1
    },
    
    #Cabos -----------------
    "fio_de_cobre": {
        "nome": "Fio de Cobre",
        "ingredientes": [
            {
                "nome": "minerio_de_cobre",
                "qnt": 1    
            }
        ],
        "resultado": 2
    },
    #Itens Complexos -------
    "circuito_basico": {
        "nome": "Circuito Basico",
        "ingredientes": [
            {
                "nome": "placa_de_ferro",
                "qnt": 2    
            },
            {
                "nome": "fio_de_cobre",
                "qnt": 3    
            },
        ],
        "resultado": 1
    },
}

opcoes_itens = ["placa_de_ferro", "fio_de_cobre", "circuito_basico"]

while True:
    #Interface -------------------
    print("Digite a acao desejada: ")
    print("1 - Calcular recipe")
    print("2 - Sair")
    escolha = int(input(""))
    #Verificacao da escolha ------
    match escolha:
        case 1:
            escolha_calcular_recipe(opcoes_itens)
        case 2:
            print('Saindo...')
            break
        case _:
            print("Opcao invalida!")
