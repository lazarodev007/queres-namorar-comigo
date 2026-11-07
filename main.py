import tkinter as tk
from tkinter import messagebox
import random

# Criar janela principal
root = tk.Tk()
root.title("NOTIFICAÇÃO")
root.geometry("600x450")
root.configure(bg="#ffc8dd")
root.resizable(False, False)

# Título da aplicação
titulo = tk.Label(
    root,
    text="...",
    bg="#ffc8dd",
    fg="#590d22",
    font=("Montserrat", 19, "bold")
)
titulo.pack(pady=65)

# Pergunta principal
pergunta = tk.Label(
    root,
    text="Aceitas namorar comigo?",
    bg="#ffc8dd",
    fg="#590d22",
    font=("Montserrat", 24, "bold")
)
pergunta.pack(pady=15)

# Função executada quando clicar em SIM
def aceitou():
    messagebox.showinfo(
        "Que felicidade!",
        "Bem vinda ao seu novo mundo!\n\n"
        "Vamos sair para jantar?"
    )

# Função para movimentar o botão NÃO
def mover_botao(event):
    root.update_idletasks()

    largura = root.winfo_width()
    altura = root.winfo_height()

    largura_botao = botao_nao.winfo_width()
    altura_botao = botao_nao.winfo_height()

    # Gerar novas coordenadas aleatórias
    novo_x = random.randint(
        20,
        largura - largura_botao - 20
    )

    novo_y = random.randint(
        210,
        altura - altura_botao - 20
    )

    # Mover o botão
    botao_nao.place(x=novo_x, y=novo_y)

# Criar botão SIM
botao_sim = tk.Button(
    root,
    text="SIM",
    bg="#ffb3c1",
    fg="#590d22",
    font=("Montserrat", 14, "bold"),
    relief="ridge",
    bd=3,
    width=10,
    cursor="hand2",
    command=aceitou
)
botao_sim.place(x=190, y=310)

# Criar botão NÃO
botao_nao = tk.Button(
    root,
    text="NÃO",
    bg="#ffb3c1",
    fg="#590d22",
    font=("Montserrat", 14, "bold"),
    relief="ridge",
    bd=3,
    width=10,
    cursor="hand2"
)
botao_nao.place(x=350, y=310)

# Detetar quando o cursor se aproxima do NÃO
botao_nao.bind("<Enter>", mover_botao)

# Iniciar aplicação
root.mainloop()