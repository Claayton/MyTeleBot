python3 -m venv venv;
source venv/bin/activate;
pip3 install -r requirements.txt;
pre-commit install;
echo "API_ID=coloque aqui seu api_id 
API_HASH=coloque aqui seu api_hash
BOT_TOKEN=coloque aqui seu bot_token
GROUP_ID=id do grupo que as mensagens devem ser enviadas" > .env
python3 run.py;
