import os


PATH = r'C:\Users\Karen\OneDrive\Рабочий стол\lesson'
def parse_path(path:str, count_file = 0, count_folder = 0):
    list_dir = os.listdir(path)
    for el in list_dir:
        el_path = os.path.join(path, el)
        if os.path.isdir(el_path):
            count_folder += 1
            count_file, count_folder = parse_path(el_path, count_file, count_folder)
        else:
            count_file += 1
    return count_file, count_folder

print(parse_path(PATH))