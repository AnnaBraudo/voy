print('Hi. This is an interactive M.Voynarovsky logical test.\nПривет. Это интерактивный тест М. Войнаровского на логическое мышление.\n')
print("You can take the test in Russian or in English.\nВы можете пройти тест на русском или английском языках.\n")
print('The Russian version is taken from testoteka.narod.ru/pozn/1/10-on.html and was translated to English by Anna Braudo.')
print('Русская версия теста взята с testoteka.narod.ru/pozn/1/10-on.html, перевод на английский выполнила Анна Браудо.\n')

lang = input("Would you like to take the test in Russian or in English? Type 'r' or 'e' respectively and click Enter.\nВы бы хотели пройти тест на русском или на английском? Наберите 'р' или 'а' и нажмите Enter.\n")
if lang == 'r' or 'р':
        print("Отлично.")
elif lang == "e" or 'а':
        print("English it is.")