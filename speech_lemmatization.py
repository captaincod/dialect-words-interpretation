import json
from pymystem3 import Mystem
from pathlib import Path
from tqdm import tqdm

stories_dir = Path('parsed_funny_stories')
lemma_dir = "lemmatization_funny_stories"
m = Mystem()

log = open(f"{lemma_dir}\\log.txt", 'w', encoding='utf-8')
sentences = open(f"{lemma_dir}\\sentences.txt", 'w', encoding='utf-8')
masked = open(f"{lemma_dir}\\masked_sentences.txt", 'w', encoding='utf-8')

for path in tqdm(sorted(stories_dir.glob("*"))):
    with open(path, encoding='utf-8') as file:
        for line in file:

            sentence = line
            masked_sentence = ""

            lemmas = m.lemmatize(line)
            analyze = json.dumps(m.analyze(line), ensure_ascii=False)
            list_from_analyze = json.loads(analyze)
            for word in list_from_analyze:
                if 'analysis' in word:
                    try:
                        if 'qual' in word['analysis'][0]:
                            log.write(f"Непонятное слово: {word['text']}, файл: {path} \n")
                            begin = sentence.find(word['text'])
                            masked_sentence = sentence[:begin] + "[MASK]" + sentence[begin + len(word['text']):]
                            sentence = masked_sentence
                    except IndexError:
                        log.write(f"Нет анализа слова: {word['text']}, файл: {path} \n")
            if len(masked_sentence):
                sentences.write(line + "\n")
                masked.write(masked_sentence + "\n")

log.close()
sentences.close()
masked.close()