import random

import spacy
import sqlite3
from flask import Flask, request, jsonify, g
from numpy import unicode
from spacy.gold import GoldParse

app = Flask(__name__)

DATABASE = 'pos_tagger.db'


@app.route('/Leipzig_UI', methods=['POST'])
def returnLeipzig_UI():
    sentences = {'sentences': request.get_json(force=True)['sentences']}

    nlp_Leipzig_UI = spacy.load('Lezig_UI')
    doc = nlp_Leipzig_UI(sentences['sentences'])

    list_sentence = []
    for token in doc:
        myObject = {}
        myObject['text'] = token.text
        myObject['lemma'] = token.lemma_
        myObject['pos'] = token.pos_
        myObject['tagger'] = token.tag_
        print(token.text)
        list_sentence.append(myObject)
    return jsonify({'list': list_sentence,
                    'sentence': sentences['sentences']})


@app.route('/Britagar_UI', methods=['POST'])
def returnBritagar_UI():
    sentences = {'sentences': request.get_json(force=True)['sentences']}

    nlp_Britagar_UI = spacy.load('Britagar_UI')
    doc = nlp_Britagar_UI(sentences['sentences'])
    # spacy.displacy.serve(doc,style='dep')
    list_sentence = []
    for token in doc:
        myObject = {}
        myObject['text'] = token.text
        myObject['lemma'] = token.lemma_
        myObject['pos'] = token.pos_
        myObject['tagger'] = token.tag_
        print(token.text)
        list_sentence.append(myObject)
    return jsonify({'list': list_sentence,
                    'sentence': sentences['sentences']})


@app.route('/Britagar_PAN', methods=['POST'])
def returnBritagar_PAN10():
    sentences = {'sentences': request.get_json(force=True)['sentences']}

    nlp_Britagar_PAN = spacy.load('Britagar_PAN10')
    doc = nlp_Britagar_PAN(sentences['sentences'])

    list_sentence = []
    for token in doc:
        myObject = {}
        myObject['text'] = token.text
        myObject['lemma'] = token.lemma_
        myObject['pos'] = token.pos_
        myObject['tagger'] = token.tag_
        print(token.text)
        list_sentence.append(myObject)
    return jsonify({'list': list_sentence,
                    'sentence': sentences['sentences']})


@app.route('/Leipzig_PAN', methods=['POST'])
def returnLeipzig_PAN():
    sentences = {'sentences': request.get_json(force=True)['sentences']}

    nlp_Leipzig_PAN10 = spacy.load('Lezig_PAN10')
    doc = nlp_Leipzig_PAN10(sentences['sentences'])

    list_sentence = []
    for token in doc:
        myObject = {}
        myObject['text'] = token.text
        myObject['lemma'] = token.lemma_
        myObject['pos'] = token.pos_
        myObject['tagger'] = token.tag_
        print(token.text)
        list_sentence.append(myObject)
    return jsonify({'list': list_sentence,
                    'sentence': sentences['sentences']})


@app.route('/detail', methods=['POST'])
def returnTag():
    tag = {'tag': request.get_json(force=True)['tag']}
    model_type = {'model_type': request.get_json(force=True)['model_type']}
    cur = get_db().cursor()
    row = cur.execute('SELECT * FROM tag_map where tag = \"' + tag['tag'] + '\" AND model_type= \"' + model_type[
        'model_type'] + '\"').fetchone()
    myObject = {}
    myObject['tag'] = row[1]
    myObject['description'] = row[2]
    myObject['example'] = row[3]
    print(row[1])
    return jsonify({'Detail': myObject, 'tag': tag})


def updateModel(doc, nlp):
    optimizer = nlp.begin_training(build_format(doc))
    for itn in range(100):
        random.shuffle(doc)
        for raw_text, entity_offsets in doc:
            doc = nlp.make_doc(raw_text)
            gold = GoldParse(doc, entities=entity_offsets)
            nlp.update([doc], [gold], drop=0.5, sgd=optimizer)


def build_format(doc):
    list_tag = []
    sentence = ''
    result = []
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)
        sentence = sentence + ' ' + token.text
        list_tag.append(unicode(token.tag_))
    result.append((unicode(sentence[1:]), {'tags': unicode(list_tag)}))
    return result


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
