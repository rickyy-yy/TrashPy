from datetime import datetime
import os
import threading
import winshell


def empty_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        update_datetime()
    except:
        exit()


def check_datetime():
    pc_user = os.getlogin()
    filepath = f"C:\\Users\\{pc_user}\\Documents\\Python\\TrashPy\\date.txt"
    now = datetime.now()
    temp_datetime = now.strftime("%d/%m/%Y %H:%M")
    current_datetime = datetime.strptime(temp_datetime, '%d/%m/%Y %H:%M')

    with open(filepath, 'r') as file:
        unformatted_datetime = file.read()
        formatted_datetime = datetime.strptime(unformatted_datetime, '%d/%m/%Y %H:%M')
        difference = current_datetime - formatted_datetime
        if difference.days >= 7:
            empty_bin()
        else:
            exit()


def update_datetime():
    pc_user = os.getlogin()
    filepath = f"C:\\Users\\{pc_user}\\Documents\\Python\\TrashPy\\date.txt"

    file = open(filepath, 'w')
    now = datetime.now()
    current_datetime = now.strftime("%d/%m/%Y %H:%M")
    file.write(current_datetime)
    file.close()


def create_datetime_storage():
    pc_user = os.getlogin()
    filepath = f"C:\\Users\\{pc_user}\\Documents\\Python\\TrashPy\\date.txt"

    if not os.path.exists(filepath):
        file = open(filepath, 'x')
        now = datetime.now()
        current_datetime = now.strftime("%d/%m/%Y | %H:%M")
        file.write(current_datetime)
        file.close()


if __name__ == '__main__':
    create_datetime_storage()
    check_datetime()
