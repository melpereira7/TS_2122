import sys, os
import os.path
from os import path
from pwd import getpwnam  
from pymongo import MongoClient
import configparser

# Insere dados numa coleção
def insertData(file,userName,email):
    config = configparser.ConfigParser()
    # inicia parsing do ficheiro de configuração
    config.read(os.path.abspath('configs/config.data'))
    mongo_user = config['Mongo']['user']
    mongo_pw = config['Mongo']['password']
    client = MongoClient('mongodb://' + mongo_user + ':' + mongo_pw + '@localhost:27017') # Ligação mongo
    mydb = client["filesystem"] # DB que representa o filesystem.
    collist = mydb.list_collection_names()
    if file not in collist: # Verifica se ficheiro já tem coleção.
        files = mydb[file]
    else:
        files = mydb.file
    
    uid = getpwnam(userName).pw_uid # Uid associado ao user.

    # Inesere user uid associado ao email.
    file_data = {
        'uid': uid,
        'email': email
    }

    result = files.insert_one(file_data)
    print('One post: {0}'.format(result.inserted_id))

# Validação de autorização
def validateAccess(filename,userName):
    if(path.exists(filename)): # Verifica se ficheiro existe.
        try:
            getpwnam(userName)
        except KeyError:
            print('User não existe no sistema.')
        if os.getuid() ==  os.stat(sys.argv[1]).st_uid: # Verifica se é o owner do ficheiro.
            return True
        else:
            print("Não és o owner do ficheiro")
            return False
    else:
        print("Ficheiro não existe")
        return False

def main():
    if(len(sys.argv)==4):
        if validateAccess(sys.argv[1],sys.argv[2]):
            insertData(sys.argv[1].split("/")[-1],sys.argv[2],sys.argv[3])
    else:
        print("Tem de ter 3 argumentos")

if __name__ == "__main__":
    main()