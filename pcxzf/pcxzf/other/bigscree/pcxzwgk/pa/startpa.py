import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def startpa():
    return await fetch('http://222.215.24.208:8888/pa')

async def startredis():
    return await fetch('http://222.215.24.208:8888/minipa')

async def main():
    # 创建两个协程任务
    task1 = asyncio.create_task(startpa())
    task2 = asyncio.create_task(startredis())

    # 并发执行两个任务
    responses = await asyncio.gather(task1, task2)
    print(responses)

# 运行主函数
if __name__ == '__main__':
    asyncio.run(main())
