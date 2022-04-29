# Интерпретация диалектных слов в российских речевых корпусах
  
`funny/` и `siberian/` -- работа с корпусами звучащей речи [http://spokencorpora.ru/], соответственно "Весёлые истории из жизни" и "Рассказы сибиряков о жизни"

1. Выгрузка данных (текстов корпусов) -- `collecting_data.py`, результаты выгрузки -- `funny/stories_fun` и `siberian/stories_sib`  
2. Обработка тестов с элементами минимальной дискурсивной транскрипции -- `speech_parsing.py`, результаты обработки -- `funny/parsed_fun` и `siberian/parsed_sib`  
3. Лемматизация обработанных текстов, отбор нестандартных слов для интерпретации -- `speech_lemmatization.py`, результаты лемматизации -- `funny/lemmatization_fun` и `siberian/lemmatization_sib`  
4. Подход с интерпретацией нестандартных слов с помощью сравнения векторных представлений слов из словаря модели с векторным представлением предложенного слова (**нерабочий**) -- `close_meaning_words.ipynb`  
5. Подход с подбором модели слова, наиболее подходящего вместо [MASK] -- `mask_word_prediction.ipynb`  

Примеры работы -- `work_examples/`  **!! УСТАРЕВШИЕ, смотрите блокноты**

![example1](https://user-images.githubusercontent.com/46486971/164705112-c748a622-e13c-469c-b7a8-6d27b976993a.png)
![example3](https://user-images.githubusercontent.com/46486971/164705176-231fe362-43b6-4628-a77b-664081cb53f2.png)
