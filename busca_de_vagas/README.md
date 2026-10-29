# Busca de Vagas no LinkedIn via WhatsApp

Um script de automação que monitora o LinkedIn em busca de novas vagas e envia os resultados direto no WhatsApp, de hora em hora, sem precisar abrir o navegador manualmente toda vez.

---

## O que ele faz

O script abre o LinkedIn usando uma sessão persistente do navegador (ou seja, se você já tiver logado antes, ele lembra do login), navega até a aba de vagas, clica em "Exibir todas" pra expandir a listagem e percorre cada uma das vagas disponíveis. Para cada vaga encontrada, ele captura o título e o link direto, e no final manda tudo num texto via WhatsApp usando o `pywhatkit`.

Esse ciclo se repete automaticamente a cada hora enquanto o script estiver rodando.

---

## Tecnologias usadas

- **[Playwright](https://playwright.dev/python/)** — controla o navegador de forma programática, clicando, navegando e lendo o conteúdo das páginas
- **[PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit)** — envia mensagens pelo WhatsApp Web automaticamente
- **[schedule](https://schedule.readthedocs.io/)** — agenda a execução do rastreamento de hora em hora
- **Python 3.14+**

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/luannsantosprogrammer/RPA.git
cd RPA/busca_de_vagas
```

### 2. Instale as dependências

O projeto usa `uv` para gerenciar pacotes. Se ainda não tiver o `uv` instalado:

```bash
pip install uv
```

Depois instale as dependências do projeto:

```bash
uv sync
```

Ou, se preferir usar um ambiente virtual tradicional:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install playwright pywhatkit schedule
```

### 3. Instale o navegador do Playwright

```bash
uv playwright install chromium
```

### 4. Configure o número de destino

Antes de rodar, abra o arquivo `busca_de_vagas.py` e coloque o número de telefone no qual as vagas serão enviadas. Localize essa linha:

```python
kit.sendwhatmsg_instantly("", texto)
```

E substitua a string vazia pelo número no formato internacional, por exemplo:

```python
kit.sendwhatmsg_instantly("+5511999999999", texto)
```

### 5. Execute o script

```bash
python busca_de_vagas.py
```

Quando o navegador abrir, **faça seu login no LinkedIn** normalmente. Depois volte ao terminal e pressione **Enter**. A partir daí, o script cuida do resto e passa a rodar o rastreamento a cada hora.

> **Obs:** O login fica salvo na pasta `user_data_dir/` criada automaticamente no diretório do projeto. Nas próximas execuções você não precisará logar de novo.

---

## Estrutura do projeto

```
busca_de_vagas/
├── busca_de_vagas.py   # Script principal
├── user_data_dir/      # Sessão persistente do navegador (gerada automaticamente)
├── pyproject.toml      # Configuração do projeto e dependências
├── uv.lock             # Lock file das dependências
└── README.md
```

---

## Pontos importantes

- O script roda com o navegador **visível** (`headless=False`) justamente para permitir o login manual na primeira vez e para o WhatsApp Web funcionar corretamente.
- A pasta `user_data_dir/` guarda os cookies e dados de sessão. Não delete ela se não quiser precisar logar novamente.
- O `pywhatkit` precisa que o WhatsApp Web esteja acessível no navegador. Se der algum problema no envio, verifique se a sessão do WhatsApp ainda está ativa.

---

## Autor

**Luann Santos** — [luannrodrigodesouzasantos@gmail.com](mailto:luannrodrigodesouzasantos@gmail.com)
