def starting_work():
    print("System: ", end = '')
    print("Работа началась...")


def take_catalog_name():
    print("System: ", end = '')
    print("Введите название каталога, который вы хотите открыть(не используйте для названия: cancel - это ключевое слово)    #без расширения")


def catalog_u_want_to_open_is_broken():
    print("System: ", end = '')
    print("Каталог который вы пытаетесь открыть поврежден, работа с ним будет некорректна")


def when_we_worked_with_catalog_we_found_that_it_is_broken():
    print("System: ", end = '')
    print("При работе с каталогом, мы обнаружили что он поврежден или удален, дальнейшая работа с ним не предусмотрена.")


def catalog_exists():
    print("System: ", end = '')
    print("Мы успешно нашли указанный вами файл! Дальнейшие действия происходят уже в нем")


def catalog_doesnot_exist():
    print("System: ", end = '')
    print("Мы не смогли найти ваш каталог в этой папке")


def user_want_to_create_catalog():
    print("System: ", end = '')
    print("Хорошо, введите название для вашего будущего каталога, учтите правила наименования файла(не используйте для названия: cancel)  #введите название без расширения")


def catalog_has_been_created():
    print("System: ", end = '')
    print("Каталог успешно создан!")


def catalog_isnot_created():
    print("System: ", end = '')
    print('Каталог не создан, проверьте название на отсутствие: \\, /, :, *, ?, ", <, >, |')


def user_doesnot_want_to_create_catalog():
    print("System: ", end = '')
    print("В таком случае повторите ввод, убедитесь в правильности написания имени файла.")


def donot_know_what_user_want_to_do():
    print("System: ", end = '')
    print("Я вас не понял, можете повторить ввод, пожалуйста.")


def ending_work():
    print("System: ", end = '')
    print("Работа завершилась... Нажмите Enter для выхода.")


def all_data_is_correct():
    print("System: ", end = '')
    print("Все данные корректны!")


def help_message():
    print("System: ", end = '')
    print("Напоминаю, чтобы узнать команды для дальнейших действий введите: help или же нужную вам команду")


def found_command():
    print("System: ", end = '')
    print("Команда найдена!")


def raskladka_command():
    print("System: ", end = '')
    print("Команда найдена! Но лучше поменять раскладку, чтобы понимать что ты пишешь.")


def didnot_find_command():
    print("System: ", end = '')
    print("Команда не найдена, попробуйте проверить ввод на правильность и повторите заново")

def help_command_not_in_catalog():
    print("System: ", end = '')
    print("Вот все найденные команды:")
    print("Commands list: help - Показать все команды(вы только что использовали)")
    print("Commands list: cancel - функция позволяет отменить последнюю команду во время ее выполнения(если команда имеет более 1 шага)")
    print("Commands list: go_to_catalog - Зайти в уже существущий каталог")
    print("Commands list: create_catalog - Создать новый каталог рецептов")
    print("Commands list: get_catalog_list - Получить список всех каталогов в этой папке.")
    print("Commands list: find_catalog - Найти каталог по имени")
    print("Commands list: del_catalog - Удалить каталог(по имени)")
    print("Commands list: leave - Выйти из программы(заранее сохраните все, что нужно)")


def help_command_in_catalog():
    print("System: ", end = '')
    print("Commands list: Вот все найденные команды:")
    print("Commands list: help - Показать все команды(вы только что использовали)")
    print("Commands list: cancel - функция позволяет отменить последнюю команду во время ее выполнения(если команда имеет более 1 шага)")
    print("Commands list: leave_catalog - Выйти из текущего каталога, (все внесенные изменения будут сохранены)")
    print("Commands list: add_recept - Добавить рецепт(каталог для сохранения должен быть уже открыт)")
    print("Commands list: see_all_recepts - Показать список всех рецептов(в открытом каталоге)")
    print("Commands list: find_recept_by_name - Найти рецепт по имени(в открытом каталоге)")
    print("Commands list: del_recept - Удалить рецепт по имени (в открытом каталоге)")
    print("Commands list: sort_recepts - Отсортировать рецепты по признаку(дата создания / время приготовления) (в открытом каталоге)")
    print("Commands list: find_recept_by_desc - Поиск рецепта по одному или нескольким ингридиентам (в открытом каталоге)")
    print("Commands list: leave - Выйти из программы(заранее сохраните все, что нужно)")


def user_left_from_catalog():
    print("System: ", end = '')
    print("Вы упешно вышли из каталога!")


def cancel_info():
    print("System: ", end = '')
    print("Вы не можете использовать команду cancel просто так, она может быть использована только при отмене другой команды(если команда имеет более 1 запроса на ввод)")


def i_will_create_new_catalog():
    print("System: ", end = '')


def now_i_will_find_all_catalogs():
    print("System: ", end = '')
    print("Запущен поиск каталогов в этой папке... Вот что мне удалось найти:")


def print_all_catalogs(catalogs):
    for i in catalogs:
        print(i)
    print("System: ", end = '')
    print("Также я указал в каких папках они лежат")


def i_didnot_find_any_catalog_so_no_list():
    print("System: ", end = '')
    print("В вашей папке не найдено абсолютно ни одного каталога")


def what_catalog_want_to_find():
    print("System: ", end = '')
    print("Введите название каталога, который вы хотите найти    #без расширения")


def now_i_will_find_this_catalog():
    print("System: ", end = '')
    print("Произвожу поиск каталога... Вот что мне удалось найти:")


def i_found_this_catalog(path):
    print("System: ", end = '')
    print("Каталог успешно найден! Вот относительный от этой папки путь до него:")
    print(path)


def didnot_find_catalog():
    print("System: ", end = '')
    print("Каталог не найден, проверьте ввод")


def catalog_name_user_want_to_delete():
    print("System: ", end = '')
    print("Введите название каталога, который вы хотите удалить")


def catalog_has_been_deleted():
    print("System: ", end = '')
    print("Каталог успешно найден и удален!")


def recept_cannot_be_create_because(because):
    print("System: ", end = '')
    print(because)

def take_name_of_recept():
    print("System: ", end = '')
    print("Введите название для своего рецепта")


def take_sostav_of_recept():
    print("System: ", end = '')
    print("Данные корректны! А теперь добавляйте за 1 ввод по ингридиенту(когда добавили все что нужно пропишите stop) #не более 25 ингридиентов")


def take_ingridient():
    print("System: ", end = '')
    print("Введите ингридиент")


def ingridient_is_saved():
    print("System: ", end = '')
    print("Ингридиент успешно сохранен!")


def zero_ingridients_error():
    print("System: ", end = '')
    print("В вашем рецепте не может быть 0 ингридиентов!")


def take_description():
    print("System: ", end = '')
    print("Данные корректны! А теперь введите краткое описание для этого рецепта")


def take_time_to_cook():
    print("System: ", end = '')
    print("Данные корректны! А теперь введите время приготовления(в минутах)")


def all_data_for_recept_is_correct(recept):
    print("System: ", end = '')
    print("Все введенные вами данные корректны! Вот получившийся рецепт:")
    print(recept)


def does_user_need_to_save_rec():
    print("System: ", end = '')
    print("Вы хотите сохранить этот рецепт? (yes/no) (да/нет)")


def recept_is_saved():
    print("System: ", end = '')
    print("Рецепт успешно сохранен!")


def recept_isnot_saved():
    print("System: ", end = '')
    print("Рецепт не был сохранен")


def didnot_know_what_user_answered_yes_or_now():
    print("System: ", end = '')
    print("Я вас не понял, повторите ввод (yes/no) (да/нет)")


def print_all_recepts(recepts: list):
    print("System: ", end = '')
    print("Вот все рецепты из вашего каталога:")
    for i in recepts:
        print(i)


def it_isnot_any_recept_in_catalog():
    print("System: ", end = '')
    print("В вашем каталоге еще нет рецептов")


def print_after_cancel():
    print("System: ", end = '')
    print("Вы отменили вызванную вами ранее команду")


def user_want_to_find_rec():
    print("System: ", end = '')
    print("Введите полное имя рецепта, который вы хотите найти")


def didnot_find_any_recepts():
    print("System: ", end = '')
    print("Мы не нашли рецептов по этому имени, проверьте ввод")


def i_found_1_recept():
    print("System: ", end = '')
    print("Вот рецепт, который я нашел:")


def i_found_some_recepts():
    print("System: ", end = '')
    print("Вот все рецепты с этим именем, которые я нашел:")


def print_all_recepts_by_name(indexes, all_recepts):
    for i in indexes:
        print(all_recepts[i])


def user_want_to_del_rec():
    print("System: ", end = '')
    print("Введите название рецепта, который вы хотите удалить")


def does_user_sure_to_del_rec():
    print("System: ", end = '')
    print("Вы точно уверены что хотите удалить этот рецепт? (yes/no) (да/нет)")


def recept_is_deleted():
    print("System: ", end = '')
    print("Рецепт успешно удален!")


def user_doesnot_want_to_del_rec():
    print("System: ", end = '')
    print("Хорошо, рецепт не был затронут!")


def do_choose_whats_recept_do_u_want_to_delete():
    print("System: ", end = '')
    print("Выберите, какой рецепт из этих вы хотите удалить, указав его номер в порядке от 1")


def cannot_del_rec():
    print("System: ", end = '')


def index_not_in_list_cant_del(user_mistake):
    print("System: ", end = '')
    print(user_mistake)


def how_does_user_want_to_sort_rec():
    print("System: ", end = '')
    print("Как вы хотите отсортировать рецепты?(дата создания/время приготовления)")


def user_choosed_date_now_before_or_after():
    print("System: ", end = '')
    print("Хорошо вы хотите отсортировать рецепт(от давних/от новых)")


def tak_nelzya_sortirovat():
    print("System: ", end = '')
    print("Я вас не понял, по вашему ключу нельзя сортировать")


def donot_know_what_did_user_ans_repeat_pls():
    print("System: ", end = '')
    print("Я вас не понял, повторите ввод пожалуйста")


def dolshe_po_gotovke_ili_net():
    print("System: ", end = '')
    print("Какие рецепты вывести первыми, которые(дольше готовить/меньше готовить)")


def take_your_sorted_list(lst):
    print("System: ", end = '')
    print("Вот ваш отсортированный список рецептов")
    for i in lst:
        print("System: ", end = '')
        print(i)


def input_ingridient_which_in_rec_u_want_to_find():
    print("System: ", end = '')
    print("Введите ингридиент который есть в рецепте, который вы ищите")


def ingridient_can_exist():
    print("System: ", end = '')
    print("Хорошо, введите следующий ингридиент или stop если это все")


def ingridient_cannot_have_special_symbols():
    print("System: ", end = '')
    print('Игридиенты не могут содержать специальные символы такие как: "|" и "&"')


def all_recepts_i_found_with_this_ingridients(recepts):
    print("System: ", end = '')
    print("Все рецепты с этими ингридиентами, что я нашел:")
    for i in recepts:
        print(i)


def i_didnot_find_recepts_with_this_ingridients():
    print("System: ", end = '')
    print("В этом каталоге нет рецептов где есть все ваши ингридиенты")


def user_didnot_input_any_ingridient():
    print("System: ", end = '')
    print("Вы не ввели ни одного ингридиента")