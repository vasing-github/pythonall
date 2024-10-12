import threading
import queue
import time

# 创建一个队列
task_queue = queue.Queue()

# 定义一个工作线程函数
def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        print(f"Processing task: {task}\n")
        time.sleep(1)  # 模拟任务处理时间
        task_queue.task_done()

# 创建并启动多个工作线程
num_threads = 4
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

# 主程序往队列里添加任务
for i in range(10):
    task_queue.put(f"Task {i}")

# 等待所有任务完成
task_queue.join()

# 停止所有工作线程
for i in range(num_threads):
    task_queue.put(None)
for thread in threads:
    thread.join()

print("All tasks are processed.")
