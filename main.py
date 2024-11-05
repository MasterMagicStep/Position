def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        line_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(line_number, line_byte)] = string
        line_number += 1
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        '二つの言語があるので',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for j in result.items():
        print(j)
