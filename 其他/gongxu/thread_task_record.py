
import queue
import threading
import time

import takerecord

class QueueManager:
    def __init__(self, num_threads):
        self.q = queue.Queue()
        self.threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=self.listen_queue)
            thread.daemon = True
            thread.start()
            self.threads.append(thread)

    def listen_queue(self):
        while True:
            item = self.q.get()
            if item is None:
                break
            self.process_item(item)
            self.q.task_done()

    def add_item(self, item):
        self.q.put(item)

    def stop_threads(self):
        self.q.join()
        for _ in self.threads:
            self.q.put(None)
        for thread in self.threads:
            thread.join()

    def process_item(self,item):
        # print(item)
        takerecord.takeRecode2(item[2], '%.4f' % (item[0]))
        time.sleep(1)
        takerecord.takeRecode2(item[2], '%.4f' % (item[0]+30))
        time.sleep(1)
        takerecord.takeRecode2(item[2], '%.4f' % (item[0] + 60))
        time.sleep(1)
        takerecord.takeRecode2(item[2], '%.4f' % (item[0] + 90))
        time.sleep(1)
        takerecord.takeRecode2(item[2], '%.4f' % (item[0] + 100))



# 使用示例
qm = QueueManager(num_threads=2)
# for i in range(10):
#     queue_manager.add_item(f"Task {i}")

# 等待所有任务完成

# qm.stop_threads()
