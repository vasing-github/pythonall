import base64
import json
import random
import time

from Crypto.Cipher import AES

def millisecond_to_time(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def format_str(c, a):
    l = ""
    k = len(str(c))
    if k > 0:
        if k + 2 > a:
            return str(c)
        else:
            g = a - k - 2
            h = 10 ** g
            b = random.randint(0, h - 1)
            f = len(str(b))
            if f < g:
                b = b * (10 ** (g - f))
            l += f"{k:02}" + str(c) + str(b)
    else:
        return str(c)
    return l


def encrypt(e):
    b = "bGVhcm5zcGFjZWFlczEyMw=="
    c = base64.b64decode(b).decode('utf-8')
    f = AES.new(c.encode('utf-8'), AES.MODE_ECB)
    padded_e = e + (16 - len(e) % 16) * chr(16 - len(e) % 16)
    d = f.encrypt(padded_e.encode('utf-8'))
    return base64.b64encode(d).decode('utf-8')


def gets(c, s, a, p):
    A = {
        "courseId": c,
        "endTime": s + a,
        "interval": True,
        "itemId": p,
        "playComplete": False,
        "position": s + a,
        "recordType": "interval",
        "startTime": s,
        "videoTotalTime": "00:39:32"
    }

    u = abs(A["endTime"] - A["startTime"])
    A["studyTimeLong"] = 0 if (u <= 1 and u > 0) else u
    A["startTimeStr"] = millisecond_to_time(A["startTime"] * 1000)
    A["endTimeStr"] = millisecond_to_time(A["endTime"] * 1000)

    x = {
        "courseId": A["courseId"],
        "itemId": A["itemId"],
        "time1": format_str(int(time.time() * 1000), 20),
        "time2": format_str(int(A["startTime"]), 20),
        "time3": format_str(36 * 60 + 6, 20),  # Convert "00:36:06" to seconds
        "time4": format_str(int(A["endTime"]), 20),
        "videoIndex": 0,
        "time5": format_str(A["studyTimeLong"], 20),
        "terminalType": 0,
        "recordType": A["recordType"]
    }

    s = encrypt(json.dumps(x))

    return s


if __name__ == '__main__':
    gets()
