from tkinter import Tk, Label, Button
class jogo:
    def __init__(self, jogador1='Jogador 1', jogador2='Jogador 2'):
        self.marca = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.vez_jogador1 = True
        self.sinbolo_jogador1 = 'X'
        self.sinbolo_jogador2 = 'w'
        self.nome_jogador1 = jogador1
        self.nome_jogador2 = jogador2
        self.mensagem_momento_jogo = f'A vez do {self.nome_jogador1 if self.vez_jogador1 else self.nome_jogador2} jogar'.upper()
        self.qdt_jogadas = 0
        self.vitoria = False

        # Configuração da self.janela

        self.janela = Tk()
        self.janela.title("Jogo da Velha")
        self.janela.rowconfigure(5)
        self.janela.columnconfigure(3)
        self.janela.resizable(False, False)

        self.janela.update_idletasks()
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        x = (largura_tela // 2) - (480 // 2)
        y = (altura_tela // 2) - (900 // 2)
        self.janela.geometry(f'480x680+{x}+{y}')

        self.distacia_x = 10
        self.distacia_y = 11

        self.informacao = Label(self.janela, text=self.mensagem_momento_jogo, font=('Arial', 23), bg='white', width=20, height=3)
        self.informacao.grid(row=1, column=1, columnspan=3, sticky='wesn', pady=(10, 20))
        # ------------------------------------------------------------------------------------------------------------------
        self.butao11 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa11)
        self.butao11.grid(row=2, column=1, padx=self.distacia_x, pady=self.distacia_y)

        self.butao12 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa12)
        self.butao12.grid(row=2, column=2, padx=self.distacia_x, pady=self.distacia_y)

        self.butao13 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa13)
        self.butao13.grid(row=2, column=3, padx=self.distacia_x, pady=self.distacia_y)

        self.butao21 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa21)
        self.butao21.grid(row=3, column=1, padx=self.distacia_x, pady=self.distacia_y)

        self.butao22 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa22)
        self.butao22.grid(row=3, column=2, padx=self.distacia_x, pady=self.distacia_y)

        self.butao23 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa23)
        self.butao23.grid(row=3, column=3, padx=self.distacia_x, pady=self.distacia_y)

        self.butao31 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa31)
        self.butao31.grid(row=4, column=1, padx=self.distacia_x, pady=self.distacia_y)

        self.butao32 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa32)
        self.butao32.grid(row=4, column=2, padx=self.distacia_x, pady=self.distacia_y)

        self.butao33 = Button(self.janela, text='', bg='blue', font=('Arial', 15), width=10, height=5, command=self.casa33)
        self.butao33.grid(row=4, column=3, padx=self.distacia_x, pady=self.distacia_y)

        # ----------------------------------

        reiniciar = Button(self.janela, text='REINICIAR', bg='#006400', font=('Arial', 20), command=self.reiniciar_jogo)
        reiniciar.grid(row=5, column=1, pady=(20, 0))

        fechar = Button(self.janela, text='FECHAR', bg='#FF0000', font=('Arial', 20), command=self.janela.quit)
        fechar.grid(row=5, column=3, sticky='wesn', pady=(20, 0))

    def jogar(self, linha, coluna):
        linha = linha - 1
        coluna = coluna - 1
        self.qdt_jogadas += 1
        if self.vez_jogador1:
            self.marca[linha][coluna] = self.sinbolo_jogador1
            self.vitoria =  self.verificar_vitoria()
            self.mensagem_momento_jogo = f'A vez do {self.nome_jogador2} jogar'
            self.momento_jogo()
            self.vez_jogador1 = False
        else:
            self.marca[linha][coluna] = self.sinbolo_jogador2
            self.vitoria = self.verificar_vitoria()
            self.mensagem_momento_jogo = f'A vez do {self.nome_jogador1} jogar'
            self.momento_jogo()
            self.vez_jogador1 = True








    def momento_jogo(self):
        if self.vitoria:
            self.mensagem_momento_jogo = f'O {self.nome_jogador1 if self.vez_jogador1 else self.nome_jogador2} Venceu!!'
        elif self.qdt_jogadas >= 9 :
            self.mensagem_momento_jogo = 'O JOGO EMPATADO'




        self.informacao.config(text=self.mensagem_momento_jogo.upper())
    def verificar_vitoria(self):
        jogador = self.sinbolo_jogador1 if self.vez_jogador1 else self.sinbolo_jogador2


        horizotal = 0
        vertical = 0
        diagonal_direita = 0
        diagonal_esquerda = 0
        for id_linha, linha in enumerate(self.marca):
            for id_coluna, simbolo in enumerate(linha):
                if simbolo == jogador: # ganhou na horizotal
                    horizotal +=1
                    if horizotal == 3:
                        return  True

                if self.marca[id_coluna][id_linha] == jogador: # ganhou na vertical
                    vertical +=1
                    if vertical == 3:
                        return  True

            if self.marca[id_linha][id_linha] == jogador: # ganhou na diagonal esquerda
                diagonal_esquerda +=1
                if diagonal_esquerda == 3:
                    return True


            if self.marca[(id_linha+1)*(-1)][id_linha] == jogador:# ganhou na diagonal direita
                diagonal_direita += 1
                if diagonal_direita == 3:
                    return True

            horizotal = vertical  = 0





        return False


    def casa11(self):

        if self.vitoria:
            return

        jogador = 'X'if self.vez_jogador1 else'O'
        self.butao11.destroy()
        rotulo = Label(self.janela,  text=jogador, bg='#48D1CC', font=('Arial', 86), width=2, height=1)
        rotulo.grid(row=2, column=1, padx=(self.distacia_x, self.distacia_x), pady=self.distacia_y)

        self.jogar(1,1)

    def casa12(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao12.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=2, column=2, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(1, 2)





    def casa13(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao13.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=2, column=3, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(1, 3)


    def casa21(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao21.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=3, column=1, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(2, 1)


    def casa22(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao22.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=3, column=2, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(2, 2)
    def casa23(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao23.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=3, column=3, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(2, 3)


    def casa31(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao31.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=4, column=1, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(3, 1)
    def casa32(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao32.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=4, column=2, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(3, 2)
    def casa33(self):
        if self.vitoria:
            return
        jogador = 'X' if self.vez_jogador1 else 'O'
        self.butao33.destroy()
        rotulo = Label(self.janela, text=jogador, bg='#48D1CC', font=('Arial', 83), width=2, height=1)
        rotulo.grid(row=4, column=3, padx=self.distacia_x, pady=self.distacia_y)
        self.jogar(3, 3)


    def reiniciar_jogo(self):
        import os
        import sys
        python = sys.executable
        os.execl(python, python, *sys.argv)



    def execute(self):
        self.janela.mainloop()







