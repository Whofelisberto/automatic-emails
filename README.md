# Automatic Emails

Projeto em Flask que classifica e-mails `PRODUTIVO` ou `IMPRODUTIVO` gerando respostas para cada categoria usando a API da OpenAI.

O backend está em `backend/` e fornece uma página web (templates e static em `frontend/`) onde você pode colar texto ou fazer upload de arquivos `.txt` ou `.pdf` para análise.

## Funcionalidade

- Classifica emails em duas categorias: `PRODUTIVO` ou `IMPRODUTIVO`.
- Gera uma resposta apropriada para cada tipo de categoria.
- Pré-processamento de texto em português (stopwords, stemming) com NLTK.
- Suporta upload de `.txt` e `.pdf` (PyPDF2).

## Pré-requisitos

- Python 3.8+ instalado

Recomenda-se criar um ambiente virtual isolado antes de instalar dependências.

## Instalação

1. Clone o repositório ou copie os arquivos:

```bash
git clone https://github.com/Whofelisberto/automatic-emails.git
cd automatic-emails
cd automatic-emails/backend
```

2. Crie e ative um ambiente virtual (bash):

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows com `bash.exe` (WSL/Mingw) o comando `source .venv/bin/activate` funciona; em PowerShell use `.\.venv\Scripts\Activate.ps1`.

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias (exemplo mínimo):

```
OPENAI_API_KEY=your_openai_api_key
```

O backend usa `python-dotenv` para carregar variáveis do `.env`.

5. Observação sobre NLTK: o projeto baixa recursos NLTK em tempo de execução (`stopwords`, `rslp`). Na primeira execução pode demorar enquanto os pacotes são baixados. Se preferir, pré-baixe manualmente executando:

```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('rslp')"
```

## Como rodar

Execute o servidor Flask a partir da raiz do projeto:

```bash
python backend/app.py
```

O servidor padrão do Flask será iniciado em `http://127.0.0.1:5000/`. Abra o navegador e acesse a página inicial.

## Como funciona (visão rápida)

- `backend/app.py`: ponto de entrada. Recebe POST de `/processar-emails`, faz preprocessamento com `utils.preprocess_text`, lê arquivos com `utils.read_file` e chama a API OpenAI para classificar e gerar a resposta.
- `frontend/templates/index.html` e `frontend/static/`: interface web.
- `requirements.txt`: dependências do projeto.

## Problemas comuns e soluções

- Erro de chave OpenAI: verifique `OPENAI_API_KEY` no `.env` e se ela é válida.
- Erro ao ler PDF: alguns PDFs não têm texto selecionável; o `PyPDF2` pode retornar `None` para páginas sem texto.
- NLTK não encontrado: execute o comando de download de NLTK mostrado acima.
- Porta em uso: defina a variável `PORT` ou modifique `app.run(...)` em `backend/app.py` para usar outra porta.


## Teste rápido

- Com o servidor rodando, acesse `http://127.0.0.1:5000/`, cole um email clique em analisar e-mail.

## Arquivos importantes

- `backend/app.py` — servidor Flask , Routes e integração com OpenAI.
- `backend/utils.py` — funções de preprocessamento e leitura de arquivos.
- `frontend/templates/index.html` — interface.
