with open("путь до файла") as file:
    # Считывает весь файл. Возвращает str
    data = file.read()
    # Считывает строку до символа /n. Возвращает str
    data = file.readline()
    # Считывает все строки. Возвращает лист[str]
    data = file.readlines()
