from src.models import *

def test_user_model():
    test_user = User(user_id=1, username='Test', email='dhalstea@uncc.edu', passkey='password123', pfp='defaultuser.png')
    assert test_user.username == 'Test'
    assert test_user.email == 'jsasser5.edu'
    assert test_user.passkey == 'password123'

   
