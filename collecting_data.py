from bs4 import BeautifulSoup
import requests
from tqdm import tqdm


url = "http://spokencorpora.ru/"
# corpus_siberian = "showtrans.py?file=01life/"
corpus_funny_stories = "showtrans.py?file=02funny/"
funny_template = 'FS_'
funny_female = '-f_sp&type=3'
funny_male = '-m_sp&type=3'

for story_number in tqdm(range(1, 41)):
    url_funny = url + corpus_funny_stories + funny_template
    if story_number < 10:
        str_story_number = '0' + str(story_number)
    else:
        str_story_number = str(story_number)
    url_funny += str_story_number
    page = requests.get(url_funny + funny_female)
    if page.text[:12] != 'No such file':
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, "html.parser")
        sex = '-f_sp'
    else:
        page = requests.get(url_funny + funny_male)
        if page.text[:12] != 'No such file':
            page.encoding = 'utf-8'
            soup = BeautifulSoup(page.text, "html.parser")
            sex = '-m_sp'
        else:
            print('Страница не найдена, код:', page.status_code)
            break
    soup.prettify()
    soup = soup.find_all('script')[3]
    text = str(soup).split('\n')
    number = 1
    with open(f'funny_stories//{funny_template}{str_story_number}{sex}.txt', 'w', encoding="utf-8") as file:
        for i in text:
            if 'datastr' in i:
                i = i.split("cell")
                for j in i[1:]:
                    encdec = j.encode('utf-8').decode('utf-8')
                    number_of_speech = f'\"{number}.\"'
                    if number_of_speech in encdec:
                        speech = encdec[encdec.find(number_of_speech):encdec.find(f'\",\"\"]')].split(",")
                        speech = ''.join(speech[1].split("\""))
                        file.write(speech + ' ')
                        number += 1
