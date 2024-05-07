import pyautogui
import time

#pyautogui.click - Clicar com o mouse.
#pyautogui.write - Escreve o texto requerido.
#pyautogui.press  -Aperta um conjunto de teclas (CTRL V, ALT, Tab). 


pyautogui.PAUSE = 0.5 #Faz uma pausa por 0.5 segundos a CADA comando feito

pyautogui.press('win') # Aperta o botão do Windows
pyautogui.write('chrome') # Abre o navegador Chrome
pyautogui.press('enter') # Entra no Chrome
pyautogui.PAUSE = 0.5 #Faz uma pausa por 0.5 segundos.
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') # Abre o link teste para registrar tarefas
pyautogui.press('enter') # Entra no Site acima

# Após os comandos acima, irá dá uma demorada por causa que vai carregar o site e abrir na aba requerida.

time.sleep(3) # ele vai esperar 3 seg, para só NESSE TRECHO assim executar o comandos abaixo.

# ETAPA 2: Fazer Login 
pyautogui.click(x=902, y=507) 
pyautogui.write('seuemail@gmail.com')
    
pyautogui.press('tab') # Passa para o campo de senha
pyautogui.write('Senha123#')

pyautogui.press('tab') # Passa para o campo de login
pyautogui.press('enter')

time.sleep(3)

# ETAPA 3: Abrir/Importar a base de dados de produtos para cadastrar
# Para instalar, digite: pip install pandas numpy openpyxl
import pandas as pd # Voce pode usar pd e também pandas, é uma abreviaçao

tabela = pd.read_csv('produtos.csv')

print(tabela)

# ETAPA 4: Cadastrar um produto
# str = String = Texto em programação
for linha in tabela.index: 
    codigo = str(tabela.loc[linha, 'codigo']) # Localizar numero da linha
    # Clicar no campo do codigo do produto
    pyautogui.click(x=882, y=364)
    # Preencher o codigo
    pyautogui.write(codigo)
    # Passar pro proximo campo
    pyautogui.press('tab')

    # Preencher marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    # Preencher tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    # Preencher categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # Preencher preço 
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # Preencher custo 
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    # Preencher obs
    obs = (str(tabela.loc[linha, 'obs']))
    if obs != 'nan':
        pyautogui.write(obs) # só escreve esse condicao se obs for diferente de nAn = nao é um numero

    # Ir para o proximo botao
    pyautogui.press('tab')

    # Apertar o botão 'ENVIAR'
    pyautogui.press('enter')            
    pyautogui.scroll(5000)

# ETAPA 5: Repetir isso tudo até acabar a lista de produto
