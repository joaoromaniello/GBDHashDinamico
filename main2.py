from hashNSeq2 import TabelaHash, Registro

def imprimir_tabela_hash(tabela_hash):
  for i, entrada in enumerate(tabela_hash.tabela):
    print(f"Indice {i}: {[registro.nseq for registro in entrada]}")

tabela_hash = TabelaHash(10)

# Inserir alguns registros na tabela hash
for i in range(0, 8):
  tabela_hash.inserir(Registro(i, f"Registro {i}"))

# Imprimir a tabela hash antes do aumento de tamanho
print("Tabela hash antes do aumento de tamanho:")
imprimir_tabela_hash(tabela_hash)

#Para simular um overflow na tabela, basta adicionar mais que 5 (tamanho maximo definido na propria classe) em
# uma posição da tabela

for i in range(0,5):
    tabela_hash.inserir(Registro(i*10, f"Registro {i}"))

# Imprimir a tabela hash depois do aumento de tamanho
print("\nTabela hash depois do aumento de tamanho:")
imprimir_tabela_hash(tabela_hash)


tabela_hash.remover(20)
tabela_hash.remover(10)
tabela_hash.remover(30)

print("")
print("Tabela após remoção dos nós 20 e 60")
imprimir_tabela_hash(tabela_hash)