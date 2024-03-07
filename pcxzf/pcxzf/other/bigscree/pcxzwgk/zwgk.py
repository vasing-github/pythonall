# -*- coding: utf-8 -*-
from aiohttp import web
import datetime
import conf
import data_txt
import get_web_data
import asyncio
import json

news_num_dic = data_txt.news_num_dic


def modify_news_num_dic(new_dic):
    global news_num_dic
    news_num_dic = new_dic
async def save_web_data():
    with open('data_txt.py', 'w') as f:
        # 将字典转换为json字符串
        json_str = json.dumps(news_num_dic)
        # 将json字符串写入文件
        f.write('news_num_dic = ' + json_str + '\n')
# HTTP请求处理函数
async def handle_root(request):
    return web.Response(text="这是根路径")

async def handle_info(request):
    return web.Response(text="这是信息页面")

async def handle_data(request):
    # 假设这里有一些数据处理的逻辑
    data = news_num_dic
    # 返回一个json格式的响应
    return web.json_response(data)


# 初始化HTTP应用
async def init_app():
    app = web.Application()
    app.router.add_get('/', handle_root)
    app.router.add_get('/info', handle_info)
    app.router.add_get('/data', handle_data)
    return app

# 定时执行的爬虫任务
async def periodic_crawler():
    while True:
        # 获取当前时间
        now = datetime.datetime.now()

        if now.hour <= conf.first_hour and now.minute < conf.firt_minutes:
            next_time = now.replace(hour=conf.first_hour, minute=conf.firt_minutes, second=0, microsecond=0)
        elif now.hour <= conf.second_hour and now.minute < conf.sencond_minutes:
            next_time = now.replace(hour=conf.second_hour, minute=conf.sencond_minutes, second=0, microsecond=0)
        else:
            next_time = now.replace(hour=conf.third_hour, minute=conf.third_minutes, second=0, microsecond=0) + datetime.timedelta(days=1)
        # 计算等待时间
        wait_time = (next_time - now).total_seconds()
        print(wait_time)
        # 等待到下一个执行时间
        await asyncio.sleep(wait_time)
        # 这里是爬虫的逻辑
        print("爬虫任务执行")
        await get_all_data()


async def get_all_data():
    new_dic = await get_web_data.get_ywdt_num()
    all_gk_num = await get_web_data.get_all_gk_num()


    modify_news_num_dic(new_dic)

    await save_web_data()


# 主函数
async def main():
    # 启动HTTP服务
    runner = web.AppRunner(await init_app())
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8888)
    await site.start()
    print("HTTP服务已启动")

    # 启动定时爬虫任务
    asyncio.create_task(periodic_crawler())

    # 运行直到被取消
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())

