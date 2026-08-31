import math
from core.CraftingCalculator import CraftingCalculator

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

calculadora = CraftingCalculator(RECIPES)


calc_recipe = calculadora.calcular_recipe(RECIPES['circuito_basico'], 10)
resultado = calculadora.calcular_crafting_tree(calc_recipe)
print(resultado)

