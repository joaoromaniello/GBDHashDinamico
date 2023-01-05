from hashText import Registro, TabelaHash

# Criar uma instância da tabela hash
tabela_hash = TabelaHash()

##EXEMPLO
tabela_hash.inserir(Registro(1, "Ana"))
tabela_hash.inserir(Registro(2, "Bruno"))
tabela_hash.inserir(Registro(3, "Carlos"))
tabela_hash.inserir(Registro(4, "Daniel"))
tabela_hash.inserir(Registro(5, "Erick"))
tabela_hash.inserir(Registro(6, "Flavia"))
tabela_hash.inserir(Registro(7, "Gabriel"))
tabela_hash.inserir(Registro(8, "Hanna"))


#imprimea a tabela
tabela_hash.imprimir()

registro = tabela_hash.buscar("Bruno")

if registro is not None:
  print("Registro encontrado: {}".format(registro.text))
else:
  print("Registro não encontrado")

# Remover o registro encontrado
tabela_hash.remover("Bruno")

# Realizar a busca do registro novamente
registro = tabela_hash.buscar("Bruno")

if registro is not None:
  print("Registro encontrado: {}".format(registro.text))
else:
  print("Registro não encontrado")