import os
import platform

# Lista de DBMS
__db_list = [
    'MariaDB',
    'MySQL',
    'SQL-Server', 
    'PostgreSQL', 
    'SQLite'
    ]

# Algunas opciones extra
__extra_options = [
    'age',
    'phone',
    'barcode',
    'number',
    'price',
    'lorem ipsum',
    'id'
    ]

def __json_files_exist():
    exist = False
    try:
        scan_files = os.scandir("./json")
        if any(scan_files):
            exist = True
    except:
        None

    return exist

# Verificar si la carpeta 'json' existe
json_directory_exists = os.path.exists("./json")
json_files_exist = __json_files_exist()


# Lista de opciones =  Nombre de archivos - carpeta 'json' + opciones estra
def __options_list():
    list = __extra_options

    if json_directory_exists:        
        json_files = os.listdir("./json")                

        if len(json_files) > 0:
            file_names = ",".join(json_files).replace(".json","").split(",")        
            # Generar opciones - Retorna una lista
            list = list + file_names        

    # Primera letra en mayúscula
    for i in range(len(list)):
        list[i] = list[i].title()

    list.sort()
    return list

def __clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# 
# Print DB options
#

def print_available_dbs():
    #__clear_console()
    
    print(chr(27)+"[1;32m","[+]", chr(27)+"[1;31m","Which DB are you going to use?", chr(27)+"[0m")
    for i in range (len(__db_list)):
        print('\t',f'{i}) {__db_list[i]}')


def get_selected_db():
    loop = True

    while loop:
        print(chr(27)+"[1;32m","-->",chr(27)+"[0m", end='')
        option = input("") 
        
        if option.isnumeric() and int(option) < len(__db_list):
            for db_name in __db_list:
                if __db_list[int(option)] == db_name:
                    option = db_name
                    loop = False
                    break     
        else:
            for db_name in __db_list:
                if option.lower() == db_name.lower():
                    loop = False
                    break
        print("")                            
    return option.lower()

#
# Print Field options
#
def print_available_fields():
    max_length  = 0
    options_list = __options_list()
    
    #__clear_console()
    #print("There are some field options...")    
    print("")
    print(chr(27)+"[1;32m","[+]", chr(27)+"[1;31m","There are some field options...", chr(27)+"[0m")

    for option in options_list:
        if len(option) > max_length:
            max_length = len(option)

    # Adds spaces to the words
    for index in range(len(options_list)):
        if len(options_list[index]) < max_length:
            total_spaces = max_length - len(options_list[index])

            for i in range(total_spaces):
                options_list[index] += " "

    min_value = int(len(options_list)/2)
    max_value = len(options_list) - min_value

    # print field options
    for index in range(max_value):        
        if index == min_value:
            print(f'\t{index})',options_list[index])
        else:
            print(f'\t{index})',options_list[index],f'\t{max_value+index})',options_list[max_value+index])
    print('\n')


def get_selected_fields(fields):
    options_selected = []
    options_list = __options_list()

    for field in fields:
        while True:                    
            print(chr(27)+"[1;32m","[+]",chr(27)+f"[1;32m",f"Field [{field}]... ",chr(27)+"[0m", end="")
            #print('[',chr(27)+"[1;33m",f'{field}',chr(27)+"[0m",']')
            value = input("")

            if value.isnumeric():
                if int(value) < len(options_list):                    
                    index = int(value)
                    options_selected.append(options_list[index].lower().replace(" ",""))
                    break
            else:
                stop = False
                for option in options_list:
                    if value.lower() == option.replace(" ","").lower():
                        options_selected.append(value.lower().replace(" ",""))
                        stop = True
                        break      
                if stop:
                    break
    return options_selected


if __name__ == "__main__":
    print("[+] You have to execute the main script")
