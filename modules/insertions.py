from os import name
from tqdm import tqdm
import time
import random
import json
import datetime

def create_sqlFile(dbInfo):
    # SQL - File
    sqlFile = open(f'{dbInfo["tbName"]}.sql',"w")

    if dbInfo["dbms"] == "mariadb" or dbInfo["dbms"] == "mysql":
        sqlFile.write(f"USE {dbInfo['dbName']};\n")

    for i in tqdm(range(dbInfo["insertions"])):
        value_field = []
        tmp_name = []

        for field in dbInfo["fieldSelected"]:            
            # Check if the item 'name' exists in the list. It's necessary to generate the domain
            # Using the generated name 'tmp_name' for the Field-Email
            if field == 'email':
                if len(tmp_name) == 0:
                    file = open(f'./json/name.json',)
                    data = json.load(file)
                    # Storing the name for the fieldName
                    tmp_name.append(data[random.randint(0,len(data)-1)]['name']) 
                
                domain = ['@yahoo.com','@gmail.com','@outlook.com','@example.com','@human.com','@hotmail.com']
                value_field.append(tmp_name[0].lower() + f"{domain[random.randint(0,len(domain)-1)]}")

                file.close()
            
            # Using the generated name 'tmp_name' for the Field-Name
            elif field == 'name':
                if len(tmp_name) == 0:
                    file = open(f'./json/name.json',)
                    data = json.load(file)
                    # Storing the name for the fieldEmail
                    tmp_name.append(data[random.randint(0,len(data)-1)]['name'])                     
                    #value_field.append(tmp_name[0])                    
                    file.close()                     
                
                value_field.append(tmp_name[0]) 
            
            elif field == 'id':
                value_field.append(i+1)  
            
            elif field == 'number':                
                value_field.append(random.randint(1,1000))
            
            elif field == 'barcode':
                code = ''
                for i in range(random.randint(12,15)):
                    code += str(random.randint(0,9))                
                value_field.append(f'{code}')

            elif field == 'age':                
                value_field.append(random.randint(1,100))

            elif field == 'phone':                
                phone = ''
                for i in range(10):
                    phone += str(random.randint(0,9))                
                value_field.append(f'{phone}')

            elif field == 'price':
                value_field.append(round(random.uniform(1.11, 1000.99),2))

            elif field == 'loremipsum':
                lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
                value_field.append(f'{lorem}')

            elif field == 'date':
                today = datetime.date.today()
                delta = datetime.timedelta(days=random.randint(0,4000))
                total = today - delta
                value_field.append(str(total))

            # Other Fields
            else:
                file = open(f'./json/{field}.json',)
                data = json.load(file)
                string = data[random.randint(0,len(data)-1)]['name']
                # 
                if dbInfo["dbms"] == "postgresql" or dbInfo["dbms"] == "sql-server":
                    string = string.replace("'","''")                
                
                value_field.append(string)            
                file.close() 

        # Creating the INSERT sql script
        str_fields = ' '.join(map(str,dbInfo["tbFields"])).replace(" ",",")
        str_values = str(value_field).replace("[","").replace("]","")

        if dbInfo["dbms"] == "postgresql" or dbInfo["dbms"] == "sql-server":
            str_values = str_values.replace('"',"'")    
        
        insertion = f"INSERT INTO {dbInfo['tbName']} ({str_fields}) VALUES ({str_values});"
        #print(f'INSERT INTO {dbInfo["tbName"]}',f'({str_fields})','VALUES',f'({str_values});')
        
        sqlFile.write(f"{insertion}\n")
    
        time.sleep(.000001)
    
    sqlFile.close()
    
    print("\n"+chr(27)+"[1;32m","[+]", chr(27) + "[0m" + "The " + chr(27)+"[1;31m" + f"{dbInfo['tbName']}.sql " + chr(27)+"[0m" + "file has been created." + chr(27)+"[0m" + "\n")

    
if __name__ == "__main__":
   print("[+] You have to execute the main script")

