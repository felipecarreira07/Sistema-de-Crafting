import math

from core.ConsoleUi import *

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

INVENTARIO = {
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

menu = ConsoleUi(RECIPES, INVENTARIO)

menu.menu_inicial()