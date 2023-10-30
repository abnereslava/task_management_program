from time import sleep 
todo = [] #unfinished task list
finished_todo = [] #finished task list
positive_ans = ["y", "yes"]
negative_ans = ["n", "no"]

def func_1_main_menu():
    print("-- MAIN MENU --")
    print("(1) Insert new tasks")
    print("(2) View tasks")
    print("(3) Organize tasks")
    print("(4) Mark tasks as finished/unfinished")
    print("(5) Delete tasks")
    print("(6) Quit program")
    menu_0_choice = "0"
    menu_0_choice = str(input("Please, enter the digit of the chosen option: "))
    if menu_0_choice == "1":
        func_insert_task()
    elif menu_0_choice == "2":
        func_2_menu_view_tasks()
    elif menu_0_choice == "3":
        func_3_menu_organize_tasklist()
    elif menu_0_choice == "4":
        func_4_menu_mark_finished()
    elif menu_0_choice == "5":
        func_5_menu_delete_tasks()
    elif menu_0_choice == "6":
        nothing = ""
        print("Shutting down")
        for p in range(3):
            nothing += "."
            print(nothing)
            sleep(0.5)
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_1_main_menu()

def func_insert_task(): #função inserir novas tasks
    print("")
    print("-" *20)
    inserted_task = input("Please, insert a task:\n")
    todo.append(inserted_task)
    print("")
    func_insert_again()

def func_insert_again(): #função que pergunta, após inserir uma task, se quer inserir outra
    print("-" *20)
    new_insert = input("Would you like to insert another task? [y/n]\n").lower()
    if new_insert in positive_ans:
        func_insert_task()
    elif new_insert in negative_ans:
        func_ask_print()
    else:
        print("Invalid answer. Try again.")
        func_insert_again()

def func_ask_print(): #função que pergunta se quer printar tasks não finalizadas
    print("")
    print("-" *20)
    view_tasklist = input("Would you like to view your current tasklist? [y/n]\n").lower()
    print("")
    if len(todo) == 0:
        print("-" *20)
        print("There are no current tasks at the moment.\n")
        func_1_main_menu()
    elif view_tasklist in positive_ans:
        func_print_list()
    elif view_tasklist in negative_ans:
        func_1_main_menu()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_ask_print()

def func_ask_print_finished(): #função que pergunta se quer printar tasks finalizadas
        print("")
        print("-" *20)
        view_finished_tasks = input("Would you like to view your finished tasks? [y/n]\n").lower()
        print("")
        if len(finished_todo) == 0:
            print("-" *20)
            print("There are no finished tasks at the moment.\n")
            func_1_main_menu()
        elif view_finished_tasks in positive_ans:
            func_print_finished_list()
        elif view_finished_tasks in negative_ans:
            func_1_main_menu()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_ask_print_finished()

def func_print_list(): #função que imprime a lista de tasks não finalizadas
    if len(todo) == 0:
        print("-" *20)
        print("There are no current tasks at the moment.\n")
        func_1_main_menu()
    else:
        print("-" *20)
        print("Current tasks:")
        counter = 0
        for i in todo:
            counter +=  1
            print(f"{counter}. {i}")
            sleep(0.3)
        func_1_main_menu()

def func_print_finished_list(): #função que imprime a lista de tasks finalizadas
    if len(finished_todo) == 0:
        print("-" *20)
        print("There are no finished tasks at the moment.\n")
        func_1_main_menu()
    else:
        print("-" *20)
        print("Finished tasks:")
        counter = 0
        for x in finished_todo:
            counter += 1
            print(f"{counter}. {x} ✓")
            sleep(0.3)
        func_1_main_menu()

def func_2_menu_view_tasks(): #finalizado - menu 2
    print("")
    print("-- VIEW TASKS --")
    print("(1) View your current taslkist")
    print("(2) View your finished tasks")
    print("(3) View all tasks")
    print("(4) Go back")
    menu_2_choice = "0"
    menu_2_choice = str(input("Please, enter the digit of the chosen option: "))
    if menu_2_choice == "1":
        print("")
        func_print_list()
    elif menu_2_choice == "2":
        print("")
        func_print_finished_list()
    elif menu_2_choice == "3":
        print("")
        if len(todo) == 0 and len(finished_todo) == 0:
            print("-" *20)
            print("There are no finished or unfinished tasks at the moment.\n")
            func_1_main_menu()
        elif len(todo) == 0 and len(finished_todo) != 0:
            print("-" *20)
            print("Current tasks:")
            print("There are no current tasks at the moment.")
            print("")
            print("Finished tasks:")
            counter2 = 0
            for o in finished_todo:
                counter2 += 1
                print(f"{counter2}. {o} ✓")
                sleep(0.3)
            func_1_main_menu()
        elif len(todo) != 0 and len(finished_todo) == 0:
            print("-" *20)
            print("Current tasks:")
            counter1 = 0
            counter2 = 0
            for l in todo:
                counter1 += 1
                print(f"{counter1} {l}")
                sleep(0.3)
            print("")
            print("Finished tasks:")
            print("There are no finished tasks at the moment.")
            func_1_main_menu()
        else:
            print("-" *20)
            print("Current tasks:")
            counter1 = 0
            counter2 = 0
            for l in todo:
                counter1 += 1
                print(f"{counter1} {l}")
                sleep(0.3)
            print("")
            print("Finished tasks:")
            for o in finished_todo:
                counter2 += 1
                print(f"{counter2}. {o} ✓")
                sleep(0.3)
            func_1_main_menu()
    elif menu_2_choice == "4":
        print("-" *20)
        func_1_main_menu()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_2_menu_view_tasks()
    
def func_4_menu_mark_finished(): #finalizado - menu 4
    print("")
    print("-- MARK TASKS AS FINISHED/UNFINISHED --")
    print("(1) Mark specific tasks as finished")
    print("(2) Mark specific tasks as unfinished")
    print("(3) Mark all tasks as finished")
    print("(4) Mark all tasks as unfinished")
    print("(5) Go back")
    menu_4_choice = "0"
    menu_4_choice = str(input("Please, enter the digit of the chosen option: "))
    if menu_4_choice == "1":
        mark_task_finished()
    elif menu_4_choice == "2":
        mark_task_unfinished()
    elif menu_4_choice == "3":
        if len(todo) == 0:
            print("-" *20)
            print("There are no unfinished tasks at the moment.\n")
            func_4_menu_mark_finished()
        else:
            finished_todo.extend(todo)
            todo.clear()
            print("-" *20)
            print("Done. All tasks marked as finished. ✓")
            func_ask_print_finished()
    elif menu_4_choice == "4":
        if len(finished_todo) == 0:
            print("-" *20)
            print("There are no finished tasks at the moment.\n")
            func_4_menu_mark_finished()
        else:
            todo.extend(finished_todo)
            finished_todo.clear()
            print("-" *20)
            print("Done. All tasks marked as unfinished.")
            func_ask_print()
    elif menu_4_choice == "5":
        print("-" *20)
        func_1_main_menu()    
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_4_menu_mark_finished()

def mark_task_finished(): #função para marcar task especifica como finalizada
    if len(todo) == 0:
        print("-" *20)
        print("There are no unfinished tasks at the moment.\n")
        func_1_main_menu()
    else:
        print("-" *20)
        print("These are your current unfinished tasks:")
        counter = 0
        for i in todo:
            counter +=  1
            print(f"{counter}. {i}")
            sleep(0.3)
        print("")
        mark_task_finished2()

def mark_task_finished2(): #split/continuação lógica da função com mesmo nome
    selected_task = input("Which task would you like to mark as finished? Enter its digit here: ")
    unfinished_list_lenght = len(todo)
    if selected_task in "0123456789":
        selected_task = int(selected_task)
        if selected_task >= 0 and selected_task <= unfinished_list_lenght:
            selected_task -= 1
            print("-" *20)
            print(f"Done. '{todo[selected_task]}' was marked as finished! ✓")
            finished_todo.append(todo[selected_task])
            todo.pop(selected_task)
            func_ask_mark_as_finished_again()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            mark_task_finished2()
    else:
            print("-" *20)
            print("Invalid entry. Try again.")
            mark_task_finished2()

def func_ask_mark_as_finished_again(): #função para perguntar se gostaria de marcar outra task como finalizada
    if len(finished_todo) == 0:
            print("-" *20)
            print("There are no tasks marked as finished anymore.\n")
            func_1_main_menu()
    else:
        print("-" *20)
        repeat_mark_as_finished = input("Would you like to mark another task as finished? [y/n]\n").lower()
        if repeat_mark_as_finished in positive_ans:
            mark_task_finished()
        elif repeat_mark_as_finished in negative_ans:
            func_ask_print_finished()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_ask_mark_as_finished_again()

def mark_task_unfinished(): #função para marcar task especifica como não finalizada
    if len(finished_todo) == 0:
        print("-" *20)
        print("There are no finished tasks at the moment.\n")
        func_1_main_menu()
    else:
        print("-" *20)
        print("These are your finished tasks:")
        counter = 0
        for k in todo:
            counter +=  1
            print(f"{counter}. {k}")
            sleep(0.3)
        print("")
        mark_task_unfinished2()

def mark_task_unfinished2(): #split/continuação lógica da função com mesmo nome
    selected_task = input("Which task would you like to mark as unfinished? Enter its digit here: ")
    finished_list_lenght = len(finished_todo)
    if selected_task in "0123456789":
        selected_task = int(selected_task)
        if selected_task >= 0 and selected_task <= finished_list_lenght:
            selected_task -= 1
            print("-" *20)
            print(f"Done. '{finished_todo[selected_task]}' was marked as finished!")
            todo.append(finished_todo[selected_task])
            finished_todo.pop(selected_task)
            func_ask_mark_as_unfinished_again()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            mark_task_unfinished2()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        mark_task_unfinished2()

def func_ask_mark_as_unfinished_again(): #função para perguntar se gostaria de marcar outra task como não finalizada
    if len(todo) == 0:
            print("-" *20)
            print("There are no tasks marked as unfinished anymore.\n")
            func_1_main_menu()    
    else:
        print("-" *20)
        repeat_mark_as_unfinished = input("Would you like to mark another task as unfinished? [y/n]\n").lower()
        if repeat_mark_as_unfinished in positive_ans:
            mark_task_unfinished()
        elif repeat_mark_as_unfinished in negative_ans:
            func_ask_print()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_ask_mark_as_unfinished_again()

def func_5_menu_delete_tasks():
    print("")
    print("-- DELETE TASKS --")
    print("(1) Delete an unfinished task")
    print("(2) Delete a finished task")
    print("(3) Delete all unfinished tasks")
    print("(4) Delete all finished tasks")
    print("(5) Delete all tasks")
    print("(6) Go back")
    menu_5_choice = "0"
    menu_5_choice = str(input("Please, enter the digit of the chosen option: "))
    if menu_5_choice == "1":
        func_delete_specific_unfinished_task()
    elif menu_5_choice == "2":
        func_delete_specific_finished_task()
    elif menu_5_choice == "3":
        func_delete_all_unfinished_tasks()
    elif menu_5_choice == "4":
        func_delete_all_finished_tasks()
    elif menu_5_choice == "5":
        func_delete_all_tasks()
    elif menu_5_choice == "6":
        print("-" *20)
        func_1_main_menu()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_4_menu_mark_finished()

def func_delete_all_tasks(): #função para deletar todas as tasks
    if len(todo) == 0 and len(finished_todo) == 0:
        print("-" *20)
        print("There are no tasks to delete.\n")
        func_1_main_menu()
    else:
        print("-" *20)
        delete_choice = input("⚠ You're about to delete all your tasks, finished and unfinished. Are you sure you want to proceed? ⚠ [y/n]:\n")
        if delete_choice in positive_ans:
            todo.clear()
            finished_todo.clear()
            nothing = ""
            for y in range(3):
                nothing += "."
                print(nothing)
                sleep(1)
            print("Done! All your tasks have been deleted.")
            print("")
            func_5_menu_delete_tasks()
        elif delete_choice in negative_ans:
            print("-" *20)
            print("Operation suspended. No tasks were deleted.")
            print("")
            func_5_menu_delete_tasks()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_delete_all_tasks()

def func_delete_all_unfinished_tasks():
    if len(todo) == 0:
        print("-" *20)
        print("There are no unfinished tasks to delete.\n")
        func_5_menu_delete_tasks()
    else:
        print("-" *20)
        delete_choice = input("⚠ You're about to delete all your unfinished tasks. Are you sure you want to proceed? ⚠ [y/n]:\n").lower()
        if delete_choice in positive_ans:
            todo.clear()
            nothing = ""
            for y in range(3):
                nothing += "."
                print(nothing)
                sleep(1)
            print("Done! All your unfinished tasks have been deleted.")
            print("")
            func_5_menu_delete_tasks()
        elif delete_choice in negative_ans:
            print("-" *20)
            print("Operation suspended. No tasks were deleted.")
            print("")
            func_5_menu_delete_tasks()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_delete_all_tasks()

def func_delete_all_finished_tasks():
    if len(finished_todo) == 0:
        print("-" *20)
        print("There are no finished tasks to delete.\n")
        func_5_menu_delete_tasks()
    else:
        print("-" *20)
        delete_choice = input("⚠ You're about to delete all your finished tasks. Are you sure you want to proceed? ⚠ [y/n]:\n").lower()
        if delete_choice in positive_ans:
            finished_todo.clear()
            nothing = ""
            for y in range(3):
                nothing += "."
                print(nothing)
                sleep(1)
            print("Done! All your finished tasks have been deleted.")
            print("")
            func_5_menu_delete_tasks()
        elif delete_choice in negative_ans:
            print("-" *20)
            print("Operation suspended. No tasks were deleted.")
            print("")
            func_5_menu_delete_tasks()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_delete_all_tasks()

def func_delete_specific_unfinished_task(): #função para deletar task não finalizada específica
    if len(todo) == 0:
        print("-" *20)
        print("There are no unfinished tasks to delete.\n")
        func_1_main_menu()
    else:
        print("-" *20)
        print("These are your current unfinished tasks:")
        counter = 0
        for m in todo:
            counter +=  1
            print(f"{counter}. {m}")
            sleep(0.3)
        print("")
        func_delete_specific_unfinished_task2()

def func_delete_specific_unfinished_task2(): #split/continuação lógica da função com mesmo nome
    selected_task = input("Which task would you like delete? Enter its digit here: ")
    unfinished_list_lenght = len(todo)
    if selected_task in "0123456789":
        selected_task = int(selected_task)
        if selected_task >= 0 and selected_task <= unfinished_list_lenght:
            selected_task -= 1
            print("-" *20)
            print(f"Done. '{todo[selected_task]}' was deleted!")
            todo.pop(selected_task)
            func_5_menu_delete_tasks()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_delete_specific_unfinished_task2()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_delete_specific_unfinished_task2()

def func_delete_specific_finished_task(): #função para deletar task finalizada específica
    if len(finished_todo) == 0:
        print("-" *20)
        print("There are no finished tasks to delete.\n")
        func_1_main_menu()
    else:
        print("-" *20)
        print("These are your current finished tasks:")
        counter = 0
        for n in finished_todo:
            counter +=  1
            print(f"{counter}. {n}")
            sleep(0.3)
        print("")
        func_delete_specific_finished_task2()

def func_delete_specific_finished_task2(): #split/continuação lógica da função com mesmo nome
    selected_task = input("Which task would you like delete? Enter its digit here: ")
    finished_list_lenght = len(finished_todo)
    if selected_task >= 0 and selected_task <= finished_list_lenght:
        selected_task -= 1
        print("-" *20)
        print(f"Done. '{finished_todo[selected_task]}' was deleted!")
        todo.pop(selected_task)
        func_5_menu_delete_tasks()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_delete_specific_unfinished_task2()

def func_3_menu_organize_tasklist():#menu 3 - finalizado
    print("")
    print("-- ORGANIZE TASKS --")
    print("(1) Rename tasks")
    print("(2) Reorder tasks")
    print("(3) Go back")
    menu_3_choice = "0"
    menu_3_choice = str(input("Please, enter the digit of the chosen option: "))
    if menu_3_choice == "1":
        print("")
        menu_rename_tasks()
    elif menu_3_choice == "2":
        menu_reorder_tasks()
    elif menu_3_choice == "3":
        print("-" *20)
        func_1_main_menu()    
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_3_menu_organize_tasklist()

def menu_rename_tasks(): #menu 3.2 - reorder tasks
    print("(1) Rename an unfinished task")
    print("(2) Rename a finished task")
    print("(3) Go back")
    menu_3_1_choice = "0"
    menu_3_1_choice = str(input("Please, enter the digit of the chosen option: "))
    print("")
    if menu_3_1_choice == "1":
        if len(todo) == 0:
            print("-" *20)
            print("There are no unfinished tasks to rename.\n")
            menu_rename_tasks()
        else:
            print("-" *20)
            print("These are your current unfinished tasks:")
            counter = 0
            for a in todo:
                counter +=  1
                print(f"{counter}. {a}")
                sleep(0.3)
            print("")
            func_rename_specific_unfinished()
    elif menu_3_1_choice == "2":
        if len(finished_todo) == 0:
                print("-" *20)
                print("There are no finished tasks to rename.\n")
                menu_rename_tasks()
        else:
            print("-" *20)
            print("These are your current finished tasks:")
            counter = 0
            for v in finished_todo:
                counter +=  1
                print(f"{counter}. {v} ✓")
                sleep(0.3)
            print("")
            func_rename_specific_finished()
    elif menu_3_1_choice == "3":
        print("-" *20)
        func_3_menu_organize_tasklist()    
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_3_menu_organize_tasklist()

def func_rename_specific_unfinished(): #função que renomeia as taks
    selected_task = input("Which task would you like rename? Enter its digit here: ")
    unfinished_list_lenght = len(todo)
    if selected_task in "0123456789":
        selected_task = int(selected_task)
        if selected_task >= 0 and selected_task <= unfinished_list_lenght:
            selected_task -= 1
            print("-" *20)
            print(f"The selected task was: {todo[selected_task]}")
            new_task_name = input("Enter its new name: ")
            todo[selected_task] = new_task_name
            print("...")
            print("Done!")
            print("")
            menu_rename_tasks()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_rename_specific_unfinished()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_rename_specific_unfinished()

def func_rename_specific_finished(): #função que renomeia as taks finalizadas
    selected_task = input("Which finished task would you like rename? Enter its digit here: ")
    finished_list_lenght = len(finished_todo)
    if selected_task in "0123456789":
        selected_task = int(selected_task)
        if selected_task >= 0 and selected_task <= finished_list_lenght:
            selected_task -= 1
            print("-" *20)
            print(f"The selected task was: {finished_todo[selected_task]} ✓")
            new_task_name = input("Enter its new name: ")
            finished_todo[selected_task] = new_task_name
            print("...")
            print("Done!")
            print("")
            menu_rename_tasks()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_rename_specific_finished()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_rename_specific_finished()

def menu_reorder_tasks(): #menu 3.2.1
    print("-" *20)
    print("(1) Reorder tasks by number")
    print("(2) Reorder tasks by name")
    print("(3) Go back")
    menu_3_2_1_choice = "0"
    menu_3_2_1_choice = str(input("Please, enter the digit of the chosen option: "))
    print("")
    if menu_3_2_1_choice == "1":
        print("-" *20)
        print("(1) Unfinished tasks")
        print("(2) Finished tasks")
        print("(3) Go back")
        menu_3_2_1_1_choice = 0
        menu_3_2_1_1_choice = input("Please, enter the digit of the chosen option: ")
        print("")
        if menu_3_2_1_1_choice == "1":
            func_change_positions_unfinished()
        elif menu_3_2_1_1_choice == "2":
            func_change_positions_finished()
        elif menu_3_2_1_1_choice == "3":
            menu_reorder_tasks()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            menu_reorder_tasks()
    elif menu_3_2_1_choice == "2":
        func_menu_3_2_1()
    elif menu_3_2_1_choice == "3":
        print("-" *20)
        func_3_menu_organize_tasklist()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        menu_reorder_tasks()
        
def func_menu_3_2_1(): #menu 3.2.1 - choice 2
    print("")
    print("(1) Sort all unfinished tasks in alphabetical order")
    print("(2) Sort all finished tasks in alphabetical order")
    print("(3) Sort all tasks in alphabetical order")
    print("(4) Go back")
    menu_3_2_1_choice2 = 0
    menu_3_2_1_choice2 = str(input("Please, enter the digit of the chosen option: "))
    print("")
    if menu_3_2_1_choice2 == "1":
        if len(todo) == 0:
            print("-" *20)
            print("There are no unfinished tasks to sort.\n")
            func_menu_3_2_1()
        else:
            sort_confirmation = input("Are you sure? [y/n]").lower()
            if sort_confirmation in positive_ans:
                todo.sort()
                nothing = ""
                for q in range(3):
                    nothing += "."
                    print(nothing)
                    sleep(1)
                    print("Done! All your unfinished tasks have been sorted in alphabetical order.")
                    print("")
                func_menu_3_2_1()
            if sort_confirmation in negative_ans:
                print("-" *20)
                print("Operation suspended. No tasks were sorted.")
                print("")
                func_menu_3_2_1()
            else:
                print("-" *20)
                print("Invalid entry. Try again.")
                func_menu_3_2_1()
    elif menu_3_2_1_choice2 == "2": #sort all finished tasks in alphabetical order
        if len(finished_todo) == 0:
            print("-" *20)
            print("There are no finished tasks to sort.\n")
            func_menu_3_2_1()
        else:
            sort_confirmation = input("Are you sure? [y/n]").lower()
            if sort_confirmation in positive_ans:
                finished_todo.sort()
                nothing = ""
                for owo in range(3):
                    nothing += "."
                    print(nothing)
                    sleep(1)
                    print("Done! All your finished tasks have been sorted in alphabetical order.")
                    print("")
                func_menu_3_2_1()
            if sort_confirmation in negative_ans:
                print("-" *20)
                print("Operation suspended. No tasks were sorted.")
                print("")
                func_menu_3_2_1()
            else:
                print("-" *20)
                print("Invalid entry. Try again.")
                func_menu_3_2_1()
    elif menu_3_2_1_choice2 == "3": #sort all tasks in alphabetical order
        if len(finished_todo) == 0 and len(todo) == 0:
            print("-" *20)
            print("There are no tasks to sort.\n")
            func_menu_3_2_1()
        else:
            sort_confirmation = input("Are you sure? [y/n]").lower()
            if sort_confirmation in positive_ans:
                finished_todo.sort()
                todo.sort()
                nothing = ""
                for wwe in range(3):
                    nothing += "."
                    print(nothing)
                    sleep(1)
                    print("Done! All your tasks have been sorted in alphabetical order.")
                    print("")
                func_menu_3_2_1()
            if sort_confirmation in negative_ans:
                print("-" *20)
                print("Operation suspended. No tasks were sorted.")
                print("")
                func_menu_3_2_1()
            else:
                print("-" *20)
                print("Invalid entry. Try again.")
                func_menu_3_2_1()
    elif menu_3_2_1_choice2 == "4":
        print("-" *20)
        menu_reorder_tasks()    
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_menu_3_2_1()

def func_change_positions_unfinished():
    if len(todo) == 0:
            print("-" *20)
            print("There are no unfinished tasks to reorder.\n")
            func_3_menu_organize_tasklist()
    else:
        print("-" *20)
        print("These are your current unfinished tasks:")
        counter = 0
        for lll in todo:
            counter +=  1
            print(f"{counter}. {lll}")
            sleep(0.3)
        print("")
        func_select_change_position()

def func_select_change_position(): #função que muda a posição das tasks não finalizadas na lista
    selected_task = 0
    selected_task = input("Which task would you like to change positions in the list? Enter its digit here: ")
    unfinished_list_lenght = len(todo)
    if selected_task in "0123456789":
        selected_task = int(selected_task)
        if selected_task >= 0 and selected_task <= unfinished_list_lenght:
            selected_task -= 1
            print("-" *20)
            print(f"The selected task was: {todo[selected_task]}")
            new_position = input("What position would you like to change it to? ")
            if new_position in "0123456789":
                new_position = int(new_position)
                if new_position >= 0 and new_position <= unfinished_list_lenght:
                    print("-" *20)
                    print(f"Done. {todo[selected_task]} was moved to position {new_position}!")
                    print("-" *20)
                    new_position -= 1
                    moving_item = todo.pop(selected_task)
                    todo.insert(new_position, moving_item)
                    menu_reorder_tasks()
                else:
                    print("-" *20)
                    print("Invalid entry. Try again.")
                    func_select_change_position()
            else:
                print("-" *20)
                print("Invalid entry. Try again.")
                func_select_change_position()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_select_change_position()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_select_change_position()

def func_change_positions_finished():
    if len(finished_todo) == 0:
            print("-" *20)
            print("There are no finished tasks to reorder.\n")
            func_3_menu_organize_tasklist()
    else:
        print("-" *20)
        print("These are your current finished tasks:")
        counter = 0
        for klb in finished_todo:
            counter +=  1
            print(f"{counter}. {klb} ✓")
            sleep(0.3)
        print("")
        func_select_finished_change_position()

def func_select_finished_change_position(): #função que muda a posição das tasks finalizadas na lista
    selected_task = input("Which task would you like to change positions in the list? Enter its digit here: ")
    finished_list_lenght = len(finished_todo)
    if selected_task in "0123456789":
        selected_task = int(selected_task)
        if selected_task >= 0 and selected_task <= finished_list_lenght:
            selected_task -= 1
            print("-" *20)
            print(f"The selected finished task was: {finished_todo[selected_task]} ✓")
            new_position = input("What position would you like to change it to? ")
            if new_position in "0123456789":
                new_position = int(new_position)
                if new_position >= 0 and new_position <= finished_list_lenght:
                    print("-" *20)
                    print(f"Done. {finished_todo[selected_task]} ✓ was moved to position {new_position}!")
                    print("-" *20)
                    new_position -= 1
                    moving_item = finished_todo.pop(selected_task)
                    finished_todo.insert(new_position, moving_item)
                    menu_reorder_tasks()
                else:
                    print("-" *20)
                    print("Invalid entry. Try again.")
                    func_select_finished_change_position()
            else:
                print("-" *20)
                print("Invalid entry. Try again.")
                func_select_finished_change_position()
        else:
            print("-" *20)
            print("Invalid entry. Try again.")
            func_select_finished_change_position()
    else:
        print("-" *20)
        print("Invalid entry. Try again.")
        func_select_finished_change_position()

func_1_main_menu()

#------------------------------------------------------------------------
# ESQUELETO DO CÓDIGO:
# "(1) Insert new task"
# "(2) View tasks"
#     "(2.1) View all unfinished tasks"
#     "(2.2) View all finished taks"
#     "(2.3) View all tasks"
#     "(2.4) Go back"
# "(3) Organize tasks"
#     "(3.1) Rename tasks"
#        "(3.1.1) Raname an unfinished task"
#        "(3.1.2) Rename a finished task"
#        "(3.1.3) Go back"
#     "(3.2) Reorder tasks"
#        "(3.2.1) Reorder a specific task index"
#           "(3.2.1.1) Reorder a unfinished task"
#           "(3.2.1.2) Reorder a finished task"
#           "(3.2.1.3) Go back"
#        "(3.1.2) Reorder all unfinished tasks by name"
#        "(3.1.3) Reorder all finished tasks by name"
#        "(3.1.4) Reorder all tasks by name"
#           "(3.1.4.2) Go back"
#     "(3.3) Go back"
# "(4) Mark tasks as finished/unfinished"
#     "(4.1) Mark a task as finished"
#     "(4.2) Mark a task as unfinished"
#     "(4.3) Mark all tasks as finished"
#     "(4.4) Mark all tasks as unfinished"
#     "(4.5) Go back"
# "(5) Delete tasks"
#     "(5.1) Delete an unfinished task"
#     "(5.2) Delete a finished task"
#     "(5.3) Delete all unfinished tasks"
#     "(5.4) Delete all finished takss"
#     "(5.5) Delete all tasks"
#     "(5.6) Go back"
# "(6) Quit program"
#     "(6.1) Are you sure?"