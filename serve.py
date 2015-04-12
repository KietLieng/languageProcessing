import os.path, flask, nltk
from flask import Flask, request

from pattern.en import comparative, superlative, parsetree
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag


app = Flask(__name__)

@app.route('/')
def hello():
    with open('index.html') as f: 
        return f.read()

@app.route('/acceptPatterns', methods=['POST'])
def acceptPatterns():
    original_content = request.form['drunk_text']
    text_content_array = original_content.split(' ')
    text_content = ''
    for s in text_content_array:
        text_content += superlative(s) + ' '
    s = parsetree(original_content, relations=True, lemmata=True)
    return repr(s)

@app.route('/acceptNLTK', methods=['POST'])
def acceptnltk():
    original_content = request.form['drunk_text']
    sentences_token = nltk.sent_tokenize(original_content)
    #sentences = nltk.pos_tag(sentences_token)
    #sentences = [nltk.word_tokenize(sent) for sent in sentences]
    #sentences = [nltk.pos_tag(sent) for sent in sentences]
    #return 'blah'
    return str(nltk.pos_tag(sentences_token))

if __name__ == "__main__":
    app.run()