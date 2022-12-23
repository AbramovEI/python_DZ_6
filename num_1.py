#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
#насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
#(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
#то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
#В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def rifma(a):
    str = a.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    temp = f(str[0])
    if all([f(i) == temp for i in str]):
        return 'Парам пам-пам'
    return 'Пам парам'

print(rifma("Хорошо-живет-на-свете-Винни-Пух!\
 Оттого-поет-он-эти-Песни-вслух!"))