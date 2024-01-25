import BL_UP
import GUI
import IS


def start():
    GUI.starting_work()
    main_loop()
    GUI.ending_work()
    final_input = IS.take_input()


def main_loop():
    in_catalog = False
    catalog_name_where_i_am = False
    life = True
    while life:
        GUI.help_message()
        command_to_do = IS.take_input()
        if in_catalog:
            is_it_command = BL_UP.check_if_it_is_command_in_catalog(command_to_do)
            if is_it_command[0] in ["correct_input", "раскладка_засекла_команда_есть"]:
                command_to_do = is_it_command[1]

                if is_it_command[0] == "correct_input":
                    GUI.found_command()
                elif is_it_command[0] == "раскладка_засекла_команда_есть":
                    GUI.raskladka_command()

                if command_to_do == "help":
                    GUI.help_command_in_catalog()

                elif command_to_do == "leave_catalog":
                    in_catalog = False
                    GUI.user_left_from_catalog()

                elif command_to_do == "add_recept":
                    GUI.take_name_of_recept()
                    recept_name = IS.take_input()
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(recept_name):
                        GUI.print_after_cancel()
                        continue
                    if BL_UP.check_if_correct_data_for_recept(recept_name, "название") != True:
                        GUI.recept_cannot_be_create_because(BL_UP.check_if_correct_data_for_recept(recept_name, "название"))
                        continue
                    GUI.take_sostav_of_recept()
                    sostav = False
                    all_sostav = []
                    while True:
                        GUI.take_ingridient()
                        sostav = IS.take_input()
                        if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                            GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                            in_catalog = False
                            break
                        if sostav in ["stop", "ыещз"]:
                            break
                        if BL_UP.check_if_it_is_cancel_command(sostav):
                            GUI.print_after_cancel()
                            break
                        if BL_UP.check_if_correct_data_for_recept(sostav, "состав") != True:
                            GUI.recept_cannot_be_create_because(BL_UP.check_if_correct_data_for_recept(sostav, "состав"))
                            continue
                        all_sostav.append(sostav)
                        GUI.ingridient_is_saved()
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(sostav):
                        continue
                    if len(all_sostav) == 0:
                        GUI.zero_ingridients_error()
                        continue
                    GUI.take_description()
                    description = IS.take_input()
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(description):
                        GUI.print_after_cancel()
                        continue
                    if BL_UP.check_if_correct_data_for_recept(description, "описание") != True:
                        GUI.recept_cannot_be_create_because(BL_UP.check_if_correct_data_for_recept(description, "описание"))
                        continue
                    GUI.take_time_to_cook()
                    time_to_cook = IS.take_input()
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(time_to_cook):
                        GUI.print_after_cancel()
                        continue
                    if BL_UP.check_if_correct_data_for_recept(time_to_cook, "время") != True:
                        GUI.recept_cannot_be_create_because(BL_UP.check_if_correct_data_for_recept(time_to_cook, "время"))
                        continue
                    recept = BL_UP.create_recept_str(recept_name, all_sostav, description, time_to_cook)
                    GUI.all_data_for_recept_is_correct(recept)
                    while True:
                        GUI.does_user_need_to_save_rec()
                        user_want_to_save_recept_yes_or_no = IS.take_input()
                        if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                            GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                            in_catalog = False
                            break
                        if BL_UP.check_if_it_is_cancel_command(user_want_to_save_recept_yes_or_no):
                            GUI.print_after_cancel()
                            break
                        if BL_UP.user_answered_yes_or_now(user_want_to_save_recept_yes_or_no) == True:
                            BL_UP.add_recept_to_file(catalog_name_where_i_am, recept)
                            BL_UP.change_count_of_recepts_in_catalog(catalog_name_where_i_am, "do_more")
                            GUI.recept_is_saved()
                            break
                        elif BL_UP.user_answered_yes_or_now(user_want_to_save_recept_yes_or_no) == False:
                            GUI.recept_isnot_saved()
                            break
                        else:
                            GUI.didnot_know_what_user_answered_yes_or_now()
                        
                

                elif command_to_do == "see_all_recepts":
                    all_recepts = BL_UP.see_all_recepts(catalog_name_where_i_am)
                    if len(all_recepts) == 0:
                        GUI.it_isnot_any_recept_in_catalog()
                    else:
                        GUI.print_all_recepts(all_recepts)


                elif command_to_do == "find_recept_by_name":
                    GUI.user_want_to_find_rec()
                    recept_name_user_want_to_find = IS.take_input()
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(recept_name_user_want_to_find):
                        GUI.print_after_cancel()
                        continue

                    recepts_with_this_name = BL_UP.find_recept_by_name(catalog_name_where_i_am, recept_name_user_want_to_find)

                    if len(recepts_with_this_name[0]) == 0:
                        GUI.didnot_find_any_recepts()
                    elif len(recepts_with_this_name[0]) == 1:
                        GUI.i_found_1_recept()
                        GUI.print_all_recepts_by_name(recepts_with_this_name[0], recepts_with_this_name[1])
                    else:
                        GUI.i_found_some_recepts()
                        GUI.print_all_recepts_by_name(recepts_with_this_name[0], recepts_with_this_name[1])


                elif command_to_do == "del_recept":
                    GUI.user_want_to_del_rec()
                    recept_to_delete = IS.take_input()
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(recept_to_delete):
                        GUI.print_after_cancel()
                        continue
                    recepts_with_this_name = BL_UP.find_recept_by_name(catalog_name_where_i_am, recept_to_delete)
                    if len(recepts_with_this_name[0]) == 0:
                        GUI.didnot_find_any_recepts()
                        continue
                    elif len(recepts_with_this_name[0]) == 1:
                        GUI.i_found_1_recept()
                        index_rec_to_del = recepts_with_this_name[0][0] + 1
                        GUI.print_all_recepts_by_name(recepts_with_this_name[0], recepts_with_this_name[1])
                    else:
                        GUI.i_found_some_recepts()
                        GUI.print_all_recepts_by_name(recepts_with_this_name[0], recepts_with_this_name[1])
                        while True:
                            GUI.do_choose_whats_recept_do_u_want_to_delete()
                            user_choose = IS.take_input()
                            if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                                GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                                in_catalog = False
                                break
                            if BL_UP.check_if_it_is_cancel_command(user_choose):
                                GUI.print_after_cancel()
                                break
                            if BL_UP.do_choose_in_list(recepts_with_this_name[0], user_choose) == True:
                                index_rec_to_del = recepts_with_this_name[0][int(user_choose) - 1] + 1
                                break
                            else:
                                GUI.index_not_in_list_cant_del(BL_UP.do_choose_in_list(recepts_with_this_name[0], user_choose))
                        if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                            GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                            in_catalog = False
                            continue
                        if BL_UP.check_if_it_is_cancel_command(user_choose):
                            continue
                    while True:
                        GUI.does_user_sure_to_del_rec()
                        does_user_want_to_delete_it_sure = IS.take_input()
                        if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                            GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                            in_catalog = False
                            break
                        if BL_UP.check_if_it_is_cancel_command(does_user_want_to_delete_it_sure):
                            GUI.print_after_cancel()
                            break
                        if BL_UP.user_answered_yes_or_now(does_user_want_to_delete_it_sure) == True:
                            BL_UP.del_recept_by_name(catalog_name_where_i_am, index_rec_to_del)
                            BL_UP.change_count_of_recepts_in_catalog(catalog_name_where_i_am, "do_less")
                            GUI.recept_is_deleted()
                            break
                        elif BL_UP.user_answered_yes_or_now(does_user_want_to_delete_it_sure) == False:
                            GUI.user_doesnot_want_to_del_rec()
                            break
                        else:
                            GUI.didnot_know_what_user_answered_yes_or_now()

                elif command_to_do == "sort_recepts":
                    GUI.how_does_user_want_to_sort_rec()
                    how_to_sort = IS.take_input()
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(how_to_sort):
                        GUI.print_after_cancel()
                        continue
                    how_to_sort_final_version = BL_UP.check_if_correct_sort_from_user(how_to_sort)
                    if how_to_sort_final_version == "дата создания":
                        while True:
                            GUI.user_choosed_date_now_before_or_after()
                            date_time = IS.take_input()
                            if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                                GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                                in_catalog = False
                                break
                            if BL_UP.check_if_it_is_cancel_command(date_time):
                                GUI.print_after_cancel()
                                break
                            ranee_or_pozje = BL_UP.check_if_rannee_or_pozje(date_time)
                            if ranee_or_pozje == "от давних":
                                sorted_lst = BL_UP.sort_by_date(catalog_name_where_i_am, "от давних")
                                if len(sorted_lst) == 0:
                                    GUI.it_isnot_any_recept_in_catalog()
                                else:
                                    GUI.take_your_sorted_list(sorted_lst)
                                break
                            elif ranee_or_pozje == "от новых":
                                sorted_lst = BL_UP.sort_by_date(catalog_name_where_i_am, "от новых")
                                if len(sorted_lst) == 0:
                                    GUI.it_isnot_any_recept_in_catalog()
                                else:
                                    GUI.take_your_sorted_list(sorted_lst)
                                break
                            else:
                                GUI.donot_know_what_did_user_ans_repeat_pls()
                        if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                            GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                            in_catalog = False
                            continue
                        if BL_UP.check_if_it_is_cancel_command(date_time):
                            continue
                    elif how_to_sort_final_version == "время приготовления":
                        while True:
                            GUI.dolshe_po_gotovke_ili_net()
                            time_to_cook = IS.take_input()
                            if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                                GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                                in_catalog = False
                                break
                            if BL_UP.check_if_it_is_cancel_command(time_to_cook):
                                GUI.print_after_cancel()
                                break
                            dolshe_menshe = BL_UP.dolshe_ili_menshe_does_user_want(time_to_cook)
                            if dolshe_menshe == "дольше готовить":
                                sorted_lst = BL_UP.sort_by_time_to_cook(catalog_name_where_i_am, "дольше готовить")
                                if len(sorted_lst) == 0:
                                    GUI.it_isnot_any_recept_in_catalog()
                                else:
                                    GUI.take_your_sorted_list(sorted_lst)
                                break
                            elif dolshe_menshe == "меньше готовить":
                                sorted_lst = BL_UP.sort_by_time_to_cook(catalog_name_where_i_am, "меньше готовить")
                                if len(sorted_lst) == 0:
                                    GUI.it_isnot_any_recept_in_catalog()
                                else:
                                    GUI.take_your_sorted_list(sorted_lst)
                                break
                            else:
                                GUI.donot_know_what_did_user_ans_repeat_pls()
                        if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                            GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                            in_catalog = False
                            continue
                        if BL_UP.check_if_it_is_cancel_command(time_to_cook):
                            continue
                    else:
                        GUI.tak_nelzya_sortirovat()

                elif command_to_do == "find_recept_by_desc":
                    all_ingridients_in_this_rec = []
                    while True:
                        GUI.input_ingridient_which_in_rec_u_want_to_find()
                        ingridient_in_need_rec = IS.take_input()
                        if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                            GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                            in_catalog = False
                            break
                        if ingridient_in_need_rec == "stop":
                            break
                        if BL_UP.check_if_it_is_cancel_command(ingridient_in_need_rec):
                            GUI.print_after_cancel()
                            break
                        if BL_UP.check_if_correct_ingridient(ingridient_in_need_rec):
                            all_ingridients_in_this_rec.append(ingridient_in_need_rec)
                            GUI.ingridient_can_exist()
                        else:
                            GUI.ingridient_cannot_have_special_symbols()
                            break
                    if not(BL_UP.check_if_catalog_can_be_used(catalog_name_where_i_am)):
                        GUI.when_we_worked_with_catalog_we_found_that_it_is_broken()
                        in_catalog = False
                        continue
                    if BL_UP.check_if_it_is_cancel_command(ingridient_in_need_rec):
                        continue
                    if len(all_ingridients_in_this_rec) == 0:
                        GUI.user_didnot_input_any_ingridient()
                    else:
                        all_recepts_with_this_ingridients = BL_UP.find_recepts_by_ingridients(catalog_name_where_i_am, all_ingridients_in_this_rec)
                        if len(all_recepts_with_this_ingridients) == 0:
                            GUI.i_didnot_find_recepts_with_this_ingridients()
                        else:
                            GUI.all_recepts_i_found_with_this_ingridients(all_recepts_with_this_ingridients)

                elif command_to_do == "leave":
                    life = False

            else:
                if command_to_do == "cancel":
                    GUI.cancel_info()
                else:
                    GUI.didnot_find_command()

        else:

            is_it_command = BL_UP.check_if_it_is_command_not_in_catalog(command_to_do)
            if is_it_command[0] in ["correct_input", "раскладка_засекла_команда_есть"]:
                command_to_do = is_it_command[1]

                if is_it_command[0] == "correct_input":
                    GUI.found_command()
                elif is_it_command[0] == "раскладка_засекла_команда_есть":
                    GUI.raskladka_command()

                if command_to_do == "help":
                    GUI.help_command_not_in_catalog()

                elif command_to_do == "go_to_catalog":
                    GUI.take_catalog_name()
                    catalog_name = IS.take_input()
                    if BL_UP.check_if_it_is_cancel_command(catalog_name):
                        GUI.print_after_cancel()
                        continue
                    full_path_from_here_to_catalog = BL_UP.find_catalog(catalog_name)
                    if  full_path_from_here_to_catalog != '*':
                        if BL_UP.check_if_catalog_can_be_used(full_path_from_here_to_catalog):
                            in_catalog = True
                            catalog_name_where_i_am = full_path_from_here_to_catalog
                            GUI.catalog_exists()
                        else:
                            GUI.catalog_u_want_to_open_is_broken()
                    else:
                        GUI.catalog_doesnot_exist()

                elif command_to_do == "create_catalog":
                    GUI.user_want_to_create_catalog()
                    catalog_name = IS.take_input()
                    if BL_UP.check_if_it_is_cancel_command(catalog_name):
                        GUI.print_after_cancel()
                    elif BL_UP.check_if_correct_file_name(catalog_name):
                        BL_UP.create_catalog(catalog_name)
                        GUI.catalog_has_been_created()
                    else:
                        GUI.catalog_isnot_created()

                elif command_to_do == "get_catalog_list":
                    GUI.now_i_will_find_all_catalogs()
                    catalogs = BL_UP.find_all_catalogs_in_dir()
                    if len(catalogs) > 0:
                        GUI.print_all_catalogs(catalogs)
                    else:
                        GUI.i_didnot_find_any_catalog_so_no_list()

                elif command_to_do == "find_catalog":
                    GUI.what_catalog_want_to_find()
                    catalog_name = IS.take_input()
                    if BL_UP.check_if_it_is_cancel_command(catalog_name):
                        GUI.print_after_cancel()
                        continue
                    GUI.now_i_will_find_this_catalog()
                    path_to_catalog = BL_UP.find_catalog(catalog_name)
                    if path_to_catalog == "*":                       #символом выбрана *, т.к. в название файла не может быть *
                        GUI.didnot_find_catalog()
                    else:
                        GUI.i_found_this_catalog(path_to_catalog)

                elif command_to_do == "del_catalog":
                    GUI.catalog_name_user_want_to_delete()
                    catalog_name = IS.take_input()
                    if BL_UP.check_if_it_is_cancel_command(catalog_name):
                        GUI.print_after_cancel()
                        continue
                    path_to_this_file = BL_UP.find_catalog(catalog_name)
                    if path_to_this_file != "*":
                        BL_UP.delete_file(path_to_this_file)
                        GUI.catalog_has_been_deleted()
                    else:
                        GUI.didnot_find_catalog()


                elif command_to_do == "leave":
                    life = False

            else:
                if command_to_do == "cancel":
                    GUI.cancel_info()
                else:
                    GUI.didnot_find_command()