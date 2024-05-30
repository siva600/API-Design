import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/"
ENDPOINT_status = "status/"
AUTH_ENDPOINT = BASE_URL + ENDPOINT_status + "/auth/jwt/"


def do(method='get', data=None, is_json=True):
    data = {} if data is None else data
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, BASE_URL + ENDPOINT_status, data=data, headers=headers)
    # + "?id=" + str(id),
    print(r.text)
    print(r.status_code)
    return r


def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()

    for item in data:
        if item['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(item['id']))
            # print(r2.json())

    return data


def create_update():
    new_data = {
        'user': 1,
        'content': "Another user siva Update"
    }
    r = requests.post(BASE_URL + ENDPOINT + "1/", data=new_data)
    # print(r.status_code)
    # print(r.headers)
    if r.status_code in range(200, 299):
        return r.json()
    return r.text


def do_obj_update():
    new_data = {
        'content': "This is updated user Update using put method"
    }
    r = requests.put(BASE_URL + ENDPOINT)
    # + "1/", data = json.dumps(new_data)
    print(r.status_code)
    if r.status_code in range(200, 299):
        return r.json()
    return r.text


get_endpoint = BASE_URL + ENDPOINT_status + str(15)



# get response without auth..
r = requests.get(get_endpoint)
print(r.text)

r2 = requests.get(get_endpoint)
print(r2.status_code)

post_headers = {
    'content-type': 'application/json'
}

data = {
    'username': '<>',
    'password': '<>',

}

# code with auth
r3 = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers= post_headers)
token = r.json()['token']
print(token)

headers = {
    # "Content-Type": "application/json",
    "Authorization": "JWT" + token,
}

data = {
    "content": "updated description"
}
post_data = json.dumps({"content": "Random content"})
post_response = requests.post(BASE_URL + ENDPOINT_status, data=post_data, headers=headers)
print(post_response.text)



# print(get_list())
# print(create_update())

# print(do_obj_update())

# do(data={'id': 54})
# do(method='delete', data={'id': 1})
# do(method='put', data={'id': 15, "content": "Coo lcontent ffrom user", 'user': 1})
# do(method='post', data={'content': "data dfrom pure_api user.", "user": 1})

