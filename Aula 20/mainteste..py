import sqlite3 # banco de dados
import tkinter as tk # interface 
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb

def conectar():
    return sqlite3.connect('leads.db')


def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        interesse TEXT,
        status TEXT             
        )       
    ''')
    conn.commit()
    conn.close()
  

# CREATE
def inserir_lead():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    interesse = entry_interesse.get()
    status = combo_status.get()

    if nome and email:
        conn = conectar()
        c = conn.cursor()

        c.execute('INSERT INTO leads(nome, email, telefone, interesse, status) VALUES(?,?,?,?,?)', (nome, email, telefone, interesse, status))

        conn.commit()
        conn.close()

        messagebox.showinfo('Sucesso', 'LEAD CADASTRADO!') 
        mostrar_leads()
    else:
        messagebox.showerror('ERRO', 'Preencha nome e e-mail!') 

# READ
def mostrar_leads():
    for row in tree.get_children():   
        tree.delete(row)

    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM leads')
    dados = c.fetchall()

    for lead in dados:
        tree.insert("", "end", values=lead)

    conn.close()


# DELETE
def delete_lead():
    selecao = tree.selection()

    if selecao:
       lead_id = tree.item(selecao)['values'][0]

       conn = conectar()
       c = conn.cursor()    

       c.execute('DELETE FROM leads WHERE id = ? ',(lead_id,))
       conn.commit()
       conn.close()

       messagebox.showinfo('Sucesso', 'LEAD DELETADO')
       mostrar_leads()

    else:
       messagebox.showerror('Aviso', 'Selecione um lead')  

# UPDATE   
def editar_lead():
     selecao = tree.selection()

     if selecao:
         lead_id = tree.item(selecao)['values'][0]
         
         novo_nome = entry_nome.get()
         novo_email = entry_email.get()
         novo_telefone = entry_telefone.get()
         novo_interesse = entry_interesse.get()
         status = combo_status.get()

         if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()  

            c.execute('UPDATE leads SET nome = ? , email = ? , telefone = ?, interesse = ?, status = ? WHERE id = ? ',(novo_nome,novo_email,novo_telefone,novo_interesse,status, lead_id))

            conn.commit()
            conn.close()  

            messagebox.showinfo('Sucesso', 'LEAD ATUALIZADOS')
            mostrar_leads()

         else:
             messagebox.showwarning('ERROO', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('ERRO','ALGO DEU ERRADO!')

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_interesse.delete(0, tk.END)
    combo_status.set("Em andamento")


def selecionar_lead(event):
    selecao = tree.selection()

    if selecao:
        dados = tree.item(selecao)['values']

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, dados[1])

        entry_email.delete(0, tk.END)
        entry_email.insert(0, dados[2])

        entry_telefone.delete(0, tk.END)
        entry_telefone.insert(0, dados[3])

        entry_interesse.delete(0, tk.END)
        entry_interesse.insert(0, dados[4])

        combo_status.set(dados[5])


# INTERFACE
janela = tk.Tk()
janela.title('Gestão de Leads')

tk.Label(janela, text='Nome:').grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text='Email:').grid(row=1, column=0)
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1)

tk.Label(janela, text='Telefone:').grid(row=2, column=0)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=1)

tk.Label(janela, text='Interesse:').grid(row=3, column=0)
entry_interesse = tk.Entry(janela)
entry_interesse.grid(row=3, column=1)

tk.Label(janela, text='Status:').grid(row=4, column=0)
combo_status = ttk.Combobox(janela, values=["Em andamento", "Convertido", "Perdido"])
combo_status.grid(row=4, column=1)
combo_status.set("Em andamento")

tk.Button(janela, text='Cadastrar', command=inserir_lead).grid(row=5, column=0)
tk.Button(janela, text='Atualizar', command=editar_lead).grid(row=5, column=1)
tk.Button(janela, text='Excluir', command=delete_lead).grid(row=6, column=0)
tk.Button(janela, text='Limpar', command=limpar_campos).grid(row=6, column=1)

# TABELA
colunas = ('ID', 'Nome', 'Email', 'Telefone', 'Interesse', 'Status')
tree = ttk.Treeview(janela, columns=colunas, show='headings')

for col in colunas:
    tree.heading(col, text=col)

tree.grid(row=7, column=0, columnspan=2)

tree.bind("<ButtonRelease-1>", selecionar_lead)

criar_tabela()
mostrar_leads()

janela.mainloop()