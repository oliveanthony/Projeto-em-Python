import os
import shutil

nome_arquivo = "Import.py"

caminho_origem = ("C:/Users/Anthony/Documents/Import.py")
caminho_destino = ("C:/Users/Anthony/Documents/Destino Python")
print("Origem:", caminho_origem)
print("Destino:", caminho_destino)
print("Arquivo existe?", os.path.exists(caminho_origem))

try:
    shutil.move(caminho_origem,caminho_destino)
    print("Arquivo movido com sucesso!")
except FileNotFoundError:
    print("Failed")