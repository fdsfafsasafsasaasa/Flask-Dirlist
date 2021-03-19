apt install -y python3 python3-pip git

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

git clone --depth 1 https://github.com/thewarsawpakt/Flask-Dirlist

python3 Flask-Dirlist/main.py