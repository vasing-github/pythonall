import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import threading

stop_pingjia = False

def pingjia(num):
    url = 'http://hcp.sczwfw.gov.cn/app/api/evaluationFileHandler'
    headers ={'Accept':'application/json, text/plain, */*',
    'Host':'hcp.sczwfw.gov.cn',
    'Origin':'http://hcp.sczwfw.gov.cn',
    'Referer': 'http://hcp.sczwfw.gov.cn/appEval/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

    files = {'content':(None,'{"anonymous":1,"busiCode":"'+num+'","evalChannel":"3","evalSource":"2","objType":"2","evaluationChildren":[],"instructions":"","objCode":"code-001","praise":[],"publish":1,"score":5,"maxBadClassifyFlag":""}')}

    r = requests.post(url, files=files)

    return r.text
def beforePIngjia1(num):
    url = 'https://hcp.sczwfw.gov.cn/app/api/evaluate/evalExpandQueryHandler'
    headers = {'Accept': 'application/json, text/plain, */*',
               'Host': 'hcp.sczwfw.gov.cn',
               'Origin': 'http://hcp.sczwfw.gov.cn',
               'Referer': 'http://hcp.sczwfw.gov.cn/appEval/index.html',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    data={
        'busiCode': num,
        'objCode':"code-001"
    }

    r = requests.post(url, data=data)


def beforePIngjia2(num):
    url = 'https://hcp.sczwfw.gov.cn/app/api/evaluate/evalIsEvaluation'
    headers = {'Accept': 'application/json, text/plain, */*',
               'Host': 'hcp.sczwfw.gov.cn',
               'Origin': 'http://hcp.sczwfw.gov.cn',
               'Referer': 'http://hcp.sczwfw.gov.cn/appEval/index.html',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    data = {
        'busiCode': num,
        'objCode': "code-001"
    }

    r = requests.post(url, data=data)
def start_pingjia():
    global stop_pingjia
    stop_pingjia = False
    date = date_entry.get()
    if int(date) > 20240925:
        messagebox.showinfo("提示", "代理池已耗尽")
        return
    for i in range(1, 2001):
        if stop_pingjia:
            break
        num = "511923-" + date + "-" + str(i).zfill(6)
        response_text = pingjia(num)
        status_text.insert(tk.END, "当前评价条数: " + str(i) + "\n")
        status_text.insert(tk.END, "请求回复: " + response_text + "\n")
        status_text.see(tk.END)
        root.update_idletasks()

def start_thread():
    thread = threading.Thread(target=start_pingjia)
    thread.start()

def stop():
    global stop_pingjia
    stop_pingjia = True

root = tk.Tk()
root.title("自动评价")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

date_entry = ttk.Entry(mainframe, width=10)
date_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="日期").grid(column=1, row=1, sticky=tk.W)
ttk.Button(mainframe, text="开始评价", command=start_thread).grid(column=3, row=3, sticky=tk.W)
ttk.Button(mainframe, text="停止评价", command=stop).grid(column=4,row=3)

status_text = tk.Text(mainframe)
status_text.grid(column=1, row=4, columnspan=3)

scrollbar = ttk.Scrollbar(mainframe, command=status_text.yview)
scrollbar.grid(column=4, row=4, sticky=(tk.N, tk.S))
status_text["yscrollcommand"] = scrollbar.set

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

date_entry.focus()
root.bind("<Return>", start_thread)

root.mainloop()
