# humle
Simple CMS build on Python Flask  

The basics are stolen from the Flask tutorial, and the setupis the same:  

python3 -m venv venv
. venv/bin/activate

pip install -e .

export FLASK_APP=flaskr
export FLASK_ENV=development
flask init-db
flask run
