cat results_LEX_COVID19.tsv | cut -sf 2 | sort | uniq > terms_LEX_COVID19.tsv
cat results_LEX_SARSCoV2.tsv | cut -sf 2 | sort | uniq > terms_LEX_SARSCoV2.tsv
cat results_DICT_COVID19.tsv | cut -sf 2 | sort | uniq > terms_DICT_COVID19.tsv
cat results_DICT_SARSCoV2.tsv | cut -sf 2 | sort | uniq > terms_DICT_SARSCoV2.tsv
cat results_aitslab_COVID19.tsv | cut -sf 2 | sort | uniq > terms_aitslab_COVID19.tsv
cat results_aitslab_SARSCoV2.tsv | cut -sf 2 | sort | uniq > terms_aitslab_SARSCoV2.tsv
cat results_GRAM_COVID19.tsv | cut -sf 2 | sort | uniq > terms_GRAM_COVID19.tsv
cat results_GRAM_SARSCoV2.tsv | cut -sf 2 | sort | uniq > terms_GRAM_SARSCoV2.tsv

echo "COVID19"

echo "count(GRAM | DICT | LEX | aitslab)="
sort terms_GRAM_COVID19.tsv terms_DICT_COVID19.tsv terms_LEX_COVID19.tsv terms_aitslab_COVID19.tsv | uniq | wc -l

echo "SARSCoV2"

echo "count(GRAM | DICT | LEX | aitslab)="
sort terms_GRAM_SARSCoV2.tsv terms_DICT_SARSCoV2.tsv terms_LEX_SARSCoV2.tsv terms_aitslab_SARSCoV2.tsv | uniq | wc -l
