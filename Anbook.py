import codecs

def pageisnumb(word):  # Добавляем аргумент word
    try:
        int(word[3])
        return True
    except ValueError:
        return False

def yearisnumb(word):  # Добавляем аргумент word
    try:
        int(word[2])
        return True
    except ValueError:
        return False

def BasicFun(source_file, result_file):
    try:
        booksnum = 0
        numpage = []
        bookname = []
        with codecs.open(source_file, 'r', encoding='utf-8') as fr, open(result_file, 'w', encoding='utf-8') as fw:
            for line in fr:
                word = line.strip().split(",")  # Добавляем strip() для удаления пробельных символов в конце строки
                if len(word) > 1:
                    booksnum += 1
                    if pageisnumb(word) and yearisnumb(word):  # Передаем word в качестве аргумента
                        numpage.append(int(word[3]))
                        bookname.append(word[0])
                    elif not pageisnumb(word):
                        print(f"Количество страниц книги под названием {word[0]} указано не в качестве цифр, либо вообще не указано. Эта книга будет пропущена")
                        input("Если прочитали это сообщение, нажмите enter чтобы продолжить выполнение кода.")
                    elif not yearisnumb(word):
                        print(f"Год издания книги под названием: {word[0]} неправильно указан, либо не указан. Книга будет пропущена!")
                        input("Если прочитали это сообщение, нажмите enter чтобы продолжить выполнение кода.")               
            maxpag = max(numpage)
            minpag = min(numpage)
            averagepage = sum(numpage) / len(numpage)
            writebooknum = "Количество книг в файле: " + str(booksnum)
            writeavearg = "Среднее количество страниц в книге: " + str(averagepage)
            writemaxbook = "Книга с наибольшим количеством страниц: " + bookname[numpage.index(maxpag)] + "( " + str(maxpag) + " страниц)"
            writeminbook = "Книга с наименьшим количеством страниц: " + bookname[numpage.index(minpag)] + "( " + str(minpag) + " страниц)"
            fw.write(writebooknum + '\n')
            fw.write(writeavearg + '\n')
            fw.write(writemaxbook + '\n')
            fw.write(writeminbook + '\n')
    except FileNotFoundError:
        print("Файл не найден, создайте файл и перезапустите программу")
        input("Нажмите любую кнопку для выхода.")

BasicFun('books.txt', 'analysis_result.txt')