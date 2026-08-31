from core.CraftingCalculator import CraftingCalculator

import os

class ConsoleUi:
    def __init__(self, _recipes_db, _inventario_db):
        self.RECIPES = _recipes_db
        self.INVENTARIO = _inventario_db
        
        self.calculadora = CraftingCalculator(self.RECIPES)
        
        pass
    
    def menu_inicial(self):
        
        while True:
            #Interface -------------------

            print('''Digite a acao desejada: 
1 - Calcular recipe
2 - Sair''')
            
            escolha = int(input(""))
            #Verificacao da escolha ------
            match escolha:
                case 1:
                    self.menu_calcular_recipe()
                case 2:
                    print('Saindo...')
                    return
                case _:
                    print("Opcao invalida!")

    def menu_calcular_recipe(self):
        _lista_itens = [
                    "placa_de_ferro", 
                    "fio_de_cobre", 
                    "circuito_basico"
                    ]
           
        #interface ---------------------
        print('Escolha o item que deseja calcular: ')
        for i, item in enumerate(_lista_itens):
                print(f'{i + 1} - {self.RECIPES[item]['nome']}')

        while True:
            escolha = int(input(""))
            if(escolha > 0 and escolha <= len(_lista_itens)):
                break
            else:
                print("Selecione uma opcao valida!")
        
        print(f"Quantos {self.RECIPES[_lista_itens[escolha - 1]]['nome']} voce deseja craftar? ")
        while True:  
            
            qnt_craft = int(input())
            if(qnt_craft > 0):
                break
            else:
                print('Selecione um numero maior que 0!')
        
        _resultado = self.calculadora.calcular_crafting_tree(self.calculadora.calcular_recipe(self.RECIPES[_lista_itens[escolha - 1]], qnt_craft))  
        
        print(f'Para craftar {qnt_craft} {self.RECIPES[_lista_itens[escolha - 1]]['nome']} voce vai precisar de: ')
        for _item in _resultado:
            print(f'{_item["nome"]}: {_item["qnt"]}') # => Falta mostrar a disponibilidade do crafting
        
        print("1 - Sair | 2 - Craftar")
        _final = int(input(""))
        match _final:
            case 1:
                pass
            case 2:
                #funcao de craft
                pass
            case _:
                print("Digite uma funcao valida")
        return
                
   