# -*- coding: utf-8 -*-
import conf
import asyncio
import re


async def get_ywdt_num():
    return await get_news_num_dic(conf.ywdt_dic)

async def count_a(count,href):
    a = await get_num(href)
    if isinstance(a, str):
        a = int(a)
    count = count + a


async def get_all_gk_num():
    count = 0
    # 要闻动态计数
    for href in conf.ywdt_dic.values():
        await count_a(count, href)

    # 基础信息公开计数
    for href in conf.jichu_dic.values():
        await count_a(count, href)

    # 重点领域不跳转部分计数
    for href in conf.height_area_with_total_dic.values():
        await count_a(count, href)

    # 专题专栏部分激素
    for href in conf.zhuanti_total_list:
        await count_a(count, href)
    print('count',count)
    return count
async def get_num(href):
    response, soup = conf.make_request_get(href)
    print(href)
    scripts = soup.find_all("script")
    for script in scripts:
        if script.string is not None:
            if 'Ls.pagination' in script.string:
                pattern = re.compile(r"total: (\d+)")
                total_match = pattern.search(script.string)
                if total_match:
                    total = total_match.group(1)
                    print(total)
                    return total

                else:
                    page_count_match = re.search(r'pageCount:(\d+)', script.string)
                    if page_count_match:
                        page_count = page_count_match.group(1)
                        return page_count * 18

async def get_news_num_dic(dic):
    news_num_dic = {}
    for menu, href in dic.items():
        news_num_dic[menu] = await get_num(href)

    return news_num_dic


async def main():
    # await get_ywdt_num()
    await get_all_gk_num()


if __name__ == '__main__':
    asyncio.run(main())