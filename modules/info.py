
def db_name():
    print(chr(27)+"[1;32m","[+]", chr(27)+"[1;31m","Database name...", chr(27)+"[0m", end="")
    dbName = input("")
    return dbName

def tb_name():
    print(chr(27)+"[1;32m","[+]", chr(27)+"[1;31m","Table name...", chr(27)+"[0m", end="")
    tb_name = input("")
    return tb_name

def tb_fields():    
    print(chr(27)+"[1;32m","[+]", chr(27)+"[1;31m","Table fields...", chr(27)+"[0m", end="")
    fields = input("").split()
    return fields
    
def total_inserts():
    change_color = False
    inserts = ''

    while True:
        if change_color:
            print(chr(27)+"[1;32m","[+]", chr(27)+f"[1;32m","How many inserts do you want to generate?", chr(27)+"[0m", end="")
            inserts = input("")
        else:
            print(chr(27)+"[1;32m","[+]", chr(27)+f"[1;31m","How many inserts do you want to generate?", chr(27)+"[0m", end="")
            inserts = input("")

        if inserts.isnumeric():
            if int(inserts) > 0:
                break
            else:
                print(chr(27)+f"[1;31m"," 0 ", chr(27)+"[0m", 'Invalid number')
        else:
            change_color = True
    return int(inserts)


if __name__ == "__main__":
    print("[+] You have to execute the main script")