from flask import Flask, render_template, request
from openai import OpenAI
import os
from utils import preprocess_text
from dotenv import load_dotenv
from utils import read_file


load_dotenv()
openai = OpenAI()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend", "templates"))
STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend", "static"))

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/processar-emails", methods=["POST"])
def process():
    text = request.form.get("text", "")
    file = request.files.get("file")

    if file and file.filename:
        text += " " + read_file(file)

    texto_original = text
    texto_processado = preprocess_text(text)

    prompt = f"""
Classifique o email (texto, .txt ou .pdf) como PRODUTIVO ou IMPRODUTIVO.
Use o TEXTO PROCESSADO apenas para identificar a categoria.
Use o TEXTO ORIGINAL para redigir a resposta.
"PRODUTIVO" emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema). Emails "IMPRODUTIVO" são aqueles que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos). Se for "PRODUTIVO", analise o email e responda adequadamente. Se for "IMPRODUTIVO", responda de forma mais curta de acordo com o contexto. Você responderá sempre os email sob o nome da empresa AutoU.

Email:
{texto_original}
Texto processado:
{texto_processado}

Formato da resposta:
Categoria:
Resposta:
"""

    response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.4
)


    content = response.choices[0].message.content

    categoria = content.split("Categoria:")[1].split("\n")[0].strip()
    resposta = content.split("Resposta:")[1].strip()

    return render_template(
        "index.html",
        categoria=categoria,
        resposta=resposta
    )

if __name__ == "__main__":
    app.run(debug=True)
