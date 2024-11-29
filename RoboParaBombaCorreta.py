# Zoom da pagina em 90%


import pyautogui
import os
from time import sleep

caminho = "C:\\Users\\mf056\\OneDrive\\Área de Trabalho\\Projeto-De-Tecnologia-Aplicada-II-main\\Teste de Tela para a bomba correta"
botao = "Botao.png"
botao2 = "Botao2.png"
botao3 = "Botao3.png"
botao4 = "Botao4.png" 
botao5 = "Botao.png"  
MF = "MaisFuncoes.png"
MF2 = "MF.png"
Pausar = "Pausar.png"
Avancar = "Avancar.png"
Alerta = "Alerta.png"
ZerarVolume = "ZerarVolume.png"
BotaoZerarVolume = "BotaoZerarVolume.png"
BotaoSim = "BotaoSim.png"
BotaoDetalhes = "BotaoDetalhes.png"
BotaoProximo = "BotaoProximo.png"
CancelarPausar = "CancelarPausar.png"


if not os.path.exists(os.path.join(caminho, botao)):
    raise FileNotFoundError(f"O arquivo de imagem {botao} não foi encontrado no diretório {caminho}.")
os.chdir(caminho)

n = 10
k = 0

sleep(8)
while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(botao)
        if local is not None:  
            pyautogui.moveTo(botao, duration=0.8)  
            pyautogui.click()  
            print("Botão 1 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {botao} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(botao2)
        if local is not None:  
            pyautogui.moveTo(botao2, duration=0.8)  
            pyautogui.click()  
            print("Botão 2 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {botao2} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


 
while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(MF)
        if local is not None:  
            pyautogui.moveTo(MF, duration=0.8)  
            pyautogui.click()  
            print("MF clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {MF} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(Pausar)
        if local is not None: 
            pyautogui.moveTo(Pausar, duration=0.8)  
            pyautogui.click()  
            print("Pausar clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {Pausar} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(Avancar)
        if local is not None: 
            pyautogui.moveTo(Avancar, duration=0.8)  
            pyautogui.click()  
            print("Avançar clicado.")
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
        local = pyautogui.locateCenterOnScreen(botao3)
        if local is not None:  
            pyautogui.moveTo(botao3, duration=0.8)  
            pyautogui.click()  
            print("Botão 3 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {botao3} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(botao3)
        if local is not None:  
            pyautogui.moveTo(botao3, duration=0.8)  
            pyautogui.click()  
            print("Botão 2 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {botao3} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(Alerta)
        if local is not None:  
            pyautogui.moveTo(local, duration=0.8)  
            pyautogui.click()  
            print("Botão 2 clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {Alerta} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(MF2)
        if local is not None:  
            pyautogui.moveTo(local, duration=0.8)  
            pyautogui.click()  
            print("MF clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {MF2} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(ZerarVolume)
        if local is not None:  
            pyautogui.moveTo(ZerarVolume, duration=0.8)  
            pyautogui.click()  
            print("Zerar volume clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {ZerarVolume} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(BotaoZerarVolume)
        if local is not None:  
            pyautogui.moveTo(BotaoZerarVolume, duration=0.8)  
            pyautogui.click()  
            print("Botão zerar volume clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {BotaoZerarVolume} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(BotaoSim)
        if local is not None:  
            pyautogui.moveTo(BotaoSim, duration=0.8)  
            pyautogui.click()  
            print("Confirmando zerar volume clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {BotaoSim} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(BotaoDetalhes)
        if local is not None:  
            pyautogui.moveTo(BotaoDetalhes, duration=0.8)  
            pyautogui.click() 
            sleep(1) 
            pyautogui.click()  
            sleep(1)
            pyautogui.click()
            sleep(1)
            pyautogui.click()
            print("Detalhes clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {BotaoDetalhes} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)

while k < n:
    try:
        local = pyautogui.locateCenterOnScreen(BotaoProximo)
        if local is not None:  
            pyautogui.moveTo(BotaoProximo, duration=0.8)  
            pyautogui.click()  
            sleep(1)
            pyautogui.click()
            sleep(1)
            pyautogui.click()
            print("Proximo clicado.")
            break 

        k += 1  
        print(f'Tentativa {k}/{n} - Imagem {BotaoProximo} não encontrada, tentando novamente...')
        sleep(0.25)  

    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada na tela.")
        k += 1
        sleep(0.25)


if k == n:
           
    print("Teste de tela finalizado")