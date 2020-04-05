This is a web tool for extracting and displaying information from COVID-19-related scientific literature for different target audiences. It is still under development.

It consists of:
1. A dictionary-based tagger (annotationpipeline-dictionary); dictionaries are in https://github.com/Aitslab/corona/tree/master/dictionaries

2. A BioBERT-based tagger

3. A scispacy/spacy-based tagger

4. A rule-based tagger

5. A tool exporting Pubtator annotations

5. A merging pipeline that merges outputs from 1-5

6. A web platform

1-5 create output files in PubAnnotation format that can also be uploaded to http://pubannotation.org/.


For background and structure of the tool please view the powerpoint
