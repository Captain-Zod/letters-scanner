# letters-scanner

Курсач.<br/><br/>
Заметка на 07.12.2022<br/>
Код превратился в дикий говнокод, где я повытаскивал из базы данных StackOverflow всё что к месту и не к месту. Обещаю себе сделать нормальный такой рефакторинг (не обещаю).<br/><br/>

Запуск: Надо установить все пакеты которые хочет пайтон. Меняете photo.jpg в папке на нужную фотку, запускаете main.py, наводите на букву и нажимаете на кнопку "Here!". Текст последней изменится на предположение, какая это буква. Если ваша фотка полностью черной кистью на белом фоне и не нуждается в применении фильтров, то измените значение DOFILTER на False в mainy.py. ВНИМАНИЕ: Убедитесь что выделение точно по середине и полностью покрывает границы буквы, оставляя совсем чуть-чуть пикселей по сторонам (Пример смотрите ниже).<br/><br/>
![Alt text](example.png)<br/><br/>
Надо запустить generator.py если нужны "эталонные образы".<br/><br/>


Не знаю тянет ли это на полноценную курсовую работу, но я делаю что мне задали, и масштаб проекта меня не волнует.<br/>
Распознавание символов с помощью сравнения их с эталонными образами. Для этого они переводятся в матрицу.<br/><br/>
