import time
import conf
import requests
from threed_record import qm
from send import sendszpc

def testqm():
    final_dic = {'平昌县经济和信息化局': { '重大民生信息': ('2023-09-21', '全县新建5G基站146座                                            '), '其他法定信息': ('2023-04-20', '《四川省中小企业特色产业集群培育认定管理暂行办法》政策解读                                            ')}, '平昌县财政局': {'其他法定信息': ('2023-09-12', '平昌县财政局机关生活垃圾分类实施方案                                            ')}, '平昌县住房和城乡建设局': {'统计信息': ('2023-10-12', '2023年1-9月资金争取情况                                            '), '重大项目': ('2023-10-12', '2023年项目储备情况                                            ')}, '平昌县退役军人事务局': {'统计信息': ('2023-08-28', '2023年4月—6月退役军人建档立卡情况统计                                            '), '重大民生信息': ('2023-05-26', '平昌县退役军人及其他优抚对象统计情况                                            '), '其他法定信息': ('2023-07-14', '拥军优抚政策解读                                            ')}, '平昌县林业局': {'统计信息': ('2023-09-25', '平昌县林业发展情况统计                                            '), '重大项目': ('2023-09-25', '平昌县储备林建设项目正式启动                                            ')}, '平昌县医疗保障局': {'统计信息': ('2023-09-22', '关于2023年第八批居民、职工门诊特殊疾病认定结果的通知                                            '), '行政许可/处罚': ('2023-09-28', '关于同意将平昌县友邦药业有限公司金太阳光店等52家连锁定点零售药店纳入门诊统筹管理的公告                                            '), '其他法定信息': ('2023-09-21', '平昌县医疗保障局关于将巴中市普济医药连锁有限公司平昌三五三分店等16家诊所药店纳入医保协议定点管理的公示                                            ')}, '平昌县金宝街道办事处': {'其他法定信息': ('2023-09-22', '金宝街道烟花爆竹零售经营门店（2024-2025）布点规划方案                                            ')}, '平昌县岳家镇人民政府': {'统计信息': ('2023-10-07', '岳家镇新增入市项目储备库2个                                            ')}, '平昌县龙岗镇人民政府': {'统计信息': ('2023-08-29', '龙岗镇二季度蔬菜及特种作物生产统计表                                            ')}, '平昌县佛楼镇人民政府': {'其他法定信息': ('2023-09-22', '佛楼镇便民服务中心运行管理办法                                            ')}, '平昌县响滩镇人民政府': {'统计信息': ('2023-08-24', '响滩镇2023年大春经济作物种植面积统计表                                            '), '重大项目': ('2023-08-24', '响滩镇肉牛产业项目建设有序推进                                            ')}, '平昌县大寨镇人民政府': {'政府工作报告': ('2023-01-03', '大寨镇人民政府2023年政府工作报告                                            '), '统计信息': ('2023-08-24', '平昌县大寨镇医保缴费工作推进情况                                            '), '预算/决算': ('2023-01-12', '大寨镇2022年财政预算执行情况及2023年财政预算                                            '), '重大项目': ('2023-08-24', '平昌县大寨镇福申社区污水处理工程项目建设情况                                            ')}, '平昌县青云镇人民政府': {'统计信息': ('2023-10-10', '青云镇辣椒种植统计                                            '), '重大项目': ('2023-10-10', '金宝街道至青云道路改建工程道路建设                                            '), '重大民生信息': ('2023-10-10', '关于做好2024年度城乡居民基本医疗保险参保工作的通知                                            '), '其他法定信息': ('2023-10-10', '农村公益性岗位补贴申领办事指南                                            ')}, '平昌县澌岸镇人民政府': {'规划计划': ('2023-01-11', '2023年工作计划                                            ')}, '平昌县云台镇人民政府': {'统计信息': ('2023-08-24', '云台镇2023年5-8月安全工作开展情况统计                                            ')}, '平昌县岩口镇人民政府': {'重大项目': ('2023-07-18', '岩口镇2023年1—6月集体经济问效报表                                            ')}, '平昌县镇龙镇人民政府': {'统计信息': ('2023-09-25', '镇龙镇2023年上半年主要蔬菜作物播种面积统计                                            '), '重大项目': ('2023-09-25', '红旗水库除险加固工程基本竣工                                            ')}, '平昌县望京镇人民政府': {'统计信息': ('2023-07-25', '望京镇关于成立望京镇第五次全国经济普查领导小组的通知                                            '), '重大民生信息': ('2023-08-25', '望京镇2023年燃气煤气消防安全应急预案                                            ')}, '平昌县江家口镇人民政府': {'统计信息': ('2023-09-21', '江家口镇2023年度大春经济作物产量统计                                            '), '其他法定信息': ('2023-09-21', '江家口镇2023年春季雨露计划补助名单                                            ')}}

    tj_miss_year_dic = {'平昌县农业农村局': ['2020'], '平昌县商务局': ['2018', '2019'], '平昌县退役军人事务局': ['2018', '2019'], '平昌县市场监督管理局': ['2018', '2019', '2020'], '平昌县乡村振兴局': ['2020'], '平昌县信访局': ['2018', '2019', '2020'], '平昌县医疗保障局': ['2018', '2019', '2021', '2022'], '四川平昌经济开发区管理委员会': ['2018', '2019'], '平昌县金宝新区管理委员会': ['2018', '2019', '2020', '2021'], '平昌县金宝街道办事处': ['2018', '2019'], '平昌县龙岗镇人民政府': ['2019', '2020'], '平昌县佛楼镇人民政府': ['2021'], '平昌县响滩镇人民政府': ['2021'], '平昌县大寨镇人民政府': ['2018'], '平昌县驷马镇人民政府': ['2018', '2019', '2020', '2021'], '平昌县粉壁镇人民政府': ['2019', '2020'], '平昌县元山镇人民政府': ['2020'], '平昌县云台镇人民政府': ['2020', '2021', '2022'], '平昌县邱家镇人民政府': ['2019', '2021'], '平昌县泥龙镇人民政府': ['2018'], '平昌县岩口镇人民政府': ['2018', '2019', '2020'], '平昌县镇龙镇人民政府': ['2018', '2019', '2020']}
    no_content_list = [('平昌县交通运输局', '机关简介'), ('平昌县岳家镇人民政府', '机关简介')]
    missing_years_dict = {'平昌县商务局': ['2018年', '2019年'], '平昌县退役军人事务局': ['2018年', '2019年'], '平昌县信访局': ['2018年', '2019年'], '平昌县医疗保障局': ['2018年', '2019年'], '平昌县金宝街道办事处': ['2018年', '2019年'], '平昌县驷马镇人民政府': ['2020年'], '平昌县江家口镇人民政府': ['2018年', '2019年']}
    zc_over_list = [('平昌县商务局',
                     '平昌县财政局平昌县商务局关于印发《平昌县2021年国家级电子商务进农村综合示范建设项目专项资金使用管理办法》的通知                                            ',
                     '2023-03-07', 437),
                    ('平昌县审计局', '四川省审计整改结果公告办法                                            ', '2023-04-10', 403),
                    ('平昌县驷马镇人民政府', '驷马镇安全生产大提升专项行动工作方案                                            ', '2023-04-06', 407),
                    ('平昌县得胜镇人民政府',
                     '平昌县得胜镇人民政府关于印发《得胜镇丰收村2023年乡村振兴重点帮扶村工作方案》的通知                                            ',
                     '2023-05-12', 371)]

    # qm.add_item({conf.menu_over_update: final_dic})
    # qm.add_item({conf.miss_tj_year: tj_miss_year_dic})
    # qm.add_item({conf.zf_year_report: missing_years_dict})
    #
    # qm.add_item({conf.finish_score: None})


    qm.add_item({conf.zc_over_time: zc_over_list})
    qm.stop()

def testsendszpc():
    sendszpc.main()


def testliuyan():
    import requests

    cookies = {
        'rhts.session.id': '2016d806-4340-445b-94fe-36034b4d6e41',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # 'Content-Length': '0',
        # 'Cookie': 'rhts.session.id=2016d806-4340-445b-94fe-36034b4d6e41',
        'Origin': 'http://124.115.216.182:8181',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://124.115.216.182:8181/index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = requests.post('http://124.115.216.182:8181/sys/hint/refreshHint', cookies=cookies, headers=headers,
                             verify=False)
    print(response.text)

def testgethint():
    import requests

    cookies = {
        'rhts.session.id': '2016d806-4340-445b-94fe-36034b4d6e41',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'rhts.session.id=2016d806-4340-445b-94fe-36034b4d6e41',
        'Origin': 'http://124.115.216.182:8181',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://124.115.216.182:8181/train/train/list/1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'stime': '26',
    }

    response = requests.post('http://124.115.216.182:8181/sys/hint/getHint', cookies=cookies, headers=headers,
                             data=data, verify=False)
    print(response.text)


# if __name__ == '__main__':
#     # testqm()
#     testliuyan()
    # testgethint()

import requests

# from bs4 import BeautifulSoup # 在这个测试函数中不是必需的

# --- 您提供的 getproxies 函数 (稍作调整和增强以提高健壮性) ---
proxies_global_cache = None  # 使用不同的变量名以区分全局缓存和函数内局部变量


def getproxies(up=False):
    global proxies_global_cache  # 声明我们意图修改全局变量

    if up or proxies_global_cache is None:
        print("尝试从API获取新的代理IP...")
        # 提取代理API接口，获取1个代理IP
        api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=ogsq2949aa37recirws7&signature=46yif7scn2bueuoj85mkowbgq2p6rl7h&num=1&pt=1&sep=1&transferip=1"

        try:
            # 获取API接口返回的代理IP
            proxy_ip_response = requests.get(api_url, verify=False, timeout=15)  # 增加超时
            proxy_ip_response.raise_for_status()  # 如果API返回错误状态码 (如403, 500等)，则抛出异常
            proxy_ip_text = proxy_ip_response.text.strip()

            if not proxy_ip_text or ':' not in proxy_ip_text:  # 简单检查返回的是否为空或格式不像 ip:port
                print(f"错误：从API获取的代理IP无效或格式不正确: '{proxy_ip_text}'")
                # 如果之前有缓存的代理，可以考虑返回旧的，或者彻底失败
                if proxies_global_cache:
                    print("警告：获取新代理失败，将尝试使用之前缓存的代理。")
                    return proxies_global_cache
                return None  # 没有有效代理可返回

            print(f"API成功返回代理IP: {proxy_ip_text}")

        except requests.exceptions.RequestException as e:
            print(f"错误：从代理API接口获取IP失败: {e}")
            # 如果之前有缓存的代理，可以考虑返回旧的，或者彻底失败
            if proxies_global_cache:
                print("警告：获取新代理失败，将尝试使用之前缓存的代理。")
                return proxies_global_cache
            return None  # 没有有效代理可返回

        # 用户名密码认证(私密代理/独享代理)
        username = "d4036946853"
        password = "zn1ehshu"

        # 构建新的代理配置
        current_proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip_text},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip_text}
        }
        proxies_global_cache = current_proxies  # 更新全局缓存
        print(f"代理已更新: {proxies_global_cache}")
        return proxies_global_cache
    else:
        print(f"使用已缓存的代理: {proxies_global_cache}")
        return proxies_global_cache


# --- 测试代理访问的函数 ---
def test_proxy_accessibility():
    print("开始代理可访问性测试...")

    # 强制获取一个新的代理进行测试
    current_proxy_config = getproxies(up=True)

    if not current_proxy_config:
        print("错误：未能获取到有效的代理配置。测试中止。")
        return

    print(f"\n将使用以下代理进行测试: {current_proxy_config}")

    urls_to_test = [
        {"name": "百度 (Baidu)", "url": "https://www.baidu.com"},
        {"name": "谷歌 (Google)", "url": "https://www.google.com"},
        {"name": "目标网站页面 (sc.gov.cn specific page)",
         "url": "https://www.sc.gov.cn/10462/zcwjk/zcwjk.shtml?title=%E3%80%8A%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%AE%89%E5%85%A8%E7%94%9F%E4%BA%A7%E6%B3%95%E3%80%8B"},
        {"name": "目标网站首页 (sc.gov.cn base)", "url": "https://www.sc.gov.cn/"}
    ]

    # 通用请求头，模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for item in urls_to_test:
        name = item["name"]
        url = item["url"]
        print(f"\n--- 正在测试访问: {name} ({url}) ---")
        try:
            # verify=True 是 requests 的默认行为，确保对目标服务器的SSL验证
            response = requests.get(url, proxies=current_proxy_config, headers=headers, timeout=20)
            print(f"成功: {name} - 状态码: {response.status_code}")
            # 可以选择打印少量返回内容以确认
            # print(f"  响应内容前100字符: {response.text[:100].replace('\n', ' ')}")
        except requests.exceptions.ProxyError as e:
            print(f"代理错误: {name} - 无法通过代理连接。错误详情: {e}")
        except requests.exceptions.ConnectTimeout as e:
            print(f"连接超时: {name} - 连接目标服务器或代理超时。错误详情: {e}")
        except requests.exceptions.ReadTimeout as e:
            print(f"读取超时: {name} - 从服务器读取数据超时。错误详情: {e}")
        except requests.exceptions.SSLError as e:
            print(f"SSL错误: {name} - SSL证书验证失败 (可能是代理问题或目标服务器配置问题)。错误详情: {e}")
        except requests.exceptions.ConnectionError as e:  # 更通用的连接错误
            print(f"连接错误: {name} - 发生连接错误。错误详情: {e}")
        except requests.exceptions.RequestException as e:  # requests库的其他异常
            print(f"请求失败: {name} - 发生 'requests' 相关错误。错误详情: {e}")
        except Exception as e:  # 捕获其他所有意外错误
            print(f"未知错误: {name} - 发生未知错误。错误详情: {e}")


# --- 主程序入口 ---
if __name__ == '__main__':
    test_proxy_accessibility()