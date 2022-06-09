# Pré requisitos

+ python3
+ no caso do macOS, [macFUSE](https://osxfuse.github.io) instalado e devidas permissões dadas


# Instalação de dependências

Correr o script `install.sh` através do comando 
```
bash install.sh
```

# Configuração da base de dados

1. abrir uma shell do mongo, escrevendo `mongo` num terminal
2. alterar para a base de dados 'fs':
  ``` 
  use fs
  ```
2. criar um novo utilizador (aqui damos o exemplo de um username 'root' e password 'root' que são os default no ficheiro de configuração):
  ```
  db.createUser({
    user:"root",
    pwd:"root",
    roles:[
      {role:"readWrite",db:"fs"}
    ]
  })
  ```


# Utilização

+ adicionar os dados necessários no ficheiro [config.ini](config.ini)
  + credenciais do utilizador criado na configuração da base de dados
  + credenciais do utilizador Gmail do qual os emails serão enviados

+ adicionar permissões
  ```
  python3 access_control.py <caminho do ficheiro> <nome do utilizador> <email>
  ```
+ iniciar o sistema de ficheiros virtual
  ```
  python3 passthroughfs.py <caminho da diretoria a copiar> <caminho da diretoria para onde copiar>
  ```