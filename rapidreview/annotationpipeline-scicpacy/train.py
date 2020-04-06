import os
import random
import spacy
from spacy.util import minibatch, compounding
from get_data import get_data
from matplotlib import pyplot as plt
from spacy.scorer import Scorer
from spacy.gold import GoldParse

n_iter = 20
evaluate_each = 2
train_split = 0.7
max_docs = 0 # 0 gets all available docs
dropout = 0.2
version = '1.0'
base_model = 'scispacy/en_core_sci_sm/en_core_sci_sm-0.2.4'
#base_model = 'en_core_web_sm'
#base_model = None

def evaluate(nlp, TEST_DATA):
    scorer = Scorer()
    for text, annot in TEST_DATA:
        doc_gold_text = nlp.make_doc(text)
        gold = GoldParse(doc_gold_text, entities=annot.get('entities'))
        pred_value = nlp(text)
        scorer.score(pred_value, gold)

    print('****************************')
    print('Token accuracy: {}'.format(scorer.scores['token_acc']))
    print('F-score: {}'.format(scorer.scores['ents_f']))
    print('P-score: {}'.format(scorer.scores['ents_p']))
    print('R-score: {}'.format(scorer.scores['ents_r']))
    print('****************************')

    return scorer.scores

def main():
    # Enabling GPU somehow corrupts the training results
    #spacy.prefer_gpu()
  
    TRAIN_DATA, TEST_DATA = get_data(train_split, max_docs)

    #Load the model, set up the pipeline and train the entity recognizer.
    if base_model is not None:
        nlp = spacy.load(base_model)  # load existing spaCy model
        print("Loaded model '%s'" % base_model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")

    # create the built-in pipeline components and add them to the pipeline
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    # otherwise, get it so we can add labels
    else:
        ner = nlp.get_pipe("ner")

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    lossarr = []
    fscorearr = []

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if base_model is None:
            nlp.begin_training()
      
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
            lossarr.append(losses['ner'])
            print("Iteration {} of {} - Loss: {}".format(itn + 1, n_iter, losses['ner']))
            if ((itn + 1) % evaluate_each == 0):
                scores = evaluate(nlp, TEST_DATA)
                fscorearr.append(scores['ents_f'])

    model_dir = os.path.join('models', 'v' + version)
    if not os.path.exists('models'):
        os.mkdir(model_dir)
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    info_file = open(os.path.join(model_dir, 'info.txt'), 'w')
    info_file.write("No train docs = {}\n".format(len(TRAIN_DATA)))
    info_file.write("iterations = {}\n".format(n_iter))
    info_file.write("train_split = {}\n".format(train_split))
    info_file.write("dropout = {}\n".format(dropout))
    info_file.write("F-score = {}\n".format(fscorearr[-1]))
    info_file.close()
    
    nlp.to_disk(model_dir)
    print("Saved model to", model_dir)

    plt.plot(lossarr, linestyle='dashed', marker='o')
    plt.xlabel('Epoch')
    plt.ylabel('NER loss')
    plt.show()

    plt.plot(fscorearr, linestyle='dashed', marker='o')
    plt.xlabel('Epoch')
    plt.ylabel('F score')
    plt.show()

if __name__ == "__main__":
    main()
