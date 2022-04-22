from bs4 import BeautifulSoup
import requests
from tqdm import tqdm


url = "http://spokencorpora.ru/"

fun_dir = 'funny\\stories_fun'
fun_corpus = "showtrans.py?file=02funny/"
fun_template = 'FS_'
fun_female = '-f_sp&type=3'
fun_male = '-m_sp&type=3'
fun_quantity = 40

sib_dir = 'siberian\\stories_sib'
sib_corpus = "showtrans.py?file=01life/"
sib_template = 'Sib_'
sib_female = '-f&type=3'
sib_male = '-m&type=3'
sib_quantity = 17

print(f"Введите номер загружаемого корпуса\n1: Весёлые истории из жизни\n2: Рассказы сибиряков о жизни")
choice = int(input())
if choice == 1:
    stories_dir = fun_dir
    corpus = fun_corpus
    template = fun_template
    female = fun_female
    male = fun_male
    quantity = fun_quantity
elif choice == 2:
    stories_dir = sib_dir
    corpus = sib_corpus
    template = sib_template
    female = sib_female
    male = sib_male
    quantity = sib_quantity

for story_number in tqdm(range(1, quantity+1)):
    url_funny = url + corpus + template
    if story_number < 10:
        str_story_number = '0' + str(story_number)
    else:
        str_story_number = str(story_number)
    url_funny += str_story_number
    page = requests.get(url_funny + female)
    if page.text[:12] != 'No such file':
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, "html.parser")
        sex = '-f'
    else:
        page = requests.get(url_funny + male)
        if page.text[:12] != 'No such file':
            page.encoding = 'utf-8'
            soup = BeautifulSoup(page.text, "html.parser")
            sex = '-m'
        else:
            print(f'Страница с номером {quantity} не найдена, код: {page.status_code}')
            break
    soup.prettify()
    soup = soup.find_all('script')[3]
    text = str(soup).split('\n')
    number = 1
    with open(f'{stories_dir}//{template}{str_story_number}{sex}.txt', 'w', encoding="utf-8") as file:
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
