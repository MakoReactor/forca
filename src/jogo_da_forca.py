#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import random

# Versão
version = "0.7"

#
# Douglas Barbosa dos Santos <douglas.santosb@gmail.com>
# License: MIT License
#
# Todo: Resolver bug onde as palvras com espaço mostram "{}" no lugar do espaço
#       Resolver bug quando jogodador perde ou vence perguntar se o mesmo quer
#       parar ou se quer um novo jogo.
#       Criar funcionálidade para dificuldade (fácil, médio, difícil)
#       
#

class Forca(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # inicializa variáveis
        self.palavra = None
        self.letras_digitadas = None
        self.palavra_secreta = None
        self.contador = None    

        # inicializa widgets do jogo
        self.create_widgets()
        # re-inicializa variáveis do jogo
        self.inicio_jogo()

    def inicio_jogo(self):
        self.letras_digitadas = []
        self.palavra_secreta = []
        self.contador = 10
        self.label_contador['text'] = self.contador
        self.letras_digitadas_mostra['text'] = ""
        self.palavra_secreta_label['text'] = ""    
                
        self.sorteia_palavra()
        
    def set_letras_digitadas(self, letras):
        chute = False
        
        for i in range(0, len(self.palavra)):
            for letra in letras:
                if letra == self.palavra[i]:
                    self.palavra_secreta[i] = letra
                    chute = True

                if letra not in self.letras_digitadas:
                    self.letras_digitadas.append(letra)
                    self.letras_digitadas_mostra['text'] = self.letras_digitadas

        if chute == False:
            self.contador-=1            
            self.label_contador['text']=self.contador

        if self.contador <= 0:
            messagebox.showinfo("Alert", "\nVOCÊ PERDEU!!!!!!!!!!            \n")
            messagebox.showinfo("Info", "A palavra secreta era:\n{0}".format(self.palavra))

        # Atualiza na tela as letras encontradas na palavra secreta        
        self.palavra_secreta_label['text'] = self.palavra_secreta

        if "_" not in self.palavra_secreta:
            messagebox.showinfo("Congrats","Parabéns você acertou a palavra secreta\n{}".format(self.palavra))


    def sorteia_palavra(self):
        """ Usa um arquivo de texto puro de onde sorteia as palavras
            quanto mais palavras nesse arquivo melhor
            neste caso esta sendo usando o arquivo 'palavras_forca.txt'
            que deve estar no mesmo diretório. 

        """           
        x = open('palavras_forca.txt', 'r')
        lista_de_palavras=x.readlines()
        x.close()
        palavra = random.choice(lista_de_palavras).split('\n')[0].upper()
        self.palavra= palavra

        # palavra de teste, retire o "#"  e altere o valor da variável
        # para testar as letras com acento e o Ç ou outros 
        # comportamentos de algumas palavras
        #self.palavra = "HOMEM ARANHA" 
        
        # Normaliza a palavra em coso de a mesma conter hífem ou espaço 'veja bug do espaço em Todo'
        for i in range(0, len(self.palavra)):
            if self.palavra[i] == "-":
                self.palavra_secreta.append("-")
            elif self.palavra[i] == " ":
                self.palavra_secreta.append(" ")
            else:
                self.palavra_secreta.append("_")


        # Atualiza o palavra secreta na tela
        self.palavra_secreta_label['text'] = self.palavra_secreta


    def create_widgets(self):
        #Frame teclado letras
        self.frame1 = Frame(self, relief = SUNKEN, borderwidth=8)
        self.frame1.grid(row=5)

        self.letraA = Button(self.frame1, font=("Helvetica", 12), text="A", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("AÁÂÃ"))
        self.letraA.grid(row=0, column=0, sticky="NWNESWSE")

        self.letraB = Button(self.frame1, font=("Helvetica", 12), text="B", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("B"))
        self.letraB.grid(row=0, column=1, sticky="NWNESWSE")

        self.letraC = Button(self.frame1, font=("Helvetica", 12), text="C", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("CÇ"))
        self.letraC.grid(row=0, column=2, sticky="NWNESWSE")

        self.letraD = Button(self.frame1, font=("Helvetica", 12), text="D", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("D"))
        self.letraD.grid(row=0, column=3, sticky="NWNESWSE")

        self.letraE = Button(self.frame1, font=("Helvetica", 12), text="E", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("EÉÊ"))
        self.letraE.grid(row=0, column=4, sticky="NWNESWSE")

        self.letraF = Button(self.frame1, font=("Helvetica", 12), text="F", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("F"))
        self.letraF.grid(row=0, column=5, sticky="NWNESWSE")

        self.letraG = Button(self.frame1, font=("Helvetica", 12), text="G", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("G"))
        self.letraG.grid(row=0, column=6, sticky="NWNESWSE")

        #linha 1
        self.letraH = Button(self.frame1, font=("Helvetica", 12), text="H", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("H"))
        self.letraH.grid(row=1, column=0, sticky="NWNESWSE")

        self.letraI = Button(self.frame1, font=("Helvetica", 12), text="I", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("IÍ"))
        self.letraI.grid(row=1, column=1, sticky="NWNESWSE")

        self.letraJ = Button(self.frame1, font=("Helvetica", 12), text="J", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("J"))
        self.letraJ.grid(row=1, column=2, sticky="NWNESWSE")

        self.letraK = Button(self.frame1, font=("Helvetica", 12), text="K", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("K"))
        self.letraK.grid(row=1, column=3, sticky="NWNESWSE")

        self.letraL = Button(self.frame1, font=("Helvetica", 12), text="L", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("L"))
        self.letraL.grid(row=1, column=4, sticky="NWNESWSE")

        self.letraM = Button(self.frame1, font=("Helvetica", 12), text="M", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("M"))
        self.letraM.grid(row=1, column=5, sticky="NWNESWSE")

        self.letraN = Button(self.frame1, font=("Helvetica", 12), text="N", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("N"))
        self.letraN.grid(row=1, column=6, sticky="NWNESWSE")

        #linha 2
        self.letraO = Button(self.frame1, font=("Helvetica", 12), text="O", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("OÓÔ"))
        self.letraO.grid(row=2, column=0, sticky="NWNESWSE")

        self.letraP = Button(self.frame1, font=("Helvetica", 12), text="P", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("P"))
        self.letraP.grid(row=2, column=1, sticky="NWNESWSE")

        self.letraQ = Button(self.frame1, font=("Helvetica", 12), text="Q", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("Q"))
        self.letraQ.grid(row=2, column=2, sticky="NWNESWSE")

        self.letraR = Button(self.frame1, font=("Helvetica", 12), text="R", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("R"))
        self.letraR.grid(row=2, column=3, sticky="NWNESWSE")

        self.letraS = Button(self.frame1, font=("Helvetica", 12), text="S", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("S"))
        self.letraS.grid(row=2, column=4, sticky="NWNESWSE")

        self.letraT = Button(self.frame1, font=("Helvetica", 12), text="T", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("T"))
        self.letraT.grid(row=2, column=5, sticky="NWNESWSE")

        self.letraU = Button(self.frame1, font=("Helvetica", 12), text="U", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("UÚ"))
        self.letraU.grid(row=2, column=6, sticky="NWNESWSE")

        #linha 3
        self.letraV = Button(self.frame1, font=("Helvetica", 12), text="V", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("V"))
        self.letraV.grid(row=3, column=0, sticky="NWNESWSE")

        self.letraW = Button(self.frame1, font=("Helvetica", 12), text="W", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("W"))
        self.letraW.grid(row=3, column=1, sticky="NWNESWSE")

        self.letraX = Button(self.frame1, font=("Helvetica", 12), text="X", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("X"))
        self.letraX.grid(row=3, column=2, sticky="NWNESWSE")

        self.letraY = Button(self.frame1, font=("Helvetica", 12), text="Y", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("Y"))
        self.letraY.grid(row=3, column=3, sticky="NWNESWSE")

        self.letraZ = Button(self.frame1, font=("Helvetica", 12), text="Z", borderwidth=1,padx=16, pady=16, command=lambda: self.set_letras_digitadas("Z"))
        self.letraZ.grid(row=3, column=4, sticky="NWNESWSE")

        self.reiniciar = Button(self.frame1, font=("Helvetica", 12), text="Reiniciar", borderwidth=1,padx=16, pady=16, command=self.inicio_jogo)
        self.reiniciar.grid(row=3, column=5,columnspan=2, sticky="NWNESWSE")
        # Fim teclado letras

        # Letras digitadas
        self.frame2 = Frame(self, relief = SUNKEN,borderwidth=8)
        self.frame2.grid(row=2,sticky="NWNESWSE")

        self.letras_digitadas_label = Label(self.frame2, text="LETRAS DIGITADAS", font=("Helvetica", 12))
        self.letras_digitadas_label.grid(row=0, columnspan=6)

        self.letras_digitadas_mostra = Label(self.frame2, text="", font=("Helvetica", 12))
        self.letras_digitadas_mostra.grid(row=1)

        # contador de erros
        self.frame3 = Frame(self, relief = SUNKEN,borderwidth=8)
        self.frame3.grid(row=3,sticky="NWNESWSE")

        self.chances_restantes_label = Label(self.frame3, text="CHANCES RESTANTES", font=("Helvetica", 12))
        self.chances_restantes_label.grid(row=0, columnspan=6)

        self.label_contador = Label(self.frame3, font=("Helvetica", 20), text = self.contador,padx=10, pady=10)        
        self.label_contador.grid(row=1, column=0, rowspan=2, columnspan=2)


        #Palavra secreta
        self.frame4 = Frame(self, relief = SUNKEN,borderwidth=8)
        self.frame4.grid(row=4,sticky="NWNESWSE")

        self.palavra_secreta_titulo = Label(self.frame4, font=("Helvetica", 12), text="PALAVRA SECRETA.", padx=10, pady=10)        
        self.palavra_secreta_titulo.grid(row=0, sticky="W")

        self.palavra_secreta_label = Label(self.frame4, font=("Helvetica", 20), text="", padx=10, pady=10)        
        self.palavra_secreta_label.grid(row=1, column=0, sticky="W")



forca = Tk()
forca.title("Palavra Secreta Ver. {}".format(version))
forca.resizable(0, 0)
#forca.geometry("400x300")
app = Forca(forca).grid()
forca.mainloop()
