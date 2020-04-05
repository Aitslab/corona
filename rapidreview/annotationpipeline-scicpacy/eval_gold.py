import os
import json
import spacy

version = '1.0'

def main():
    model_dir = os.path.join('models', 'v' + version)
    nlp = spacy.load(model_dir)
    #doc = nlp(text)

    entities = ["Disease_COVID-19", "Virus_SARS-CoV-2"]

    gold_path = os.path.join('annotations', 'gold.json')
    with open(gold_path) as f:
        gold = json.load(f)

    for document in gold["documents"]:
        print("\n\nDocument " + document["id"])
        for passage in document["passages"]:
            doc = nlp(passage["text"])
            print("\n" + passage["infons"]["type"])
            print("From NER")
            for ent in doc.ents:
                print([ent.label_, ent.start_char, ent.end_char, ent.text])
            print("From Gold")
            for annotation in passage["annotations"]:
                if annotation["infons"]["type"] in entities:
                    print([annotation["infons"]["type"], annotation["locations"][0]["offset"], annotation["locations"][0]["length"], annotation["text"]])


if __name__ == "__main__":
    main()
