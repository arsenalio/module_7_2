info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    n = 0
    slem = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        tell = (file.tell())
        n += 1
        file.write(f'{i}\n')
        file.close()
        slem.update({(n, tell):i})
    return slem

result = custom_write('test.txt', info)
for slem in result.items():
    print(slem)