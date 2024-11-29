# Zoom da pagina em 90%
import pyautogui
import os
from time import sleep

caminho = "C:\\Users\\mf056\\OneDrive\\Área de Trabalho\\Projeto-De-Tecnologia-Aplicada-II-main\\Teste de tela para a bomba incorreta"

Botão = "BotaoVazio.png"
Voltar = "Voltar.png"
Biblioteca = "Biblioteca.png"
Voltar2 = "Volta2.png"
PausarInfusao = "PausarInfusao.png"
Avancar = "Avancar.png"
NovaFuncao = "NovaFuncao.png"


if not os.path.exists(os.path.join(caminho, Botão)):
    raise FileNotFoundError(f"O arquivo de imagem {Botão} não foi encontrado no diretório {caminho}.")
os.chdir(caminho)

n = 10
k = 0

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(Botão)
        if local is not None:  
            pyautogui.moveTo(Botão, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {Botão} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


while k < n:
    try:
        local1 = pyautogui.locateCenterOnScreen(Voltar)
        if local1 is not None:  
            pyautogui.moveTo(local1, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {Voltar} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local2 = pyautogui.locateCenterOnScreen(Biblioteca)
        if local2 is not None:  
            pyautogui.moveTo(local2, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {Biblioteca} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


while k < n:
    try:
        local3 = pyautogui.locateCenterOnScreen(Voltar2)
        if local3 is not None:  
            pyautogui.moveTo(local3, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {Voltar2} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


while k < n:
    try:
        local4 = pyautogui.locateCenterOnScreen(PausarInfusao)
        if local4 is not None:  
            pyautogui.moveTo(local4, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {PausarInfusao} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local5 = pyautogui.locateCenterOnScreen(Avancar)
        if local5 is not None:  
            pyautogui.moveTo(local5, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {Avancar} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


while k < n:
    try:
        local6 = pyautogui.locateCenterOnScreen(NovaFuncao)
        if local6 is not None:  
            pyautogui.moveTo(local6, duration=0.8)  
            pyautogui.click() 
            sleep(0.8) 
            pyautogui.click()
            sleep(0.8) 
            pyautogui.click()
            sleep(0.8) 
            pyautogui.click()
            sleep(0.8) 
            

            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {NovaFuncao} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


if k == n: 
    print("Teste de tela concluido")