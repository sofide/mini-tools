import requests


for i in range(1000):
    user_id = 'f' * 8 + str(i).rjust(8, '0')
    response = requests.post('http://pyconar-talks.fiqus.com/api/scores',
                             json={'score': {'score': 5, 'talk_id': 4, 'user_id': user_id}})

    print(user_id, response.status_code, response.content)
