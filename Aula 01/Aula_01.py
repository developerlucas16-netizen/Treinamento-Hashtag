# Automação sobre cadastrar produtos de fomra automatica, apartir de uma base de dados
# blibioecas = pacotes de código

import pyautogui 
import time

# pyautogui.click -> clica
# pyautogui.write -> escreve
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)

pyautogui.PAUSE = 1 # -> Pausa entre cada linha de codigo

sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "lucaspython@gmail.com"
senha = "lucas123"
# passo a passo do seu programa
# passo 1: Entrar no sistema da empresa
# abrir o navegador

pyautogui.press('win') # win -> tecla windowns
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(6)
pyautogui.write(sistema)
pyautogui.press('enter')
# Tempo para o site carregar
time.sleep(6)

# passo 2: Fazer login
# clicar no ponto de email
pyautogui.click(x=800, y=449)
pyautogui.write(email)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('enter')
time.sleep(6)

# passo 3: Abrir a base de dados
# importar arquivos
import pandas

tabela = pandas.read_csv("5.0Aula 01/produtos.csv")

for linha in tabela.index: 
# passo 4: Cadastrar um produto
    # código
    time.sleep(3)
    pyautogui.click(x=676, y=318) # clicar no campo do código
    codigo = str(tabela.loc[linha, 'codigo']) # tabelas de python sempre colocar conchetes
    pyautogui.write(codigo)
    pyautogui.press('tab') # passar para próximo tópico
    # marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    # tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    # categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    # preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    # custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    # observação
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab') # passar pro botao enviar

    pyautogui.press('enter')

    # voltar para o inicio da tela
    pyautogui.scroll(5000)

# passo 5: Repetir o passo 4 até acabar a lista de produtos




