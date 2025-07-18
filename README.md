# MiniChatbot
Esto es una prueba de concepto de un chatbot ligero que utilizar modelos NPL con spaCY para reposder preguntas simples 
en españo o inglés simulando un local de juegos de mesa.

## Requisitos
- Python 3.9
- Flask
- spaCy
- langdetect

## Instalación
Se puede utilizar el archivo requirements.txt para instalar las dependencias.
```bash
pip install -r requirements.txt
python -m spacy download es_core_news_sm
python -m spacy download en_core_web_sm
