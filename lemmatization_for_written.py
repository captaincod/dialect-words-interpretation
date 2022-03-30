import json
from pymystem3 import Mystem
from pathlib import Path

stories_dir = Path('funny_stories_written')
m = Mystem()

log = open('funny_stories_written\\lemmatization\\log.txt', 'w', encoding='utf-8')

for path in sorted(stories_dir.glob("*")):
    if not path.is_dir():
        f = open(path, encoding='utf-8')
        text = ""
        for l in f:
            text += l
        new_path = str(stories_dir) + '\lemmatization\\' + str(path)[len(str(stories_dir)) + 1:]
        new_f = open(new_path, 'w', encoding='utf-8')
        new_text = ''
        new_text += text + '\n'
        lemmas = m.lemmatize(text)
        new_text += '\n' + "Леммы:" + '\n' + ''.join(lemmas) + '\n'
        strange_words = []
        analyze = json.dumps(m.analyze(text), ensure_ascii=False)
        list_from_analyze = json.loads(analyze)
        for word in list_from_analyze:
            if 'analysis' in word:
                try:
                    if 'qual' in word['analysis'][0]:
                        log.write(f"Непонятное слово: {word['text']}, файл: {path} \n")
                        strange_words.append(word['text'])
                except IndexError:
                    log.write(f"Нет анализа слова: {word['text']}, файл: {path} \n")
        if len(strange_words) > 0:
            new_text += '\n' + "Непонятные слова:" + '\n' + ' '.join(strange_words) + '\n'
        new_text += "Вся информация:" + '\n' + json.dumps(m.analyze(text), indent=1, ensure_ascii=False)
        f.close()
        new_f.write(new_text)
        new_f.close()
    else:
        break
log.close()
