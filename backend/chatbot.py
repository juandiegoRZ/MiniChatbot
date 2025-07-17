from flask import Flask, request, jsonify
from flask_cors import CORS
from langdetect import detect
import spacy
import json

app = Flask(__name__)
CORS(app)

# se cargan los modelos de lenguaje
nlp_es = spacy.load("es_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

# se cargan las preguntas del archivo json
with open("data.json", encoding="utf-8") as f:
    REPOSITORY = json.load(f)

# se procesan las preguntas con el uso de spacy
question_docs_es = {q: nlp_es(q) for q in REPOSITORY["es"]}
question_docs_en = {q: nlp_en(q) for q in REPOSITORY["en"]}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"reply": "Please enter a valid question."})

    language = detect(user_input)

    # se verifica si el texto está en inglés o en español
    if language == "es":
        user_doc = nlp_es(user_input.lower())
        question_docs = question_docs_es
        responses = REPOSITORY["es"]
    elif language == "en":
        user_doc = nlp_en(user_input.lower())
        question_docs = question_docs_en
        responses = REPOSITORY["en"]
    else:
        return jsonify({"reply": "Unsupported language. Please use English or Spanish."})

    # se usa el umbral de similtud de spacy para verificar la coincidencia de las preguntas
    best_match = None
    best_score = 0.7  # Umbral

    for question, doc in question_docs.items():
        score = user_doc.similarity(doc)
        if score > best_score:
            best_score = score
            best_match = question

    if best_match:
        return jsonify({"reply": responses[best_match]})
    else:
        return jsonify({
            "reply": "Lo siento, no entendí tu consulta. Puedes intentar con otra pregunta." if language == "es"
                     else "Sorry, I didn't understand your question. Please try a different one."
        })

if __name__ == "__main__":
    app.run(debug=True)
