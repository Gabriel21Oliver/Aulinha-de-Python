import tkinter as tk
from tkinter import messagebox



def exibir_resposta(resposta):
    if resposta.lower() == "sim":
        messagebox.showinfo("Resposta", "Opaaaaa! 💖\nEspero que seja o início de algo maravilhoso!")
    else:
        messagebox.showinfo("Resposta", "Oh, entendi. Se precisar de tempo para pensar, tudo bem. 😊")

def mudar_posicao(event):
    novo_x = event.x + 30  # Ajuste para evitar que o botão fique sob o ponteiro do mouse
    novo_y = event.y - 20  # Ajuste para posicionar o botão um pouco acima do ponteiro do mouse
    botao_nao.place(x=novo_x, y=novo_y)

# Criar a janela principal
janela = tk.Tk()
janela.title("Pedido de Namoro")

# Criar um rótulo na janela
rotulo = tk.Label(janela, text="Oi! Eu tenho uma pergunta para você...\nVocê gostaria de namorar comigo?")
rotulo.pack(pady=100)

# Criar botões "Sim" e "Não" na janela
botao_sim = tk.Button(janela, text="Sim", command=lambda: exibir_resposta("sim"))
botao_sim.pack(side=tk.LEFT, padx=10)

botao_nao = tk.Button(janela, text="Não", command=lambda: exibir_resposta("não"))
botao_nao.pack(side=tk.LEFT, padx=10)

# Associar a função mudar_posicao ao evento Enter (passagem do mouse sobre) do botão "Não"
botao_nao.bind("<Enter>", mudar_posicao)

# Executar o loop principal da janela
janela.mainloop()
