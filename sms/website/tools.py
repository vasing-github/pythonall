import base64
import json
import requests
import random
from hashlib import md5

def base64_api(img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": 'vasing', "password": 'vas9624', "typeid": 3, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

def randomNum():
    seed = "0123456789"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    return ''.join(sa)
def randomNum2():
    seed = "01"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    return ''.join(sa)
def randomNumchart():
    seed = "0123456789qwertyuioplkjhgfdsazxcvbnm"
    sa = []
    for i in range(32):
        sa.append(random.choice(seed))
    return ''.join(sa)
def toolmd5(t):
    return md5(t.encode()).hexdigest()

def generate_uuid(length=None, radix=None):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    uuid = [None]*36
    radix = len(chars) if radix is None else radix
    if length is not None:
        return ''.join(random.choice(chars[:radix]) for _ in range(length))
    else:
        for i in range(36):
            if not uuid[i]:
                r = random.randint(0, 16)
                uuid[i] = chars[(r & 0x3) | 0x8] if i==19 else chars[r]
        uuid[8] = uuid[13] = uuid[18] = uuid[23] = '-'
        uuid[14] = '4'
        return ''.join(uuid)