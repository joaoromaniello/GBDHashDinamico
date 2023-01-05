from hashAlt3Text import TabelaHash


tabela_hash = TabelaHash()
##EXEMPLO
tabela_hash.inserir(1, "Ana")
tabela_hash.inserir(2, "Bruno")
tabela_hash.inserir(3, "Carlos")
tabela_hash.inserir(4, "Daniel")
tabela_hash.inserir(5, "Erick")
tabela_hash.inserir(6, "Flavia")
tabela_hash.inserir(7, "Gabriel")
tabela_hash.inserir(8, "Hanna")

tabela_hash.imprimir()
# Realizar a busca de um registro com base na chave TEXT
rids = tabela_hash.buscar("Bruno")

if rids is not None:
  print("Registros encontrados:", end=" ")
  for rid in rids:
    print(rid, end=" ")
  print()
else:
  print("Registros não encontrados")

