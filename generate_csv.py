def grep(file_path, substring):
    with open(file_path, 'r') as file:
        for line in file:
            if substring in line:
                yield line


for line in grep('file.txt', 'substring'):
    print(line)
