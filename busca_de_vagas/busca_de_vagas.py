from playwright.sync_api import sync_playwright
import pywhatkit as kit
import schedule
import time
import os



def rastreio_de_vagas():
    vagas = []
    with sync_playwright() as p:
        navegador = p.chromium.launch_persistent_context(
            headless=False,
            user_data_dir=f"{os.getcwd()}/user_data_dir"
            )
        page1 = navegador.pages[0]
        page1.goto("https://www.linkedin.com/jobs/search-results/")
        page1.wait_for_timeout(5000)

        if page1.url == "https://www.linkedin.com/home":
            print("Faça seu login e depois volte para o terminal e aperte enter:\n")
            input()

        tag_a = page1.locator("a")
        contagem = tag_a.count()
        print(contagem)
        for i in range(contagem):
            if tag_a.nth(i).inner_text() == "Vagas":
                tag_a.nth(i).click()
                break
            
        page1.wait_for_timeout(5000)
        span = page1.locator("span")
        contagem = span.count()
        for i in range(contagem):
            if span.nth(i).inner_text() == "Exibir todas":
                span.nth(i).click()
                break

        page1.wait_for_timeout(5000)

        paragrafos = page1.locator("div[role=button]")
        contagem = paragrafos.count()
        for i in range(8,contagem -4):
            paragrafos.nth(i).click()
            page1.wait_for_timeout(3000)
            link = page1.url
            vaga = f"{paragrafos.nth(i).inner_text()}\n{link}\n"
            vagas.append(vaga)

                
        page1.wait_for_timeout(60000)

    texto = f'''
        Olá, temos novas vagas:
        {"\n".join(vagas)}
    '''
    kit.sendwhatmsg_instantly("", texto, 30, True)

schedule.every().day.at("12:00").do(rastreio_de_vagas)

while True:
    schedule.run_pending()
    time.sleep(1)