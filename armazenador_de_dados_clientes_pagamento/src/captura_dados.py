import pdfplumber as p
import os,re
import pandas as pd



def armazenador_de_dados_de_notas_fiscais():
    # verificar qual sistema operacional esta usando
    caminho = ''
    if os.name == "posix":
        #para linux verifico o caminho para a pasta de downloads
        caminho = f"{os.getenv('HOME')}/Downloads"
    elif os.name == "nt":
        #para windows verifico o caminho para a pasta de downloads
        caminho = f"{os.getenv('USERPROFILE')}/Downloads"
    
    lista_de_pdf = os.listdir(caminho)
    
    
    regex_cnpj = r"(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})"
    regex_emitente = r"Razão Social / Emitente: (.*?)\n"
    regex_data = r"Data do Documento: (\d{2}/\d{2}/\d{4})"
    regex_status_pagamento = r"Status do Pagamento: (.*)"
    regex_descricao = r"Descrição dos Serviços: (.*?)\n"
    regex_valor = r"Valor Total: R\$ ([\d\.]+,\d{2})"
    
    
    dados = {
        'cnpj':[],
        'emitente':[],
        'data':[],
        'status_pagamento':[],
        'descricao':[],
        'valor':[]
    }
    
    for pdf in lista_de_pdf:
        if pdf.endswith(".pdf"):
            with p.open(f"{caminho}/{pdf}") as pdf_file:
                for page in pdf_file.pages:
                    text = page.extract_text()
    
                    if text:
                        match_cnpj = re.search(regex_cnpj, text)
                        match_emitente = re.search(regex_emitente, text)
                        match_data = re.search(regex_data, text)
                        match_status = re.search(regex_status_pagamento, text)
                        match_desc = re.search(regex_descricao, text)
                        match_valor = re.search(regex_valor, text)
    
                        dados['cnpj'].append(match_cnpj.group(1) if match_cnpj else None)
                        dados['emitente'].append(match_emitente.group(1) if match_emitente else None)
                        dados['data'].append(match_data.group(1) if match_data else None)
                        dados['status_pagamento'].append(match_status.group(1) if match_status else None)
                        dados['descricao'].append(match_desc.group(1) if match_desc else None)
                        dados['valor'].append(match_valor.group(1) if match_valor else None)
    
    
    df = pd.DataFrame(dados)
    
    if os.path.exists(f"{caminho}/dados.csv"):
        df.to_csv(f"{caminho}/dados.csv", mode='a', header=False, index=False)
    else:
        df.to_csv(f"{caminho}/dados.csv", index=False)
    
    
    
    
    