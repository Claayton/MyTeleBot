# MyTeleBot

Bot para Telegram
O bot intercepta todas as mensagens enviadas ao usuario e realiza alguns tratamentos e respostas automaticas dependendo da mensagem.
A principal funcionalidade que é implementada e objetivo do bot é filtrar todas as mensagens com vagas para desenvolvedor python e encaminha-las para um grupo específico onde os usuarios podem analizar e aplicar para as vagas.

[🚀 Configurando o ambiente](#setup) - Aqui estão algumas instruções que permitirão que vocẽ obtenha uma cópia do projeto em sua máquina local.

[⚙️ Executando os testes](#tests) - Aqui estão alguns passos bem simples para testar o projeto.

[📦 Detalhes do desenvolvimento](#develop) - Aqui estão alguns detalhes do desenvolvimento da aplicação.

## Setup

## 🚀 Configurando o ambiente

### **📋 Pré-requisitos**:


O projeto foi desenvolvido em um sistema operacional `linux mint 20.03`, essas instruções devem funcionar na maioria dos casos, mas pode ter alguma diferença dependendo do sistema.

Uma das ferramentas exenciais para rodar o programa é o `git`, mas você provavelmente já tem ele na tua maquina.
Outro detalhe importando é que estou utilizando a versão mais recente do python no momento, a `versão 3.10.2`, e é recomendado que utilize a mesma versão para evitar problemas, mas provavelmente deve funcionar em qualquer versão acima da 3.8. 

Eu utilizei `pyenv` para instalar na minha maquina, mas vocẽ pode utilizar o [site oficial](https://www.python.org/downloads/) se preferir.

### __Ambiente virtual__

É uma boa prática criar um ambiente virtual para isolar o projeto da sua maquina e evitar conflitos, utilize o comando a seguir para instalar o `virtualenv` caso ainda não tenha instalado:
```
 sudo pip3 install virtualenv
```
Agora configure seu `ambiente virtual` para evitar possiveis conflitos:
```
python3 -m venv venv 
```
*Em seguida você deverá `ativar` esse ambiente:*
```
source venv/bin/activate 
```
*Agora instale as `bibliotecas e pacotes` necessários para rodar o projeto:*
```
pip3 install -r requirements.txt
```
*Você vai precisar de um arquivo para alocar suas `variáveis de ambiente`, use o comando abaixo para criá-lo e exportar as variáveis (Você deve substituir os valores pelas suas informações pessoais que podem ser encontradas no site da api do telegram):*
```
echo "API_ID=coloque aqui seu api_id 
API_HASH=coloque aqui seu api_hash
BOT_TOKEN=coloque aqui seu bot_token
GROUP_ID=id do grupo que as mensagens devem ser enviadas" > .env
```

*O projeto ja está configurado e pronto para ser testado em modo de desenvolvedor:*
```
python3 run.py
```

## Tests

## ⚙️ Executando os testes

Utilizar para esse projeto o pytest para fazer os testes necessários, e para executar os testes do projeto é muito simples:

```
  # Rodar o testes da forma padrão:
  pytest

  # Rodar os testes mostrando os detalhes caso ocorra algum erro:
  pytest -v
```

* Esse projeto não utiliza coverage.

## Develop

## 📦 Desenvolvimento

* **Biblioteca**: Utilizo nesse projeto a biblioteca [telethon](https://github.com/LonamiWebs/Telethon), que ja me entrega toda a parte de comunicação com servidor.
* **Docker**: Utilizar tambem o docker mas não encontrei ainda uma forma de rodar o programa direto pelo docker-compose, ja que o login na api do telegram depende de um segundo fator de autenticação, e por isso o usuario precisa digitar algumas informações na primeira seção, informações essas que ficam salvas nas proximas seções, e ai sim possibilitam subir o container com o seguinte commando:
```
docker-compose up --build
```
