def read_file(name_file):
    with open(name_file, 'r', encoding="utf-8") as file:
        text = file.readlines()
    return text


def write_file(name_file, text):
    with open(name_file, 'w', encoding="utf-8") as file:
        file.writelines(text)
