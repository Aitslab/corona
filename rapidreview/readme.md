This is a web tool for extracting and displaying information from COVID-19-related scientific literature for different target audiences. It is still under development.

It consists of:
1. A dictionary-based tagger (annotationpipeline-dictionary); dictionaries are in https://github.com/Aitslab/corona/tree/master/dictionaries

2. A BioBERT-based tagger (ongoing)

3. A scispacy/spacy-based tagger (annotationpipeline-scispacy); model trained on silver standard corpus from our manuscript (https://arxiv.org/abs/2003.09865) and evaluated on gold standard corpus from same manuscript

4. A rule-based tagger (ongoing)

5. A pipeline for exporting Pubtator annotations from https://www.ncbi.nlm.nih.gov/research/pubtator/; examples of json files in annotationpipeline-pubtator

5. A merging pipeline that merges outputs from 1-5 (ongoing)

6. A web tool with embedded PubAnnotation TextAE viewer (webplatform)

1-5 create output files in PubAnnotation format that will also be uploaded to http://pubannotation.org/, a repository for sharing biomedical annotations in the BioNLP community.


For more info on background and structure of the tool please view the powerpoint file.
