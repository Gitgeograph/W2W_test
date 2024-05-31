cd W2W 
python -m venv venv
source venv/bin/activate
cd backend 
pip install r requirements.txt
py manage.py migrate
py manage.py loaddata tapp/fixtures/data.json
py manage.py runserver


cd frontend
npm install
npm start
