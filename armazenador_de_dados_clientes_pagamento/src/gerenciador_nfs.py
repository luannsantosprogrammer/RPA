from captura_dados import armazenador_de_dados_de_notas_fiscais
from download_nfs import dowload_notas_fiscais

from notifypy import Notify
from time import sleep

notification = Notify()
notification.title = "Mensagem automação"

notification.message = "Iniciado varredura de e-mails"
notification.send()

dowload_notas_fiscais()

notification.message = "Finalizada varredura de e-mails"
notification.send()

sleep(5)

notification.message = "Iniciado captura de dados"
notification.send()

armazenador_de_dados_de_notas_fiscais()

notification.message = "Finalizada captura de dados"
notification.send()