try:
    from  modules import console
    from  modules import info
    from  modules import insertions
   
    console.print_available_dbs()
    dbms_name = console.get_selected_db()

    total_insertions = info.total_inserts()
    db_name = info.db_name()
    tb_name = info.tb_name()
    tb_fields = info.tb_fields()

    if  not console.json_directory_exists:
        print("\n" + chr(27)+"[1;31m","[-]" + chr(27)+"[0m", "Directory 'json' does not exist :(\n")
    
    if not console.json_files_exist:
        print(chr(27)+"[1;31m","[-]" + chr(27)+"[0m", " The 'json' directory is empty:(\n")
        print(chr(27)+"[1;31m","[-]" + chr(27)+"[0m", " There are less options:(\n")

    console.print_available_fields()    
    fields_selected = console.get_selected_fields(tb_fields)

    db_info = {
        "dbms": dbms_name,
        "dbName": db_name,
        "tbName": tb_name,
        "tbFields": tb_fields,
        "insertions": total_insertions,
        "fieldSelected": fields_selected
    }

    print("\n Generating")
    insertions.create_sqlFile(db_info)

except KeyboardInterrupt:
    print("\n\n" + chr(27)+"[1;31m","[-]" + chr(27)+"[0m", "The process has been interrupted :(\n")

except ModuleNotFoundError as error:
    print("\n\n" + chr(27)+"[1;31m","[-]" + chr(27)+"[0m", "Modules are missing :(\n")
    print(chr(27)+"[1;33m","[*]",chr(27)+"[0m", error)
    print(chr(27)+"[1;33m","[*]",chr(27)+"[0m" + " Verify if the directory 'modules' exists")

except Exception as error:
    print("\n\n" + chr(27)+"[1;31m","[-]" + chr(27)+"[0m", f"{error} :( \n")