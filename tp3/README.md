# Trabalho prático 3


### Base de dados

1. Instalar a **mongodb** e iniciar o serviço, instruções são encontradas [aqui](https://www.mongodb.com/docs/manual/installation/)

2. Abrir uma *shell* do mongo:
   
   `mongo`

3. Criar uma base de dados com o nome ***filesystem***:
   
   `use filesystem`

4. Criar um novo utilizador:
   ```
   db.createUser({
             user: "root",
             pwd: "root",
             roles: [
               { role: "readWrite", db: "filesystem" }
             ]
    })
    ```

