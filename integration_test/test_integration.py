import requests
from web import app

def test_basic_request():
    r = requests.get('http://127.0.0.1:5000/')
    assert r.status_code == 200


def test_login_required_when_logged_out():
	with app.test_client() as client:
		response = client.get('/add')
		assert response.status_code == 302

		response = client.get('/user/lionel_messi')
		assert response.status_code == 302

def test_login_required_when_logged_in():
	with app.test_client() as client:
		username = 'tanhakate'	
		password = '123456'
		data = dict(username=username, password=password)
		response = client.post('/login', data=data)
		assert response.status_code == 302
		assert 'tanhakate' in response.headers['Location']

		#response = client.get('/add')
		#assert response.status_code == 200

		response = client.get('/user/tanhakate') #valid username
		assert response.status_code == 200