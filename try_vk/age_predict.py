import requests
from datetime import date

domain = "https://api.vk.com/method"
access_token = '3400cd01a5c5949a33c0d5e7f11070d4f4bc7226e6e6062840f317c00f59b1d4cf156db73cd034db2c541'


def send_query(action, query_params):
    query = domain + "/" + action \
            + "?access_token=" + access_token

    for key, value in query_params.items():
        query += "&" + key + "=" + value
    return requests.get(query)


def age_predict(user_id):
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"

    response = send_query("friends.get", {"user_id": str(user_id), "fields": "bdate"})
    j = response.json()
    sum = 0
    num = 0
    for person in response.json()['response']:
        if 'bdate' in person.keys():
            d = [int(i) for i in person['bdate'].split('.')]
            if len(d) == 3 and d[2] > 1990:
                today = date.today()
                person_time = today - date(d[2], d[1], d[0])
                sum += person_time.days // 365
                num += 1
    return sum / num


if __name__ == '__main__':
    response = send_query("friends.get", {"order": "name", "fields": "sex"})

    j = response.json()
    for p in j['response']:
        if p['last_name'] == 'Головин':
            print(age_predict(p['uid']))
