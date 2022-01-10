import PySimpleGUI as sg

class Calculadora:
  def __init__(self):
    self.digitando = True
    self.numeros1 = "0"
    self.numeros2 = "0"
    self.opera = ""
    
  def Iniciar(self):
    
    #Layout
    self.layout = [
      [sg.Text('Calculadora UMP-2000', justification='right', font=("Helvetica", 25))],
      
      # Onde mostram os numeros que serão calculados
      [sg.Output(size=(26,2), key ='_output_', font=("Helvetica", 25))],
      [sg.Button('7', size=(5, 2),font=("Helvetica", 25)),sg.Button('8', size=(5, 2),font=("Helvetica", 25)),sg.Button('9', size=(5, 2),font=("Helvetica", 25)),sg.Button('/', size=(5, 2),font=("Helvetica", 25))],# 7,8,9,/
      [sg.Button('4', size=(5, 2),font=("Helvetica", 25)),sg.Button('5', size=(5, 2),font=("Helvetica", 25)),sg.Button('6', size=(5, 2),font=("Helvetica", 25)),sg.Button('x', size=(5, 2),font=("Helvetica", 25))],# 4,5,6,x
      [sg.Button('1', size=(5, 2),font=("Helvetica", 25)),sg.Button('2', size=(5, 2),font=("Helvetica", 25)),sg.Button('3', size=(5, 2),font=("Helvetica", 25)),sg.Button('-', size=(5, 2),font=("Helvetica", 25))],# 1,2,3,-
      [sg.Button('0', size=(5, 2),font=("Helvetica", 25)),sg.Button('=', size=(5, 2),font=("Helvetica", 25)),sg.Button('C', size=(5, 2),font=("Helvetica", 25)),sg.Button('+', size=(5, 2),font=("Helvetica", 25))]# 0,=,+,C
    ]
    
    # Criando a janela da Calculadora
    self.janela = sg.Window('Calculadora',layout=self.layout)
    
    while True:
      
      # Recebendo valores:
      self.eventos, self.valores = self.janela.Read() 
      while self.digitando == True:

        if self.eventos == '+':         #Se depois de ter digitado o numero, a operação escolhida for soma
          print(self.eventos)           #A Calculadora printa o simbolo de soma
          self.opera=self.eventos       #Aloca o sinal de soma na variavel de escolher a operação
          self.numeros2=self.numeros1   #Passa o valor da primeira variavel para a segunda
          self.numeros1="0"             #Zera a primeira variavel para receber o próximo numero
          break
        
        elif self.eventos == '-':
          print(self.eventos)
          self.opera=self.eventos
          self.numeros2=self.numeros1   
          self.numeros1="0" 
          break
        
        elif self.eventos == '/':
          print(self.eventos)
          self.opera=self.eventos
          self.numeros2=self.numeros1
          self.numeros1="0" 
          break
        
        elif self.eventos == 'x':
          print(self.eventos)
          self.opera='*'
          self.numeros2=self.numeros1
          self.numeros1="0" 
          break
        
        elif self.eventos == 'C':
          self.numeros1="0"
          self.numeros2="0"
          #sg.Window.FindElement('_output_').Update('')
          print(" ")
          break
        
        elif self.eventos == '=':
          print(self.eventos)
          if self.opera=='+':
            self.ressoma()
            break
          elif self.opera=='-':
            self.ressub()
            break
          elif self.opera=='/':
            self.resdiv()
            break
          elif self.opera=='*':
            self.resmul()
            break
          break
        
        else:
          if self.numeros1=="0":
            self.numeros1=str(self.eventos)
            print(self.numeros1)
            break
          else:
            self.numeros1=self.numeros1+self.eventos
            print(self.numeros1)
            break
  
  def ressoma(self):
    self.numeros2=int(self.numeros2)+int(self.numeros1)
    print(self.numeros2)
    self.numeros1="0"
    self.numeros2="0"
  
  def ressub(self):
    self.numeros2=int(self.numeros2)-int(self.numeros1)
    print(self.numeros2)
    self.numeros1="0"
    self.numeros2="0"

  def resdiv(self):
    self.numeros2=float(self.numeros2)/float(self.numeros1)
    print(self.numeros2)
    self.numeros1="0"
    self.numeros2="0"
  
  def resmul(self):
    self.numeros2=int(self.numeros2)*int(self.numeros1)
    print(self.numeros2)
    self.numeros1="0"
    self.numeros2="0"

Calc = Calculadora()
Calc.Iniciar()
