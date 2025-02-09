import time
import requests

start = time.time()

response = requests.post(
    "https://api.deepseek.com/v1/chat/completions",
    headers={"Authorization": "Bearer sk-8e77dafc16d743149491c69daabe0c77"},
    json={
        "model": "deepseek-coder",  # 添加 model 字段
        "messages": [{"role": "user", "content": "给我一个修改pdf文件的python代码"}]
    }
)

print(f"API响应时间: {time.time()-start:.2f}s")
print(response.text)