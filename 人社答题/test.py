import hashlib
import time
import cofig
def check_md5(input_string, md5_hash):
    # 计算输入字符串的MD5哈希值
    shijianchuo = str(int(time.time() * 1000))
    input_string = input_string + str(shijianchuo)
    hash_object = hashlib.md5(input_string.encode())
    generated_hash = hash_object.hexdigest()
    print(generated_hash)
    # 比较生成的哈希值和给定的哈希值
    if generated_hash == md5_hash:
        return True
    else:
        return False

# # 测试函数
# input_string = 'oVqGH69wz29MD_Ex-_2w2PLntdEw'
# md5_hash = '0b1qjFGa1TX92G0aEeJa1r1mJL0qjFGC'
# print(check_md5(input_string, md5_hash))

if 760374 in cofig.playersid:
    print('yes')
shijianchuo='1694998715'
radom_number = 'Nmj9I3Tf2a3VRJ4A'
sign = hashlib.md5((hashlib.md5((shijianchuo ).encode()).hexdigest() +  radom_number).encode()).hexdigest(),
print(sign)