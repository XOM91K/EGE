def mask_name(name):
    if len(name) <= 2:
        return name[0] + '*' * (len(name) - 1)
    elif len(name) <= 4:
        return name[:2] + '*' * (len(name) - 2)
    else:
        return name[:3] + '*' * (len(name) - 3)

def process_line(line):
    names = line.strip().split()
    masked_names = [mask_name(name) for name in names]
    return ' '.join(masked_names)

def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            masked_line = process_line(line)
            outfile.write(masked_line + '\n')

# Пример использования
input_filename = 'input.txt'  # имя входного файла
output_filename = 'output.txt'  # имя выходного файла

process_file(input_filename, output_filename)