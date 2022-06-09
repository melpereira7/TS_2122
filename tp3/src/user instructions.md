# Pre requisitos

+ python3
+ no caso do macOS, [macFUSE](https://osxfuse.github.io) instalado e devidas permissões dadas


# Instalação de dependências

Correr o script `install.sh` através do comando 
```
bash install.sh
```


# Utilização

+ adicionar permissões
  ```
  python3 access_control.py <caminho do ficheiro> <nome do utilizador> <email>
  ```
+ iniciar o sistema de ficheiros virtual
  ```
  python3 passthroughfs.py <caminho da diretoria a copiar> <caminho da diretoria para onde copiar>
  ```