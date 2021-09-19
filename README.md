## Общее описание решения

Проект является цифровым решением в рамках конкурса World AI&DATA Challenge, соответствующиим задаче "<Распознавание химических, математических, физических символов и нот в электронный шрифт Брайля>" (https://git.asi.ru/tasks/world-ai-and-data-challenge/<url задачи>)

Разработанное и представленное Ильёй Оводовым в 2020 году на конкурс World AI&Data Challenge решение Angelina Braille Reader (https://datamasters.ru/digital_solutions_library/social/sol1 : репозиторий - https://git.asi.ru/solutions/world-ai-and-data-challenge/angelina-braille-reader , ссылка на решение - from=http://angelina-reader.ru/), получившее главный приз конкурса, требует расширения своей функциональности на обработку математических, физических и химических текстов, а также нот, написанных Брайлем.Также мы улучшили модель и добавили перевод с текста на брайл.
(https://git.asi.ru/Fazo_Team/braille-reader-bot)

## Общее описание логики работы решения
Разработка модуля распознавания химического, физического и математического языков, а также символом нотного стана с целью развития модели Angelina Braille Reader

Ползователь может запустить бота с помощью Telegram : T.me/Fazouzbot



## Требования к окружению для запуска продукта
Платформа: кроссплатформенное решение, linux, windows, macOS, иное.

Используемый язык программирования с указанием версии(Python 3.8+), если существенно.

## Сценарий сборки и запуска проекта
Приведите пошаговую инструкцию по запуску вашего проекта.

        1) Найти по ссылку : T.me/fazouzbot
        2) Запустить и регистрироваться 
        3) Далее выбрать необходимый параметр Text --> Braille или Braille --> Text
        4) Нажимать кнопку отправить фото и выбрать необходимую картинку для перевода  


## Сценарий компиляции и запуска
``` 
git clone https://git.asi.ru/Fazo_Team/braille-reader-bot

pip install -r requirements.txt

wget -O weights/model.t7 http://angelina-reader.ovdv.ru/retina_chars_eced60.clr.008

python3 app.py
```
## Примеры использования


https://youtube.com/shorts/bN4xtTGXQhw?feature=share


## Используемые наборы данных

https://elib.bspu.by/bitstream/doc/4402/1/Условные обозначения по система Брайля_2010wm.pdf

## Дополнительный инструментарий

Дополнительные инструменты, которые требуются для развёртывания решения.
frameworks(OpenCV, Pillow, Aiogramm, Keras, Telegram Bot API)

## General Solution Description

The project is the digital solution for a World AI&DATA Challenge's task "<Recognition of chemical, mathematical, physical symbols and notes in electronic Braille>" (https://git.asi.ru/tasks/world-ai-and-data-challenge/<task url>)

Developed and presented by Ilya Ovodov in 2020 for the World AI&Data Challenge competition, the Angelina Braille Reader solution (https://datamasters.ru/digital_solutions_library/social/sol1 : repository - https://git.asi.ru/solutions/world-ai-and-data-challenge/angelina-braille-reader , link to the solution - from=http: / / angelina-reader. ru/), which received the main prize of the competition, requires expanding its functionality to process mathematical, physical and chemical texts, as well as notes written in Braille.We also improved the model and added a translation from text to braille.
(https://git.asi.ru/Fazo_Team/braille-reader-bot)

## Solution's logics general description

Development of a module for recognizing chemical, physical and mathematical languages, as well as the symbol of the musical notation in order to develop the Angelina Braille Reader model

The user can launch the bot using Telegram : T.me/Fazouzbot

## Execution environmental requirements and setup
Platform: cross-platform solution, linux, windows, macOS, other.

The programming language used, indicating the version (Python 3.8+), if significant.



## Compilation and launch scenario

```
git clone https://git.asi.ru/Fazo_Team/braille-reader-bot

pip install -r requirements.txt

wget -O weights/model.t7 http://angelina-reader.ovdv.ru/retina_chars_eced60.clr.008

python3 app.py
```


## Use cases and examples

https://youtube.com/shorts/bN4xtTGXQhw?feature=share


## Used datasets 

https://elib.bspu.by/bitstream/doc/4402/1/Условные обозначения по система Брайля_2010wm.pdf

## Additional instrumentation and tools

frameworks(OpenCV, Pillow, Aiogramm, Keras, Telegram Bot API)