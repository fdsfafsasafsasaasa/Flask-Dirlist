apt install -y python3 python3-pip python3-venv git

python3 -m venv venv

source venv/bin/activate

git clone --depth 1 https://github.com/thewarsawpakt/Flask-Dirlist

pip install -r Flask-Dirlistrequirements.txt

python3 Flask-Dirlist/main.py