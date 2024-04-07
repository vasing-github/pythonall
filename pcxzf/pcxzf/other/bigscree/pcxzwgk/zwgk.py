# -*- coding: utf-8 -*-
from aiohttp import web
import datetime
import conf
import data_txt
import get_web_data
import asyncio
import json
import aiohttp_cors

news_num_dic = data_txt.news_num_dic
all_gk_num = data_txt.all_gk_num
day_week_mon_dic = data_txt.day_week_mon_dic
jczwgk_dic = data_txt.jczwgk_dic
zhuanti_of = data_txt.zhuanti_of
hight_area_dic = data_txt.hight_area_dic
alljcgk = data_txt.alljcgk

def modify_news_num_dic(new_dic, new_all_gk_num, new_day_week_mon_dic, new_jczwgk_dic, new_zhuanti_of, new_hight_area_dic,new_alljcgk):
    global news_num_dic, all_gk_num, day_week_mon_dic,jczwgk_dic, zhuanti_of, hight_area_dic,alljcgk

    news_num_dic = new_dic
    all_gk_num = new_all_gk_num
    day_week_mon_dic = new_day_week_mon_dic
    jczwgk_dic = new_jczwgk_dic
    zhuanti_of = new_zhuanti_of
    hight_area_dic = new_hight_area_dic
    alljcgk = new_alljcgk


async def save_web_data():
    global news_num_dic, all_gk_num, day_week_mon_dic,jczwgk_dic, zhuanti_of, hight_area_dic,alljcgk
    with open('data_txt.py', 'w', encoding='utf-8') as f:

        json_str = json.dumps(news_num_dic, ensure_ascii=False)
        f.write('news_num_dic = ' + json_str + '\n')

        json_str = json.dumps(all_gk_num, ensure_ascii=False)
        f.write('all_gk_num = ' + json_str + '\n')

        json_str = json.dumps(day_week_mon_dic, ensure_ascii=False)
        f.write('day_week_mon_dic = ' + json_str + '\n')

        json_str = json.dumps(jczwgk_dic, ensure_ascii=False)
        f.write('jczwgk_dic = ' + json_str + '\n')

        json_str = json.dumps(zhuanti_of, ensure_ascii=False)
        f.write('zhuanti_of = ' + json_str + '\n')

        json_str = json.dumps(hight_area_dic, ensure_ascii=False)
        f.write('hight_area_dic = ' + json_str + '\n')

        f.write('alljcgk = ' + str(alljcgk) + '\n')

        f.write("time = '" + str(datetime.datetime.now()) + "'\n")


# HTTP请求处理函数
async def handle_root(request):
    return web.Response(text="这是根路径")


async def handle_checkpa(request):
    dic = {}
    dic['time'] = data_txt.time
    dic['prox_num'] = conf.prox_num
    a = all_gk_num.get('基础信息') + all_gk_num.get('要闻动态') + all_gk_num.get('重点领域1') + all_gk_num.get(
        '所有政府信息') + all_gk_num.get('专题专栏') + alljcgk
    dic['all_num'] = a
    return web.json_response(dic)


async def handle_pa(request):
    asyncio.create_task(get_all_data())
    return web.Response(text="Crawler started")


async def handle_zhuanti(request):
    return web.json_response(zhuanti_of)


async def handle_height(request):
    return web.json_response(hight_area_dic)


async def handle_data(request):
    return web.json_response(jczwgk_dic)


async def handle_midddle_data(request):
    middle_data_dic = {}
    middle_data_dic['平昌要闻'] = int(news_num_dic.get('平昌要闻'))
    middle_data_dic['基层动态'] = int(news_num_dic.get('基层动态'))
    middle_data_dic['部门工作'] = int(news_num_dic.get('部门工作'))
    middle_data_dic['基础信息'] = all_gk_num.get('基础信息')
    middle_data_dic['重点领域'] = all_gk_num.get('重点领域1') + all_gk_num.get('重点领域2')

    return web.json_response(middle_data_dic)


async def handle_getallgk(request):
    a = all_gk_num.get('基础信息') + all_gk_num.get('要闻动态') + all_gk_num.get('重点领域1') + all_gk_num.get('所有政府信息') + all_gk_num.get('专题专栏') + alljcgk
    return web.json_response(a)


async def handle_getdayweekmon(request):
    new_dic = {}
    new_dic['今日'] = day_week_mon_dic['当天'] + all_gk_num['当天政府信息']
    new_dic['本周'] = day_week_mon_dic['本周'] + all_gk_num['本周政府信息']
    new_dic['本月'] = day_week_mon_dic['本月'] + all_gk_num['本月政府信息']
    new_dic['公示公告'] = news_num_dic['公示公告']
    new_dic['热点关注'] = news_num_dic['热点关注']

    return web.json_response(new_dic)


# 初始化HTTP应用
async def init_app():
    app = web.Application()

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })

    # 添加CORS支持的路由
    cors.add(app.router.add_route("GET", '/', handle_root))
    cors.add(app.router.add_route("GET", '/zhuanti', handle_zhuanti))
    cors.add(app.router.add_route("GET", '/height', handle_height))
    cors.add(app.router.add_route("GET", '/jiceng', handle_data))
    cors.add(app.router.add_route("GET", '/middledata', handle_midddle_data))
    cors.add(app.router.add_route("GET", '/getallgk', handle_getallgk))
    cors.add(app.router.add_route("GET", '/getdayweekmon', handle_getdayweekmon))
    cors.add(app.router.add_route("GET", '/pa', handle_pa))
    cors.add(app.router.add_route("GET", '/checkpa', handle_checkpa))
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
        # await asyncio.wait_for(get_all_data(), timeout=wait_time)

        # 这里是爬虫的逻辑
        print("爬虫任务执行")
        # await get_all_data()


async def get_all_data():
    conf.prox_num = 0

    new_dic = await get_web_data.get_ywdt_num()
    all_gk_num = await get_web_data.get_all_gk_num()
    day_week_mon_dic = await get_web_data.get_day_week_mon_dic()
    jczwgk_dic,alljcgk = await get_web_data.get_jczwgk_dic()
    zhuanti_of = await get_web_data.get_zhuanti_of()
    hight_area_dic = await get_web_data.get_height_area()

    modify_news_num_dic(new_dic,all_gk_num,day_week_mon_dic,jczwgk_dic,zhuanti_of,hight_area_dic,alljcgk)

    await save_web_data()


# 主函数
async def main():
    # 启动HTTP服务
    runner = web.AppRunner(await init_app())
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8888)
    await site.start()
    print("HTTP服务已启动")
    # 运行直到被取消
    await asyncio.Event().wait()

if __name__ == '__main__':
    asyncio.run(main())

