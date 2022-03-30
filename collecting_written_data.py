from bs4 import BeautifulSoup
import requests
from tqdm import tqdm


url = "http://spokencorpora.ru/"
corpus_funny_stories = "showwritten.py?file=02funny/"
funny_template = 'FS_'
funny_female = '-f_wr'
funny_male = '-m_wr'

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
        sex = funny_female
    else:
        page = requests.get(url_funny + funny_male)
        if page.text[:12] != 'No such file':
            page.encoding = 'utf-8'
            soup = BeautifulSoup(page.text, "html.parser")
            sex = funny_male
        else:
            print('No page found', url_funny)
            break
    soup.prettify()
    written_content = str(soup.find(id="written-content"))
    written_content = written_content[written_content.find('<p>')+3:written_content.find('</p>')]
    if len(written_content.split('   ')) > 1:
        written_content = written_content.split('   ')[1]
    f = open(f'funny_stories_written//{funny_template}{str_story_number}{sex}.txt', 'w', encoding="utf-8")
    f.write(written_content)
    f.close()

