import math

RECIPES = {
    #Placas -----------------
    "placa_de_ferro": {
        "nome": "Placa de Ferro",
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
    "recipe_louca": {
        "nome": "Recipe Louca",
        "ingredientes": [
            {
                "nome": "circuito_basico",
                "qnt": 1    
            }
        ],
        "resultado": 1
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

# Precisa receber um array que ficou identificou que ficou com todos os crafings necesasrios pra recipe prinpipal (O array do nodulo da Crafting Tree)
#Tipo => [{"nome": "placa_de_ferro","qnt": 2},{"nome": "fio_de_cobre","qnt": 3},{"nome": "minerio_de_ferro","qnt": 4},{"nome": "minerio_de_cobre","qnt": 2},]
#Esse array ja passou pelo cacular_rendimento()
#Nesse caso a recipe nao exige organizacao, mas se tivesse minerio de ferro como requisito pro Circuito_Basico, ele precisaria ser agrupado com o minerio de ferro usado pras placas
def agrupador_recipes(_recipe):

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

#Funcionando perfeitamente pra retornar a quantidade de itens de uma recipe
#Requer verificacao de entrada
def calcular_recipe(_recipe, _qnt):
        
    _result = []
    for _ingrediente in _recipe['ingredientes']:
        
       _temp = {
           "nome": _ingrediente["nome"],
           "qnt": math.ceil(((_qnt * _ingrediente["qnt"]) / _recipe["resultado"])) # => 41 / 2 -> 20,5 -> 21 arredondado
       }

       _result.append(_temp)     
       
    return _result
    
#RECIPE['NOME DA RECIPE']
def calcular_crafting_tree(_recipe_recebida):
    # _recipe_recebida => [{'nome': 'placa_de_ferro', 'qnt': 2}, {'nome': 'fio_de_cobre', 'qnt': 3}]
    
    _array_percorrido = _recipe_recebida['ingredientes']

    _array_temporario = _array_percorrido # Array pra ir dando append nele ate acabar o loop, no final o _recipe vai ser igual a ele.
    
    _array_final = []
    
    while True:
    
        if not _array_percorrido: 
            break
        else: 
            for i, _ingrediente_atual in enumerate(_array_percorrido):
                if _ingrediente_atual['nome'] in RECIPES:
                    _array_temporario.extend(calcular_recipe(RECIPES[_ingrediente_atual['nome']], _ingrediente_atual['qnt']))
                    _array_final.append(_array_temporario.pop(i))
                    pass
                else:
                    _array_final.append(_array_temporario.pop(i))
            
            _array_percorrido = _array_temporario
            
    return _array_final




# print(calcular_recipe(RECIPES['circuito_basico'], 1))
# print(calcular_recipe(RECIPES['placa_de_ferro'], 2))
# print(calcular_recipe(RECIPES['fio_de_cobre'], 3))

resultado = calcular_crafting_tree(RECIPES['recipe_louca'])
print(resultado)

# recipe_calculada = calcular_recipe(recipes["circuito_basico"], 1)
# recipe_crafting_tree = calcular_crafting_tree(recipe_calculada) # => [{'nome': 'placa_de_ferro', 'qnt': 2}, {'nome': 'fio_de_cobre', 'qnt': 3}]
# #Tem que virar => [{"nome": "placa_de_ferro","qnt": 2},{"nome": "fio_de_cobre","qnt": 3},{"nome": "minerio_de_ferro","qnt": 4},{"nome": "minerio_de_cobre","qnt": 2}]


# agrupador_recipes(lista_teste)



#Posso usar o else no For pra parar o loop quando nao tiver mais nenhuma recipe nos ingredientes

