This is a web tool for extracting and displaying information from COVID-19-related scientific literature for different target audiences. It is still under development and the codes included here are still being polished. They have been submitted for Hack the Crisis Sweden and will also be submitted to the kaggle CORD-19 challenge. For people who want to reuse the code please cite the source and our manuscript (https://arxiv.org/abs/2003.09865). Besides this, the following licence applies: https://github.com/Aitslab/corona/blob/master/license_gpl-3.0.txt

It consists of:
1. A dictionary-based tagger (annotationpipeline-dictionary); dictionaries are in https://github.com/Aitslab/corona/tree/master/dictionaries

2. A BioBERT-based tagger (ongoing)

3. A scispacy/spacy-based tagger (annotationpipeline-scispacy); model trained on silver standard corpus from our manuscript (https://arxiv.org/abs/2003.09865) and evaluated on gold standard corpus from same manuscript

4. A rule-based tagger (ongoing)

5. A pipeline for exporting Pubtator annotations from https://www.ncbi.nlm.nih.gov/research/pubtator/; examples of json files in annotationpipeline-pubtator

5. A merging pipeline that merges outputs from 1-5 (ongoing)

6. A web tool with embedded PubAnnotation TextAE viewer (webplatform)

1-5 create output files in PubAnnotation format that will also be uploaded to http://pubannotation.org/, a repository for sharing biomedical annotations in the BioNLP community The annotated classes are indicated in the annotation_classes.txt file.


For more info on background and structure of the tool please view the powerpoint file.


## Acknowledgement
This code is being developed by the following people:

Sonja Aits, Lund University, project leader, developer, expertise on biomedical applications of artificial intelligence

Salma Kazemi Rashed, developer, bioinformatics expertise (PhD student in Aits group)

Jong Chan Lim, web developer, bioinformatics expertise (Master student in Aits group)

Antton Lamarca, developer, bioinformatics expertise (project student in Aits group)

Annie Tallund, developer (project student in Aits/Nugues groups)

Sofi Flink, developer (project student in Aits/Nugues groups)

Betül Eren Keskin, developer, biomedical expertise

Magnus Ehlde, developer (spacy/scispacy)

external advisors (not team members):

Johan Frid, Humanities Lab, Lund University

Pierre Nugues, Department of Computer Science, Lund University

Cochrane Sweden

Jonas Björk, Lund University

Fernanda Dórea, epidemiologist, developer, National Veterinary Institute

Tomas Rosendal, epidemiologist, advisor, National Veterinary Institute

This work is partially funded by the Swedish Research Council

We make use of tools and code developed by others:

https://pages.semanticscholar.org/coronavirus-research

https://www.ncbi.nlm.nih.gov/research/pubtator/

http://pubannotation.org/

https://github.com/dmis-lab/biobert

https://allenai.github.io/scispacy/

https://spacy.io/






