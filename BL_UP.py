import os
from datetime import datetime
import BL_LOW


def check_if_correct_file_name(file_name: str) -> bool:
    '''
    :param file_name: type(str) - name of file which user wants to create
    :return: type(bool), can be file created or not?
    '''
    for i in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        if i in file_name:
            return False
    return True


def create_catalog(file_name: str) -> None:
    '''
    :param file_name: type(str) - name of file, which will be written in file
    :no return: it will create file, with information about this catalog
    '''
    date = str(datetime.now())[0:10]
    BL_LOW.rewrite_file(f"{file_name}.catalog", f"Название каталога: {file_name} | Количество рецептов в каталоге: 0 | Дата создания: {date}")


def user_answered_yes_or_now(user_answer: str) -> bool or None:
    '''
    if we donot know what did user answer: we will return None
    :param user_answer: type(str) - user inputed something
    :return: type(bool) - if user tried to asnwer yes: True, if his answer is no: False
    '''
    if user_answer.lower() in ["yes", "да"]:
        return True
    elif user_answer.lower() in ["no", "нет"]:
        return False
    return None


def check_if_it_is_command_not_in_catalog(any_command: str) -> tuple:
    '''
    this func can find only commands which you can use if you arenot in catalog
    :param any_command: type(str) - user tried to do any command
    :return: type(tup) - 1st element(str) - if we find command: correct_input or раскладка_засекла_команда_есть; if donot: нет;
    :return: type(tup) - 2ond element(str) - we return corrected command if command exists, or if it doesnot: -1.
    '''
    commands_list = ["help", "go_to_catalog", "create_catalog", "get_catalog_list", "find_catalog", "del_catalog", "leave"]
    commands_raskladka_list = ["рудз", "пщ_ещ_сфефдщп", "скуфеу_сфефдщп", "пуе_сфефдщп_дшые", "аштв_сфефдщп", "вуд_сфефдщп", "дуфму"]
    if any_command.lower() in commands_list:
        return "correct_input", any_command.lower()
    elif any_command.lower() in commands_raskladka_list:
        index = commands_raskladka_list.index(any_command.lower())
        return "раскладка_засекла_команда_есть", commands_list[index]
    return "нет", -1



def check_if_it_is_command_in_catalog(any_command: str) -> tuple:
    '''
    this func can find only command which you can use in catalog
    :param any_command: type(str) - user tried to do any command
    :return: type(tup) - 1st element(str) - if we find command: correct_input or раскладка_засекла_команда_есть; if donot: нет;
    :return: type(tup) - 2ond element(str) - we return corrected command if command exists, or if it doesnot: -1.
    '''
    commands_list = ["help", "leave_catalog", "add_recept", "see_all_recepts", "find_recept_by_name",
                     "del_recept", "sort_recepts", "find_recept_by_desc", "leave"]
    commands_raskladka_list = ["рудз", "дуфму_сфефдщп", "фвв_кусузе", "ыуу_фдд_кусузеы", "аштв_кусузе_ин_тфьу",
                               "вуд_кусузе", "ыщке_кусузеы", "аштв_кусузе_ин_вуыс", "дуфму"]
    if any_command.lower() in commands_list:
        return "correct_input", any_command.lower()
    elif any_command.lower() in commands_raskladka_list:
        index = commands_raskladka_list.index(any_command.lower())
        return "раскладка_засекла_команда_есть", commands_list[index]
    return "нет", -1


def check_if_it_is_cancel_command(any_command: str) -> bool:
    '''
    cancel command needs this func, only hear it can check if user want to cancel something
    :param any_command: type(str) - user tried to input something
    :return: type(bool), if it is cancel: True; if it is something else: False
    '''
    if any_command.lower() in ["cancel", "сфтсуд"]:
        return True
    return False


def find_all_catalogs_in_dir() -> list:
    '''
    this func returns full list of paths to catalogs which u can find in this directory
    :no param:
    :return: type(list) - it will return list which has ALL (paths to) catalogs(files with .catalog) in this directory
    '''
    catalog = []
    for i in os.listdir():
        if os.path.isfile(i):
            catalog.append(i)
        elif os.path.isdir(i):
            all_files_in_this_dir = BL_LOW.find_all_files_in_dir(i)
            for i in all_files_in_this_dir:
                catalog.append(i)
    only_catalogs = BL_LOW.only_catalogs_delete_default_files(catalog)
    return only_catalogs


def find_catalog(catalog_name: str) -> str:
    '''
    if we cannot find catalog in this dir it will return *, because file name cannot has *, it means "We didnot find it"
    :param catalog_name: type(str) - name of catalog which user wants to find
    :return: type(str) - if we find catalog with this name in this dir, we will return path to it (from this dir), else it returns *
    '''
    catalog_name = f"{catalog_name}.catalog"
    for i in os.listdir():
        if os.path.isfile(i):
            if i == catalog_name:
                return i
        elif os.path.isdir(i):
            all_files_in_that_dir = BL_LOW.find_all_files_in_dir(i)
            all_files = [i for i in all_files_in_that_dir]          #нужно для того чтобы переменные ссылались на разные списки
            for i in range(len(all_files)):
                all_files[i] = all_files[i].split("\\")
            for i in range(len(all_files)):
                if catalog_name == all_files[i][-1]:
                    return all_files_in_that_dir[i]
    return "*"


def delete_file(path_to_file: str) -> None:
    '''
    this func can delete file which you want, just give func path to it
    :param file_name: type(str) - path to file we need to delete (from main dir)
    :no return: just deleting file
    '''
    os.remove(f"{path_to_file}")


def check_if_correct_data_for_recept(data, data_type_in_recept: str) -> str or bool:
    '''
    this func will check if data for recept is correct
    :param data: type(str or list) - user want to add any info in his new recept
    :param data_type_in_recept: type(str) - type will help func to know how to test the data
    :return: type(bool or str) - if data is correct, it will return True, else - mistake description(str)
    '''
    if data_type_in_recept == "название":
        if len(data) > 40:
            return "Название должно содержать не более 40 символов"
        elif len(data) < 2:
            return "Название должно содержать более 1 символа"
    elif data_type_in_recept == "состав":
        if len(data) > 20:
            return "Ингридиент не должен содержать более 20 символов"
        elif len(data) < 2:
            return "Ингридиент должен содержать более 1 символа"
    elif data_type_in_recept == "описание":
        if len(data) > 125:
            return "Краткое описание должно занимать не более 125 символов"
        elif len(data) < 2:
            return "Краткое описание должно занимать более 1 символа"
    elif data_type_in_recept == "время":
        if len(data) > 3:
            return "Время приготовления не должно занимать 1000 или более минут"
        elif len(data) == 0:
            return "Обязательно должно быть время приготовления"
    if "|" in data_type_in_recept or "&" in data_type_in_recept:
        return 'Пожалуйста, не используйте эти символы: "|", "&", они нужен для корректной работы программы'
    return True


def create_recept_str(name: str, sostav: list, description: str, time_to_cook: str) -> str:
    '''
    this func returns (str) recept using include data
    :param name: type(str) - name of recept
    :param sostav: type(list) - list of ingridients which will be in recept
    :param description: type(str) - recept"s description
    :param time_to_cook: type(str) - time to cook
    :return: type(str) - it return recept, which inculde all data we gave
    '''
    date = str(datetime.now())[0:10]
    recept = f"Название рецепта: {name} | Состав(ингридиенты): "
    for i in sostav:
        recept = recept + i + " & "
    recept = recept + f"| Краткое описание: {description} | Время готовки: {time_to_cook} минут. | Дата создания рецепта: {date}"
    return recept
    

def change_count_of_recepts_in_catalog(catalog_we_are_in: str, do_more_or_less: str) -> None:
    '''
    this func will change count of recepts when you use create or delete recept func 
    :param catalog_we_are_in: type(str) - path to catalog where we need change count of recepts
    :param do_more_or_less: type(str) - delete and create funcs use it, that why we need 2ond parametr
    :no return: it just will change count of recepts in any catalog
    '''
    all_data = BL_LOW.return_data_from_file(catalog_we_are_in)
    all_data = all_data.split("\n")
    data = all_data[0]
    special_symbol = "|"
    count_of_symbols = 0
    all_another_info_before_count = ''
    count_of_recepts = ''
    we_got_num = False
    all_another_info_after_count = ''
    for i in range(len(data)):
        if data[i] == special_symbol:
            count_of_symbols += 1
            if count_of_symbols == 1:
                all_another_info_before_count = all_another_info_before_count + special_symbol
            else:
                all_another_info_after_count = all_another_info_after_count + special_symbol
        elif data[i].isdigit() and count_of_symbols == 1:
            we_got_num = True
            count_of_recepts = count_of_recepts + data[i] 
        elif we_got_num == True:
            all_another_info_after_count = all_another_info_after_count + data[i]
        else:
            all_another_info_before_count = all_another_info_before_count + data[i]
    if do_more_or_less == "do_more":
        new_num = BL_LOW.make_new_num_bigger(int(count_of_recepts))
    elif do_more_or_less == "do_less":
        new_num = BL_LOW.make_new_num_less(int(count_of_recepts))
    all_data[0] = all_another_info_before_count + new_num + all_another_info_after_count
    data_to_write = all_data[0]
    for i in range(len(all_data) - 1):
        data_to_write += f"\n{all_data[i + 1]}"
    BL_LOW.rewrite_file(catalog_we_are_in, data_to_write)



def add_recept_to_file(catalog_name: str, recept: str) -> None:
    '''
    this func will add recept to catalog which u want
    :param catalog_name: type(str) - path to catalog where we need to add a new recept
    :param recept: type(str) - recept str, which include many info
    :no return: it just will add recept to catalog
    '''
    BL_LOW.write_something_in_file(catalog_name, f"\n{recept}")


def see_all_recepts(file_name: str) -> list:
    '''
    this func will give you a list of recepts in catalog
    :param file_name: type(str) - path to catalog where we need to get all recepts
    :return: type(list) - list of all recepts in catalog
    '''
    data = BL_LOW.return_data_from_file(file_name)
    stroks = data.split("\n")
    stroks.pop(0)
    return stroks


def find_recept_by_name(catalog_name: str, recept_name: str) -> tuple:
    '''
    using this func you can find recept, by his name
    :param catalog_name: type(str) - path to catalog with recepts
    :param recept_name: type(str) - name of recept which user needs to find
    :return: type(tuple) - 1st el: type(list) - list of recepts indexes, which has this name;
    :return: type(tuple) - 2ond el: type(list) - list of all recepts in this file;
    '''
    all_recepts_indexes_with_this_name = []
    data = BL_LOW.return_data_from_file(catalog_name)
    data = data.split("\n")
    del data[0]
    first_dvoetochie = False
    recept_name_in_this_line = ''
    for i in range(len(data)):
        for j in data[i]:
            if j == ":" and first_dvoetochie == False:
                first_dvoetochie = True
            elif first_dvoetochie == True:
                if j != "|":
                    recept_name_in_this_line += j
            if j == "|":
                recept_name_in_this_line = recept_name_in_this_line[1:]
                recept_name_in_this_line = recept_name_in_this_line[:-1]
                break
        if recept_name_in_this_line == recept_name:
            all_recepts_indexes_with_this_name.append(i)
        recept_name_in_this_line = ''
        first_dvoetochie = False
    return all_recepts_indexes_with_this_name, data


def del_recept_by_name(catalog_name: str, index: int) -> None:
    '''
    using this func you can delete recept by name
    :param catalog_name: type(str) - path to catalog with recepts
    :param index: type(int) - recept index which func will use to delete recept
    :no return: - it just will delete recept from catalog
    '''
    data = BL_LOW.return_data_from_file(catalog_name)
    data = data.split("\n")
    del data[index]
    new_data = data[0]
    for i in range(len(data) - 1):
        new_data += f"\n{i + 1}"
    BL_LOW.rewrite_file(catalog_name, new_data)


def do_choose_in_list(lst: list, users_choose: str) -> str or bool:
    '''
    using this func you can know if users choice is correct
    :param lst: type(list) - list of recepts
    :param users_choose: type(str) - users index that his want to choose in lst
    :return: type(str, bool) - it will return True if user data is correct, else mistake description(str) 
    '''
    elements_count = len(lst)
    if users_choose.isdigit():
        if int(users_choose) <= elements_count and users_choose != "0":
            return True
        return "Ваше число выходит за рамки списка или является 0"
    return "Вы ввели не целое положительное число"


def check_if_correct_sort_from_user(sort_by: str) -> str:
    '''
    using this func you will know how does user want to sort recepts
    :param sort_by: type(str) - user choose type of sorting
    :return: type(str) - it will return "дата создания" or "время приготовления" if sort_by is correct, else "некорректный ввод"
    '''
    if sort_by.lower() in ["дата создания", "lfnf cjplfybz"]:
        return "дата создания"
    elif sort_by.lower() in ["время приготовления", "dhtvz ghbujnjdktybz"]:
        return "время приготовления"
    return "некорректный ввод"


def check_if_rannee_or_pozje(ot_davnih_or_ot_novix: str) -> str:
    '''
    using this func you will know how does user want to sort recepts(again)
    :param ot_davnih_or_ot_novix: type(str) - user choose type of sorting
    :return: type(str) - it will return "от давних" or "от новых" if sort_by is correct, else "некорректный ввод"
    '''
    if ot_davnih_or_ot_novix.lower() in ["от давних", "jn lfdyb["]:
        return "от давних"
    elif ot_davnih_or_ot_novix.lower() in ["от новых", "jn yjds["]:
        return "от новых"
    return "некорректный ввод"


def dolshe_ili_menshe_does_user_want(dolshe_menshe: str) -> str:
    '''
    using this func you will know how does user want to sort recepts(again)
    :param dolshe_menshe: type(str) - user choose type of sorting
    :return: type(str) - it will return "дольше готовить" or "меньше готовить" if sort_by is correct, else "некорректный ввод"
    '''
    if dolshe_menshe.lower() in ["дольше готовить", "ljkmit ujnjdbnm"]:
        return "дольше готовить"
    elif dolshe_menshe.lower() in ["меньше готовить", "vtymit ujnjdbnm"]:
        return "меньше готовить"
    return "некорректный ввод"


def find_time_to_cook_in_str(str: str) -> int:
    '''
    you will find time to cook by this recept
    :param str: type(str) - it means recept str, 1 str which indlude 1 recept
    :return: type(int) - it will return how much do u need to cook something using recept
    '''
    str_with_time_to_cook = str.split("|")[3]
    all_num = []
    for i in str_with_time_to_cook:
        if i.isdigit():
            all_num.append(i)
    final_num = ''
    for i in all_num:
        final_num = final_num + i
    return int(final_num)


def sort_by_time_to_cook(catalog_name: str, ot_menshego_ili_ot_bolshego: str) -> list:
    '''
    using this func you will sort recepts and return it
    :param catalog_name: type(str) - name of catalog which we are using now
    :param ot_menshego_ili_ot_bolshego: type(str) - type of sorting
    :return: type(list) - list of all sorted recepts
    '''
    data = BL_LOW.return_data_from_file(catalog_name)
    data = data.split("\n")
    del data[0]
    index_helper = 0
    for i in range(len(data)):
        for j in range(len(data) - index_helper):
            j += index_helper
            previos_num = find_time_to_cook_in_str(data[i])
            this_num = find_time_to_cook_in_str(data[j])
            if ot_menshego_ili_ot_bolshego == "дольше готовить":
                if previos_num < this_num:
                    data[i], data[j] = data[j], data[i]
            elif ot_menshego_ili_ot_bolshego == "меньше готовить":
                if previos_num > this_num:
                    data[i], data[j] = data[j], data[i]
        index_helper += 1
    return data


def what_date_is_bigger(first_date, second_date):
    '''
    using this func you can know what date is bigger
    :param first_date: type(another) - first date
    :param second_date: type(another) - second date
    :return: type(another or str) - it will return bigger date of 2, or "одна и таже дата"
    '''
    if int(first_date[0:4]) > int(second_date[0:4]):
        return first_date
    elif int(first_date[0:4]) < int(second_date[0:4]):
        return second_date
    elif int(first_date[5:7]) > int(second_date[5:7]):
        return first_date
    elif int(first_date[5:7]) < int(second_date[5:7]):
        return second_date
    elif int(first_date[8:10]) > int(second_date[8:10]):
        return first_date
    elif int(first_date[8:10]) < int(second_date[8:10]):
        return second_date
    else:
        return "одна и таже дата"


def find_date_in_str(str: str) -> str:
    '''
    using this func you can know what date in this recept
    :param str: type(str) - str which include 1 recept
    :return: type(str) - it will return only date from recept
    '''
    return (str[-1:-11:-1])[::-1]


def sort_by_date(catalog_name: str, ranee_or_pozje: str) -> list:
    '''
    using this func you will sort recepts and return it
    :param catalog_name: type(str) - name of catalog which we are using now
    :param ranee_or_pozje: type(str) - type of sorting
    :return: type(list) - list of all sorted recepts
    '''
    data = BL_LOW.return_data_from_file(catalog_name)
    data = data.split("\n")
    del data[0]
    index_helper = 0
    for i in range(len(data)):
        for j in range(len(data) - index_helper):
            j += index_helper
            first_date = find_date_in_str(data[i])
            second_date = find_date_in_str(data[j])
            bigger_date = what_date_is_bigger(first_date, second_date)
            if bigger_date == second_date and ranee_or_pozje == "от новых":
                data[i], data[j] = data[j], data[i]
            elif bigger_date == first_date and ranee_or_pozje == "от давних":
                data[i], data[j] = data[j], data[i]
        index_helper += 1
    return data


def find_only_ingridients_in_rec(rec_str: str) -> list:
    '''
    using this func you can get an ingridients list
    :param rec_str: type(str) - string which include 1 recept
    :return: type(list) - list of all ingridients in this recept
    '''
    rec_str = rec_str.split("|")
    rec_str = rec_str[1]
    rec_str = rec_str.split("&")
    del rec_str[-1]
    already_get_dvoetochie = False
    first_ingridient = ''
    for i in rec_str[0]:
        if i == ":":
            already_get_dvoetochie = True
        elif already_get_dvoetochie:
            first_ingridient += i
    rec_str[0] = first_ingridient
    for i in range(len(rec_str)):
        rec_str[i] = rec_str[i][1:len(rec_str[i]) - 1:1]
    return rec_str


def find_recepts_by_ingridients(catalog_name: str, ingrirdients_lst: list) -> list:
    '''
    using this func you can get list of recepts which include some ingridients
    :param catalog_name: type(str) - path to catalog, where we need to find recepts with some ingridients
    :param ingridients_lst: type(list) - list of ingridients
    :return: type(list) - list off all recepts(str) which include off all ingridients we need
    '''
    data = BL_LOW.return_data_from_file(catalog_name)
    data = data.split("\n")
    del data[0]
    recepts_that_has_this_ingridients = []
    recept_podhodit = True
    for i in data:
        ingridients_in_this_rec = find_only_ingridients_in_rec(i)
        for j in ingrirdients_lst:
            if not(j in ingridients_in_this_rec):
                recept_podhodit = False
        if recept_podhodit:
            recepts_that_has_this_ingridients.append(i)
        recept_podhodit = True
    return recepts_that_has_this_ingridients


def check_if_correct_ingridient(ingridient: str) -> bool:
    '''
    this func will check if ingridient can be used in recept
    :param ingridient: type(str) - 1 ingridient which user wants too add to new recept
    :return: type(bool) - True if ingridient can be used, False if ingridient cannot be used
    '''
    if not("|" in ingridient) and not("&" in ingridient):
        return True
    return False


def check_if_catalog_can_be_used(catalog_name: str) -> bool:
    '''
    using thic func you can know if catalog can be used in work
    :param catalog_name: type(str) - path to catalog which we need to use
    :return: type(bool) - True if catalog can be used in work, False if it is deleted or broken
    '''
    if BL_LOW.check_if_catalog_exists_by_path(catalog_name):
        if BL_LOW.check_if_catalog_isnot_broken(catalog_name):
            return True
    return False