class Registro:
  def __init__(self, nseq, text):
    self.nseq = nseq
    self.text = text

class TabelaHash:
  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.tabela = [[] for _ in range(self.tamanho)]
    self.tamanho_maximo = 5

  def funcao_hash(self, nseq):
    return nseq % self.tamanho

  def buscar(self, nseq):
    posicao = self.funcao_hash(nseq)
    for registro in self.tabela[posicao]:
      if registro.nseq == nseq:
        return registro
    return None

  def inserir(self, registro):
    posicao = self.funcao_hash(registro.nseq)
    if len(self.tabela[posicao]) >= self.tamanho_maximo:
      self.aumentar_tamanho()
    self.tabela[posicao].append(registro)

  def remover(self, nseq):
    posicao = self.funcao_hash(nseq)
    for i, registro in enumerate(self.tabela[posicao]):
      if registro.nseq == nseq:
        self.tabela[posicao].pop(i)
        return True
    return False

  def aumentar_tamanho(self):
    tamanho_antigo = self.tamanho
    self.tamanho *= 2
    tabela_antiga = self.tabela
    self.tabela = [[] for _ in range(self.tamanho)]
    for entrada in tabela_antiga:
      for registro in entrada:
        self.inserir(registro)