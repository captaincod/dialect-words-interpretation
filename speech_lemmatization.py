import json
from pymystem3 import Mystem
from pathlib import Path
from tqdm import tqdm


print(f"Введите номер корпуса\n1: Весёлые истории из жизни\n2: Рассказы сибиряков о жизни")
choice = int(input())
if choice == 1:
    stories_dir = Path("funny\\parsed_fun")
    lemma_dir = "funny\\lemmatization_fun"
    name = "fun"
elif choice == 2:
    stories_dir = Path("siberian\\parsed_sib")
    lemma_dir = "siberian\\lemmatization_sib"
    name = "sib"

mystem = Mystem()

log = open(f"{lemma_dir}\\log.txt", 'w', encoding='utf-8')
sentences = open(f"{lemma_dir}\\{name}_sentences.txt", 'w', encoding='utf-8')
masked = open(f"{lemma_dir}\\{name}_masked.txt", 'w', encoding='utf-8')

for path in tqdm(sorted(stories_dir.glob("*"))):
    with open(path, encoding='utf-8') as file:
        for line in file:
            masked_sentence = ""
            lemmas = mystem.lemmatize(line)
            analyze = json.dumps(mystem.analyze(line), ensure_ascii=False)
            list_from_analyze = json.loads(analyze)
            for word in list_from_analyze:
                if 'analysis' in word:
                    try:
                        if 'qual' in word['analysis'][0]:
                            log.write(f"Непонятное слово: {word['text']}, файл: {path} \n")
                            begin = line.find(word['text'])
                            masked_sentence = line[:begin] + "[MASK]" + line[begin + len(word['text']):]
                    except IndexError:
                        log.write(f"Нет анализа слова: {word['text']}, файл: {path} \n")
            if len(masked_sentence):
                sentences.write(line + "\n")
                masked.write(masked_sentence + "\n")

log.close()
sentences.close()
masked.close()