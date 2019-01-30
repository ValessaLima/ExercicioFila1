class fila():

  def __init__(self):
    self.fila_avioes = []

  def enqueue(self):
    num_aviao= int(input("qual o numero do avião?"))
    self.fila_avioes.append(num_aviao)
    print("avião add na lista de espera")
  
  print ("a quantidade de avioes na lista de espera são",len(self.fila_avioes))
  print("os numeros de avioes são",self.num_avião)
  print("autorisada a largada do primeiro aviao")

  def dequeue(self):
    self.fila_avioes.pop(0)