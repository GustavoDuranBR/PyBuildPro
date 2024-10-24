import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import os
from PIL import Image, ImageTk  # Importando Image e ImageTk do Pillow

def selecionar_diretorio():
    dir_path = filedialog.askdirectory()
    entry_diretorio.delete(0, tk.END)
    entry_diretorio.insert(0, dir_path)

def selecionar_ico():
    ico_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    entry_ico.delete(0, tk.END)
    entry_ico.insert(0, ico_path)

def selecionar_py():
    py_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    entry_py.delete(0, tk.END)
    entry_py.insert(0, py_path)

def selecionar_script_inno():
    inno_path = filedialog.askopenfilename(filetypes=[("Inno Setup Script", "*.iss")])
    entry_inno.delete(0, tk.END)
    entry_inno.insert(0, inno_path)

def iniciar_build():
    dir_programa = entry_diretorio.get()
    arquivo_ico = entry_ico.get()
    arquivo_py = entry_py.get()
    arquivo_inno = entry_inno.get()

    # Formata o nome dos arquivos para serem usados nos comandos
    nome_ico = os.path.basename(arquivo_ico)
    nome_py = os.path.basename(arquivo_py)

    # Verifica se já existe um .exe na pasta dist e exclui se existir
    dist_path = os.path.join(dir_programa, 'dist', nome_py.replace('.py', '.exe'))
    if os.path.exists(dist_path):
        os.remove(dist_path)
    
    # Comando específico que será executado
    comando_exe = f"pyinstaller --onefile --windowed --icon=\"{nome_ico}\" \"{nome_py}\""
    
    # Navega até o diretório e executa o comando no CMD
    terminal_cmd = f'cd /d "{dir_programa}" && {comando_exe}'
    
    # Executa o comando e espera pela conclusão
    subprocess.run(terminal_cmd, shell=True)

    # Inicia o Inno Setup
    iniciar_inno_setup()

def iniciar_inno_setup():
    arquivo_inno = entry_inno.get()
    
    # Comando para executar o Inno Setup
    terminal_cmd_inno = f'"C:\\Program Files (x86)\\Inno Setup 6\\ISCC.exe" "{arquivo_inno}"'
    
    # Executa o comando do Inno Setup e espera pela conclusão
    subprocess.run(terminal_cmd_inno, shell=True)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de .exe e Instalador")
root.geometry("650x320")

# Definindo o ícone da janela
root.iconbitmap(r"D:\PYTHON_PROJETOS\BuildAutomator\icon.ico")

# Carregando a imagem com Pillow
imagem_titulo = Image.open(r"D:\PYTHON_PROJETOS\BuildAutomator\image.png")
imagem_titulo = imagem_titulo.resize((50, 50), Image.LANCZOS)  # Ajusta o tamanho da imagem
imagem_titulo = ImageTk.PhotoImage(imagem_titulo)

label_imagem = ttk.Label(root, image=imagem_titulo)
label_imagem.grid(row=0, column=0, padx=5, pady=5)

# Título com texto
titulo = ttk.Label(root, text="PyBuildPro", font=('Segoe UI', 16, 'bold'), foreground="white", background="#2e2e2e")
titulo.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Estilo do ttk
style = ttk.Style()
style.theme_use('clam')  # Usando o tema 'clam' para um visual mais moderno
style.configure('TButton', font=('Segoe UI', 10), padding=6, background="#0078d7", foreground="white")
style.map('TButton', background=[('active', '#0056a6')], foreground=[('active', 'white')])
style.configure('TEntry', font=('Segoe UI', 10), padding=6, fieldbackground="#1e1e1e", foreground="white")
style.configure('TLabel', background="#2e2e2e", foreground="white")

# Criando os widgets
ttk.Label(root, text="Diretório do Programa:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_diretorio = ttk.Entry(root, width=50)
entry_diretorio.grid(row=1, column=1, padx=5, pady=5)
ttk.Button(root, text="Selecionar", command=selecionar_diretorio).grid(row=1, column=2, padx=5, pady=5)

ttk.Label(root, text="Arquivo .ico:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
entry_ico = ttk.Entry(root, width=50)
entry_ico.grid(row=2, column=1, padx=5, pady=5)
ttk.Button(root, text="Selecionar", command=selecionar_ico).grid(row=2, column=2, padx=5, pady=5)

ttk.Label(root, text="Arquivo .py:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
entry_py = ttk.Entry(root, width=50)
entry_py.grid(row=3, column=1, padx=5, pady=5)
ttk.Button(root, text="Selecionar", command=selecionar_py).grid(row=3, column=2, padx=5, pady=5)

ttk.Label(root, text="Script Inno Setup (.iss):").grid(row=4, column=0, padx=5, pady=5, sticky='w')
entry_inno = ttk.Entry(root, width=50)
entry_inno.grid(row=4, column=1, padx=5, pady=5)
ttk.Button(root, text="Selecionar", command=selecionar_script_inno).grid(row=4, column=2, padx=5, pady=5)

ttk.Button(root, text="Gerar Build", command=iniciar_build).grid(row=5, columnspan=3, pady=10)

# Mudando a cor de fundo da janela principal
root.configure(bg="#2e2e2e")

root.mainloop()
