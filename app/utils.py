import json
import os

caminho_arquivo = "confirmados.json"

def ler_presenca():
    if not os.path.exists(caminho_arquivo):
        return []
    
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
        
        