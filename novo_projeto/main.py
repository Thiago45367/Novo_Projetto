import os
from novo_projeto.models.pessoa import Pessoa
from novo_projeto.models.enums.sexo import Sexo

os.system("cls || clear")

# Instanciando classe.
pessoa = Pessoa("Marta", 22, Sexo.FEMININO)

print(pessoa)