import pyautogui as gui
from time import sleep
from notifypy import Notify
import os


caminho = os.getcwd()



def verificando_imagem(img):
    #função para verificar se a imagem existe e clicar nela
    imagem_verificada = gui.locateCenterOnScreen(
        f"{caminho}/{img}",
        confidence=0.8
    )
    gui.click(img)



notification = Notify()
notification.title = "Mensagem automação"


def dowload_notas_fiscais():

    sleep(5)
    
    condicao_varredura = "varrendo"


    while condicao_varredura == "varrendo":
        try:
            # clicando na barra de pesquisa do email e digitando "is:unread" para pesquisar emails não lidos
            verificando_imagem("img/pesquisar_email.png")

            gui.write("is:unread")
            gui.press("enter")
            sleep(8)
            
            #clicando no email com o título "Notal Fiscal Eletrônica"
            verificando_imagem("img/imagem_clicar.png")
            sleep(5)

            #rolando a tela para baixo para encontrar a barra do pdf
            gui.scroll(-250)
            imagem_pdf = gui.locateCenterOnScreen(
            f"{caminho}/img/barra_pdf.png",
            confidence=0.8
        )

            #movendo o mouse para a barra do pdf
            gui.moveTo(imagem_pdf.x,imagem_pdf.y,duration=1)
            sleep(2)

            #clicando no botão de download
            verificando_imagem("img/botao_download.png")
            sleep(2)

            #retornando para a tela inicial do google
            verificando_imagem("img/imagem_inicial.png")
            sleep(4)
        except:
            #mudando a variável para finalizar o loop
            condicao_varredura = "finalizado"
            notification.message = "Finalizada varredura"
            notification.send()
            print("Finalizada varredura")