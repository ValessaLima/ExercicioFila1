class fila():

  def __init__(self):
    self.fila_avioes = []

  def enqueue(self):
    num_aviao= int(input("qual o numero do avi�o?"))
    self.fila_avioes.append(num_aviao)
    print("avi�o add na lista de espera")
  
  print ("a quantidade de avioes na lista de espera s�o",len(self.fila_avioes))
  print("os numeros de avioes s�o",self.num_avi�o)
  print("autorisada a largada do primeiro aviao")

  def dequeue(self):
    self.fila_avioes.pop(0)