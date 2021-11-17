def read_file(filename):
    file = open(filename, encoding='UTF-8')
    data = []
    for line in file:
        data.append(line)
    file.close()
    return data
