from api import app
import json
def test_start():
    with app.test_client() as c:
        response = c.get('/')
        data=json.loads(response.data)
        assert data['message']=='my diary'

def test_get_all_entries():

    with app.test_client() as c:
        response = c.get('/API/v1/index')
        data=json.loads(response.data)
        assert type(data) == dict
        assert data['entry'] !=None




def test_post_all_entries():
    with app.test_client() as c:
        
        data={
            "Entry":"preparations",
            "time":"6:00-8:00am"
        }
        response = c.post('/API/v1/index', json=data)
        assert type(data) == dict
        assert data['Entry'] != None  


def test_put_all_entries():
     with app.test_client() as c:
        data={
                "Entry":"church sessions",
                "time":"8:00-9:00am"
        }
        response = c.put('/API/v1/index', json = data)
        assert type(data) == dict
        assert data['Entry'] != None
