import json
import random

def get_data(train_split = 0.7, max_docs = 0):
    docs = json.loads(open('corona_silver.json', encoding='utf-8').read())
  
    data = []
    for item in docs:
        entities = []
        for annotation in item['denotations']:
            entities.append((annotation['start'], annotation['end'], annotation['id']))
        data.append((item['text'].lower(), { 'entities': entities }))

    random.shuffle(data)

    if max_docs > 0:
        data = data[:max_docs]
    nof_train = int(round(len(data)*train_split))
    train_data = data[:nof_train]
    test_data = data[nof_train:]
    return train_data, test_data

if __name__ == "__main__":
    get_data()
