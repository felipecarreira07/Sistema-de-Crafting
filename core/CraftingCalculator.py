import math

class CraftingCalculator:
    def __init__(self, recipes_db):
        self.recipes_db = recipes_db
        
    def agrupador_recipes(self, _recipe):

        _recipe_final = []
        
        for _item in _recipe:
            if len(_recipe_final) > 0:
                
                for _recipe_atual in _recipe_final:
                    if _item["nome"] == _recipe_atual["nome"]:
                        _recipe_atual["qnt"] += _item["qnt"]
                        break
                else:
                    _recipe_final.append(_item)
                    
            else:
                _recipe_final.append(_item)

        return _recipe_final
    
    #Falta verificacao de entrada da recipe e quantidade
    def calcular_recipe(self, _recipe, _qnt):
        _result = []
        for _ingrediente in _recipe['ingredientes']:
            _temp = {
                "nome": _ingrediente["nome"],
                "qnt": math.ceil(((_qnt * _ingrediente["qnt"]) / _recipe["resultado"])) # => 41 / 2 -> 20,5 -> 21 arredondado
            }

            _result.append(_temp)     
        
        return _result
    
    def calcular_crafting_tree(self, _recipe_recebida):
        # _recipe_recebida => [{'nome': 'placa_de_ferro', 'qnt': 2}, {'nome': 'fio_de_cobre', 'qnt': 3}]
        
        _array_percorrido = _recipe_recebida

        _array_temporario = _array_percorrido # Array pra ir dando append nele ate acabar o loop, no final o _recipe vai ser igual a ele.
        
        _array_final = []
        
        while True:
        
            if not _array_percorrido: 
                break
            else: 
                for i, _ingrediente_atual in enumerate(_array_percorrido):
                    if _ingrediente_atual['nome'] in self.recipes_db:
                        _array_temporario.extend(self.calcular_recipe(self.recipes_db[_ingrediente_atual['nome']], _ingrediente_atual['qnt']))
                        _array_final.append(_array_temporario.pop(i))
                        pass
                    else:
                        _array_final.append(_array_temporario.pop(i))
                
                _array_percorrido = _array_temporario
                
        return _array_final
    
    def verificar_disponibilidade_recipe(self, _itens_necessarios):
        
        #Funcao antiga pra identificar disponibilidade de crafting =>
        
        #Recebe o array do calcular_crafting_tree
    #  def verificar_disponibilidade_fabric(self, recipe, qnt):
            
    #         pode_fazer = True
            
    #         for ingrediente in recipe['ingredientes']:
    #             #Informa se da pra craftar baseado na quantidade presente no INVENTARIO
    #             nome_ingrediente = ingrediente['nome']
    #             num_calculado = math.ceil(ingrediente['qnt'] * (qnt / recipe['resultado'])) 
                
    #             if self.INVENTARIO[nome_ingrediente]['qnt'] >= ingrediente['qnt']:
                    
    #                 status = f'Disponivel (Restarao {self.INVENTARIO[nome_ingrediente]['qnt'] - num_calculado})'
                    
    #             else:
                    
    #                 status = f'Em falta (faltam {num_calculado - self.INVENTARIO[nome_ingrediente]['qnt']})'
    #                 pode_fazer = False
                
    #             print(f'{self.INVENTARIO[nome_ingrediente]['nome']}: {status}')
            
    #         while True:
    #             if pode_fazer:
    #                 print("Pode fazer!") #Depois vira uma funcao pra realmente craftar
    #                 break
    #             else:
    #                 print("Nao pode fazer!")
    #                 break
                
    #         return
    
        pass