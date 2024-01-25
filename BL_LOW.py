import os


def return_data_from_file(file_name: str) -> str:
    '''
    you can get all data from file using this func
    :param file_name: type(str) - path to catalog where we need to get data
    :return: type(str) - all data from file
    '''
    file = open(file_name, "r", encoding = "UTF-8")
    data = file.read()
    file.close()
    return data


def write_something_in_file(file_name: str, something_to_write: str) -> None:
    '''
    you can write(add) something to file using this func
    :param file_name: type(str) - path to catalog where we need to write something
    :param something_to_write: type(str) - something which you need to write in file
    :no return: - it will just write something u need in any file
    '''
    file = open(file_name, "a", encoding = "UTF-8")
    file.write(something_to_write)
    file.close()


def rewrite_file(file_name: str, must_be_in_file: str) -> None:
    '''
    you can rewrite your file using this func, all file"s data will be deleted, and then we will write something.
    :param file_name: type(str) - path to catalog which we need to rewrite
    :param must_be_in_file: type(str) - something which you need to has in your file
    :no return: - it will just rewrite any file
    '''
    file = open(file_name, "w", encoding = "UTF-8")
    file.write(must_be_in_file)
    file.close()


def check_if_catalog_exists_by_path(path_to_catalog: str) -> bool:
    '''
    this func will check if catalog you need to use exists
    :param path_to_catalog: type(str) - path to catalog which we need to check
    :return: type(bool) - True if catalog exists, False if it doesnot
    '''
    path_to_catalog = path_to_catalog.split("\\")
    if len(path_to_catalog) > 1:
        if path_to_catalog[-1] in os.listdir(path_to_catalog[0:len(path_to_catalog):1]):
            return True
    elif len(path_to_catalog) == 1:
        if path_to_catalog[0] in os.listdir():
            return True
    return False


def check_if_catalog_isnot_broken(path_to_catalog: str) -> bool:
    '''
    this func will check if catalog you need to use - can be used
    :param path_to_catalog: type(str) - path to catalog where we need to check data
    :return: type(bool) - True if catalog can be used, False if catalog is broken
    '''
    data = return_data_from_file(path_to_catalog)
    data = data.split("\n")
    first_str_special_symbols_count = 0
    special_symbol = "|"
    another_special_symbols = "&"
    for i in data[0]:
        if i == special_symbol:
            first_str_special_symbols_count += 1
    if not(first_str_special_symbols_count == 2):
        return False
    for i in range(len(data) - 1):
        i += 1
        special_symbol_count = 0
        another_special_symbols_count = 0
        for j in data[i]:
            if j == special_symbol:
                special_symbol_count += 1
            elif j == another_special_symbols:
                another_special_symbols_count += 1
        if special_symbol_count != 4 or another_special_symbols_count < 1:
            return False
        special_symbol_count = 0
        another_special_symbols_count = 0
    return True


def find_all_files_in_dir(path: str) -> list:
    '''
    this func will return you ALL files which any dir has
    :param path: type(str) - path to dir
    :return: type(list) - it will return ALL files which that dir(by path) has
    '''
    catalogs = []
    paths = []
    new_paths = []
    itterations = 0
    while True:
        paths = new_paths
        new_paths = []
        if itterations == 0:
            itterations += 1
            for i in os.listdir(path):
                if os.path.isfile(f"{path}\{i}"):
                    catalogs.append(f"{path}\{i}")
                elif os.path.isdir(f"{path}\{i}"):
                    new_paths.append(f"{path}\{i}")
        else:
            for i in paths:
                for j in os.listdir(i):
                    if os.path.isfile(f"{i}\{j}"):
                        catalogs.append(f"{i}\{j}")
                    elif os.path.isdir(f"{i}\{j}"):
                        new_paths.append(f"{i}\{j}")
        if len(new_paths) == 0:
            return catalogs
        

def only_catalogs_delete_default_files(files: list) -> list:
    '''
    this func will return you only catalogs
    :param files: type(list) - list with paths to files
    :return: type(list) - it will return new list with paths, which incude only paths to catalogs
    '''
    catalogs = []
    for i in files:
        if (i[-1:-9:-1])[::-1] == '.catalog':
            catalogs.append(i)
    return catalogs


def make_new_num_bigger(num: int) -> str:
    '''
    this func will return you bigger num
    :param num: type(int) - num which we need to make bigger
    :return: type(str) - it will return str which include num + 1
    '''
    return str(num + 1)


def make_new_num_less(num: int) -> str:
    '''
    this func will return you less num
    :param num: type(int) - num which we need to make less
    :return: type(str) - it will return str which include num - 1
    '''
    return str(num - 1)