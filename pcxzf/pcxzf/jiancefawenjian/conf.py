import datetime

import requests
from bs4 import BeautifulSoup
from openpyxl.styles import Font

bumen_Mennu_list = {'平昌县人民政府办公室': {'机关简介': '/public/column/6601841?type=4&action=list&nav=2&sub=0&catId=6715701', '规划计划': '/public/column/6601841?type=4&action=list&nav=2&sub=1&catId=6715721', '统计信息': '/public/column/6601841?type=4&action=list&nav=2&sub=2&catId=6715731', '行政许可/服务事项': '/public/column/6601841?type=4&action=list&nav=2&sub=3&catId=6717261', '行政处罚/行政强制': '/public/column/6601841?type=4&action=list&nav=2&sub=4&catId=6717245', '预算/决算': 'http://www.scpc.gov.cn/ztzl/pcxczyjsgk/index.html', '价格信息': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/jghsf/index.html', '收费项目': 'http://www.scpc.gov.cn/public/column/6601981?type=4&action=list&nav=2&sub=5&catId=6715921', '政府采购': '/public/column/6601841?type=4&action=list&nav=2&sub=8&catId=6715771', '重大项目': '/public/column/6601841?type=4&action=list&nav=2&sub=9&catId=6715781', '重大民生信息': '/public/column/6601841?type=4&action=list&nav=2&sub=10&catId=6715791', '招考录用': 'http://www.scpc.gov.cn/public/column/6602001?type=4&action=list&nav=2&sub=6&catId=6715941', '政府工作报告': '/public/column/6601841?type=4&action=list&nav=2&sub=12&catId=6716271', '建议/提案': 'http://www.scpc.gov.cn/hdjl/ytabl/index.html', '其他法定信息': '/public/column/6601841?type=4&action=list&nav=2&sub=14&catId=6715811'}, '平昌县发展和改革局': {'机关简介': '/public/column/6601861?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6601861?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6601861?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6601861?type=4&action=list&nav=2&sub=3&catId=6715891', '重大项目': '/public/column/6601861?type=4&action=list&nav=2&sub=4&catId=6715921', '其他法定信息': '/public/column/6601861?type=4&action=list&nav=2&sub=5&catId=6715951'}, '平昌县经济和信息化局': {'机关简介': '/public/column/6601881?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6601881?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6601881?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6601881?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6601881?type=4&action=list&nav=2&sub=4&catId=6715901', '其他法定信息': '/public/column/6601881?type=4&action=list&nav=2&sub=5&catId=6715951'}, '平昌县教育科技局': {'机关简介': '/public/column/6601901?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6601901?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6601901?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6601901?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6601901?type=4&action=list&nav=2&sub=4&catId=6715901', '教育科技': '/public/column/6601901?type=4&action=list&nav=2&sub=5&catId=6715921', '其他法定信息': '/public/column/6601901?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县公安局': {'机关简介': '/public/column/6601921?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6601921?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6601921?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6601921?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6601921?type=4&action=list&nav=2&sub=4&catId=6715901', '其他法定信息': '/public/column/6601921?type=4&action=list&nav=2&sub=5&catId=6715951'}, '平昌县民政局': {'机关简介': '/public/column/6601941?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6601941?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6601941?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6601941?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6601941?type=4&action=list&nav=2&sub=4&catId=6715901', '养老服务': '/public/column/6601941?type=4&action=list&nav=2&sub=5&catId=6715921', '社会救助': '/public/column/6601941?type=4&action=list&nav=2&sub=6&catId=6715931', '其他法定信息': '/public/column/6601941?type=4&action=list&nav=2&sub=7&catId=6715951'}, '平昌县司法局': {'机关简介': '/public/column/6601961?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6601961?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6601961?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6601961?type=4&action=list&nav=2&sub=3&catId=6715891', '司法监督': '/public/column/6601961?type=4&action=list&nav=2&sub=4&catId=6715921', '其他法定信息': '/public/column/6601961?type=4&action=list&nav=2&sub=5&catId=6715951'}, '平昌县财政局': {'机关简介': '/public/column/6601981?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6601981?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6601981?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6601981?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6601981?type=4&action=list&nav=2&sub=4&catId=6715921', '其他法定信息': '/public/column/6601981?type=4&action=list&nav=2&sub=5&catId=6715951'}, '平昌县人力资源和社会保障局': {'机关简介': '/public/column/6602001?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602001?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602001?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602001?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602001?type=4&action=list&nav=2&sub=4&catId=6715901', '就业创业': '/public/column/6602001?type=4&action=list&nav=2&sub=5&catId=6715921', '社会保障': '/public/column/6602001?type=4&action=list&nav=2&sub=6&catId=6715931', '招考录用': '/public/column/6602001?type=4&action=list&nav=2&sub=7&catId=6715941', '其他法定信息': '/public/column/6602001?type=4&action=list&nav=2&sub=8&catId=6715951'}, '平昌县自然资源和规划局': {'机关简介': '/public/column/6602021?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602021?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602021?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602021?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602021?type=4&action=list&nav=2&sub=4&catId=6715901', '重大项目': '/public/column/6602021?type=4&action=list&nav=2&sub=5&catId=6715921', '其他法定信息': '/public/column/6602021?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县住房和城乡建设局': {'机关简介': '/public/column/6602041?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602041?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602041?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602041?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602041?type=4&action=list&nav=2&sub=4&catId=6715901', '价格信息': '/public/column/6602041?type=4&action=list&nav=2&sub=5&catId=6715911', '重大项目': '/public/column/6602041?type=4&action=list&nav=2&sub=6&catId=6715921', '住房保障': '/public/column/6602041?type=4&action=list&nav=2&sub=7&catId=6715931', '其他法定信息': '/public/column/6602041?type=4&action=list&nav=2&sub=8&catId=6715951'}, '平昌县交通运输局': {'机关简介': '/public/column/6602061?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602061?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602061?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602061?type=4&action=list&nav=2&sub=3&catId=6715891', '重大项目': '/public/column/6602061?type=4&action=list&nav=2&sub=4&catId=6715921', '行政权力': '/public/column/6602061?type=4&action=list&nav=2&sub=5&catId=6715931', '其他法定信息': '/public/column/6602061?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县水利局': {'机关简介': '/public/column/6602081?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602081?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602081?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602081?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602081?type=4&action=list&nav=2&sub=4&catId=6715901', '重大项目': '/public/column/6602081?type=4&action=list&nav=2&sub=5&catId=6715921', '其他法定信息': '/public/column/6602081?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县农业农村局': {'机关简介': '/public/column/6602101?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602101?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602101?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602101?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602101?type=4&action=list&nav=2&sub=4&catId=6715901', '涉农补贴': '/public/column/6602101?type=4&action=list&nav=2&sub=5&catId=6715911', '重大项目': '/public/column/6602101?type=4&action=list&nav=2&sub=6&catId=6715921', '农产品价格监测': '/public/column/6602101?type=4&action=list&nav=2&sub=7&catId=6715931', '其他法定信息': '/public/column/6602101?type=4&action=list&nav=2&sub=8&catId=6715951'}, '平昌县商务局': {'机关简介': '/public/column/6602121?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602121?type=4&action=list&nav=2&sub=1&catId=6715861', '价格监测': '/public/column/6602121?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602121?type=4&action=list&nav=2&sub=3&catId=6715891', '其他法定信息': '/public/column/6602121?type=4&action=list&nav=2&sub=4&catId=6715951'}, '平昌县文化广播电视体育和旅游局': {'机关简介': '/public/column/6602141?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602141?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602141?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602141?type=4&action=list&nav=2&sub=3&catId=6715891', '公共文化服务': '/public/column/6602141?type=4&action=list&nav=2&sub=4&catId=6715921', '行政权力': '/public/column/6602141?type=4&action=list&nav=2&sub=5&catId=6715931', '其他法定信息': '/public/column/6602141?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县卫生健康局': {'机关简介': '/public/column/6602161?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602161?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602161?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602161?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602161?type=4&action=list&nav=2&sub=4&catId=6715901', '卫生健康': '/public/column/6602161?type=4&action=list&nav=2&sub=5&catId=6715931', '其他法定信息': '/public/column/6602161?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县退役军人事务局': {'机关简介': '/public/column/6602181?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602181?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602181?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602181?type=4&action=list&nav=2&sub=3&catId=6715891', '其他法定信息': '/public/column/6602181?type=4&action=list&nav=2&sub=4&catId=6715951'}, '平昌县应急管理局': {'机关简介': '/public/column/6602201?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602201?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602201?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602201?type=4&action=list&nav=2&sub=3&catId=6715891', '应急管理': '/public/column/6602201?type=4&action=list&nav=2&sub=4&catId=6715921', '监测预警': '/public/column/6602201?type=4&action=list&nav=2&sub=5&catId=6715931', '其他法定信息': '/public/column/6602201?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县审计局': {'机关简介': '/public/column/6602221?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602221?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602221?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602221?type=4&action=list&nav=2&sub=3&catId=6715891', '审计监督': '/public/column/6602221?type=4&action=list&nav=2&sub=4&catId=6715931', '其他法定信息': '/public/column/6602221?type=4&action=list&nav=2&sub=5&catId=6715951'}, '平昌县市场监督管理局': {'机关简介': '/public/column/6602241?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602241?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602241?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602241?type=4&action=list&nav=2&sub=3&catId=6715891', '市场监管': '/public/column/6602241?type=4&action=list&nav=2&sub=4&catId=6715931', '其他法定信息': '/public/column/6602241?type=4&action=list&nav=2&sub=5&catId=6715951'}, '巴中市平昌生态环境局': {'机关简介': '/public/column/6602261?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602261?type=4&action=list&nav=2&sub=1&catId=6715861', '执法检查': '/public/column/6602261?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602261?type=4&action=list&nav=2&sub=3&catId=6715891', '环评公示': '/public/column/6602261?type=4&action=list&nav=2&sub=4&catId=6715911', '环保督察': '/public/column/6602261?type=4&action=list&nav=2&sub=5&catId=6715921', '环境质量公报': '/public/column/6602261?type=4&action=list&nav=2&sub=6&catId=6715931', '其他法定信息': '/public/column/6602261?type=4&action=list&nav=2&sub=7&catId=6715951'}, '平昌县统计局': {'机关简介': '/public/column/6602281?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602281?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602281?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602281?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602281?type=4&action=list&nav=2&sub=4&catId=6715901', '其他法定信息': '/public/column/6602281?type=4&action=list&nav=2&sub=5&catId=6715951'}, '平昌县信访局': {'机关简介': '/public/column/6602321?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602321?type=4&action=list&nav=2&sub=1&catId=6715861', '预算/决算': '/public/column/6602321?type=4&action=list&nav=2&sub=2&catId=6715891', '其他法定信息': '/public/column/6602321?type=4&action=list&nav=2&sub=3&catId=6715951'}, '平昌县林业局': {'机关简介': '/public/column/6602341?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602341?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602341?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602341?type=4&action=list&nav=2&sub=3&catId=6715891', '收费项目': '/public/column/6602341?type=4&action=list&nav=2&sub=4&catId=6715901', '重大项目': '/public/column/6602341?type=4&action=list&nav=2&sub=5&catId=6715921', '其他法定信息': '/public/column/6602341?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县医疗保障局': {'机关简介': '/public/column/6602361?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602361?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602361?type=4&action=list&nav=2&sub=2&catId=6715871', '预算/决算': '/public/column/6602361?type=4&action=list&nav=2&sub=3&catId=6715891', '行政许可/处罚': '/public/column/6602361?type=4&action=list&nav=2&sub=4&catId=6715911', '医疗保障': '/public/column/6602361?type=4&action=list&nav=2&sub=5&catId=6715931', '其他法定信息': '/public/column/6602361?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县行政审批和数据局': {'机关简介': '/public/column/6602381?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602381?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602381?type=4&action=list&nav=2&sub=2&catId=6715871', '行政权力': '/public/column/6602381?type=4&action=list&nav=2&sub=3&catId=6715881', '预算/决算': '/public/column/6602381?type=4&action=list&nav=2&sub=4&catId=6715891', '放管服改革': '/public/column/6602381?type=4&action=list&nav=2&sub=5&catId=6715931', '其他法定信息': '/public/column/6602381?type=4&action=list&nav=2&sub=6&catId=6715951'}, '平昌县综合行政执法局': {'机关简介': '/public/column/6602401?type=4&action=list&nav=2&sub=0&catId=6715841', '规划计划': '/public/column/6602401?type=4&action=list&nav=2&sub=1&catId=6715861', '统计信息': '/public/column/6602401?type=4&action=list&nav=2&sub=2&catId=6715871', '行政权力': '/public/column/6602401?type=4&action=list&nav=2&sub=3&catId=6715881', '预算/决算': '/public/column/6602401?type=4&action=list&nav=2&sub=4&catId=6715891', '其他法定信息': '/public/column/6602401?type=4&action=list&nav=2&sub=5&catId=6715951'}, '四川平昌经济开发区管理委员会': {'机关简介': '/public/column/6604364?type=4&action=list&nav=2&sub=0&catId=6717280', '规划计划': '/public/column/6604364?type=4&action=list&nav=2&sub=1&catId=6717283', '统计信息': '/public/column/6604364?type=4&action=list&nav=2&sub=2&catId=6717286', '预算/决算': '/public/column/6604364?type=4&action=list&nav=2&sub=3&catId=6717289', '重大项目': '/public/column/6604364?type=4&action=list&nav=2&sub=4&catId=6717292', '其他法定信息': '/public/column/6604364?type=4&action=list&nav=2&sub=5&catId=6717298'}, '平昌县金宝新区管理委员会': {'机关简介': '/public/column/6602841?type=4&action=list&nav=2&sub=0&catId=6715981', '规划计划': '/public/column/6602841?type=4&action=list&nav=2&sub=1&catId=6716001', '统计信息': '/public/column/6602841?type=4&action=list&nav=2&sub=2&catId=6716011', '预算/决算': '/public/column/6602841?type=4&action=list&nav=2&sub=3&catId=6716031', '民生保障': '/public/column/6602841?type=4&action=list&nav=2&sub=4&catId=6716071', '其他法定信息': '/public/column/6602841?type=4&action=list&nav=2&sub=5&catId=6716091'}, '平昌县佛头山管理委员会': {'机关简介': '/public/column/6602881?type=4&action=list&nav=2&sub=0&catId=6715981', '规划计划': '/public/column/6602881?type=4&action=list&nav=2&sub=1&catId=6716001', '统计信息': '/public/column/6602881?type=4&action=list&nav=2&sub=2&catId=6716011', '预算/决算': '/public/column/6602881?type=4&action=list&nav=2&sub=3&catId=6716031', '民生保障': '/public/column/6602881?type=4&action=list&nav=2&sub=4&catId=6716071', '其他法定信息': '/public/column/6602881?type=4&action=list&nav=2&sub=5&catId=6716091'}, '平昌县同州街道办事处': {'机关简介': '/public/column/6603021?type=4&action=list&nav=2&sub=0&catId=6715981', '规划计划': '/public/column/6603021?type=4&action=list&nav=2&sub=1&catId=6716001', '统计信息': '/public/column/6603021?type=4&action=list&nav=2&sub=2&catId=6716011', '预算/决算': '/public/column/6603021?type=4&action=list&nav=2&sub=3&catId=6716031', '民生保障': '/public/column/6603021?type=4&action=list&nav=2&sub=4&catId=6716071', '其他法定信息': '/public/column/6603021?type=4&action=list&nav=2&sub=5&catId=6716091'}, '平昌县江口街道办事处': {'机关简介': '/public/column/6603041?type=4&action=list&nav=2&sub=0&catId=6715981', '规划计划': '/public/column/6603041?type=4&action=list&nav=2&sub=1&catId=6716001', '统计信息': '/public/column/6603041?type=4&action=list&nav=2&sub=2&catId=6716011', '预算/决算': '/public/column/6603041?type=4&action=list&nav=2&sub=3&catId=6716031', '民生保障': '/public/column/6603041?type=4&action=list&nav=2&sub=4&catId=6716071', '其他法定信息': '/public/column/6603041?type=4&action=list&nav=2&sub=5&catId=6716091'}, '平昌县金宝街道办事处': {'机关简介': '/public/column/6604081?type=4&action=list&nav=2&sub=0&catId=6715981', '规划计划': '/public/column/6604081?type=4&action=list&nav=2&sub=1&catId=6716001', '统计信息': '/public/column/6604081?type=4&action=list&nav=2&sub=2&catId=6716011', '预算/决算': '/public/column/6604081?type=4&action=list&nav=2&sub=3&catId=6716031', '民生保障': '/public/column/6604081?type=4&action=list&nav=2&sub=4&catId=6716071', '其他法定信息': '/public/column/6604081?type=4&action=list&nav=2&sub=5&catId=6716091'}, '平昌县白衣镇人民政府': {'机关简介': '/public/column/6603081?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603081?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603081?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603081?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603081?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603081?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603081?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县涵水镇人民政府': {'机关简介': '/public/column/6603541?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603541?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603541?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603541?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603541?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603541?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603541?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县岳家镇人民政府': {'机关简介': '/public/column/6603561?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603561?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603561?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603561?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603561?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603561?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603561?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县西兴镇人民政府': {'机关简介': '/public/column/6603521?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603521?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603521?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603521?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603521?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603521?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603521?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县龙岗镇人民政府': {'机关简介': '/public/column/6603241?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603241?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603241?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603241?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603241?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603241?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603241?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县土垭镇人民政府': {'机关简介': '/public/column/6603461?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603461?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603461?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603461?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603461?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603461?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603461?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县佛楼镇人民政府': {'机关简介': '/public/column/6603581?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603581?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603581?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603581?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603581?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603581?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603581?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县响滩镇人民政府': {'机关简介': '/public/column/6603101?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603101?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603101?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603101?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603101?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603101?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603101?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县大寨镇人民政府': {'机关简介': '/public/column/6603501?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603501?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603501?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603501?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603501?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603501?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603501?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县驷马镇人民政府': {'机关简介': '/public/column/6603061?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603061?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603061?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603061?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603061?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603061?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603061?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县青云镇人民政府': {'机关简介': '/public/column/6603621?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603621?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603621?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603621?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603621?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603621?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603621?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县兰草镇人民政府': {'机关简介': '/public/column/6603221?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603221?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603221?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603221?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603221?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603221?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603221?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县澌岸镇人民政府': {'机关简介': '/public/column/6603361?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603361?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603361?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603361?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603361?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603361?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603361?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县粉壁镇人民政府': {'机关简介': '/public/column/6603321?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603321?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603321?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603321?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603321?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603321?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603321?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县得胜镇人民政府': {'机关简介': '/public/column/6603261?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603261?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603261?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603261?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603261?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603261?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603261?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县元山镇人民政府': {'机关简介': '/public/column/6603161?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603161?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603161?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603161?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603161?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603161?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603161?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县灵山镇人民政府': {'机关简介': '/public/column/6603741?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603741?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603741?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603741?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603741?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603741?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603741?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县土兴镇人民政府': {'机关简介': '/public/column/6603481?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603481?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603481?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603481?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603481?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603481?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603481?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县云台镇人民政府': {'机关简介': '/public/column/6603181?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603181?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603181?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603181?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603181?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603181?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603181?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县三十二梁镇人民政府': {'机关简介': '/public/column/6604061?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6604061?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6604061?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6604061?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6604061?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6604061?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6604061?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县板庙镇人民政府': {'机关简介': '/public/column/6603201?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603201?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603201?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603201?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603201?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603201?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603201?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县邱家镇人民政府': {'机关简介': '/public/column/6603301?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603301?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603301?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603301?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603301?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603301?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603301?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县笔山镇人民政府': {'机关简介': '/public/column/6603121?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603121?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603121?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603121?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603121?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603121?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603121?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县泥龙镇人民政府': {'机关简介': '/public/column/6603661?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603661?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603661?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603661?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603661?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603661?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603661?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县岩口镇人民政府': {'机关简介': '/public/column/6603701?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603701?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603701?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603701?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603701?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603701?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603701?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县镇龙镇人民政府': {'机关简介': '/public/column/6603141?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603141?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603141?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603141?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603141?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603141?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603141?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县望京镇人民政府': {'机关简介': '/public/column/6603281?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6603281?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6603281?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6603281?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6603281?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6603281?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6603281?type=4&action=list&nav=2&sub=6&catId=6716091'}, '平昌县江家口镇人民政府': {'机关简介': '/public/column/6604071?type=4&action=list&nav=2&sub=0&catId=6715981', '政府工作报告': '/public/column/6604071?type=4&action=list&nav=2&sub=1&catId=6715991', '规划计划': '/public/column/6604071?type=4&action=list&nav=2&sub=2&catId=6716001', '统计信息': '/public/column/6604071?type=4&action=list&nav=2&sub=3&catId=6716011', '预算/决算': '/public/column/6604071?type=4&action=list&nav=2&sub=4&catId=6716031', '民生保障': '/public/column/6604071?type=4&action=list&nav=2&sub=5&catId=6716071', '其他法定信息': '/public/column/6604071?type=4&action=list&nav=2&sub=6&catId=6716091'}}

bumenList = {'平昌县人民政府办公室': '/public/column/6601841?type=2', '平昌县发展和改革局': '/public/column/6601861?type=2', '平昌县经济和信息化局': '/public/column/6601881?type=2', '平昌县教育科技局': '/public/column/6601901?type=2', '平昌县公安局': '/public/column/6601921?type=2', '平昌县民政局': '/public/column/6601941?type=2', '平昌县司法局': '/public/column/6601961?type=2', '平昌县财政局': '/public/column/6601981?type=2', '平昌县人力资源和社会保障局': '/public/column/6602001?type=2', '平昌县自然资源和规划局': '/public/column/6602021?type=2', '平昌县住房和城乡建设局': '/public/column/6602041?type=2', '平昌县交通运输局': '/public/column/6602061?type=2', '平昌县水利局': '/public/column/6602081?type=2', '平昌县农业农村局': '/public/column/6602101?type=2', '平昌县商务局': '/public/column/6602121?type=2', '平昌县文化广播电视体育和旅游局': '/public/column/6602141?type=2', '平昌县卫生健康局': '/public/column/6602161?type=2', '平昌县退役军人事务局': '/public/column/6602181?type=2', '平昌县应急管理局': '/public/column/6602201?type=2', '平昌县审计局': '/public/column/6602221?type=2', '平昌县市场监督管理局': '/public/column/6602241?type=2', '巴中市平昌生态环境局': '/public/column/6602261?type=2', '平昌县统计局': '/public/column/6602281?type=2', '平昌县信访局': '/public/column/6602321?type=2', '平昌县林业局': '/public/column/6602341?type=2', '平昌县医疗保障局': '/public/column/6602361?type=2', '平昌县行政审批和数据局': '/public/column/6602381?type=2', '平昌县综合行政执法局': '/public/column/6602401?type=2', '四川平昌经济开发区管理委员会': '/public/column/6604364?type=2', '平昌县金宝新区管理委员会': '/public/column/6602841?type=2', '平昌县佛头山管理委员会': '/public/column/6602881?type=2', '平昌县同州街道办事处': '/public/column/6603021?type=2', '平昌县江口街道办事处': '/public/column/6603041?type=2', '平昌县金宝街道办事处': '/public/column/6604081?type=2', '平昌县白衣镇人民政府': '/public/column/6603081?type=2', '平昌县涵水镇人民政府': '/public/column/6603541?type=2', '平昌县岳家镇人民政府': '/public/column/6603561?type=2', '平昌县西兴镇人民政府': '/public/column/6603521?type=2', '平昌县龙岗镇人民政府': '/public/column/6603241?type=2', '平昌县土垭镇人民政府': '/public/column/6603461?type=2', '平昌县佛楼镇人民政府': '/public/column/6603581?type=2', '平昌县响滩镇人民政府': '/public/column/6603101?type=2', '平昌县大寨镇人民政府': '/public/column/6603501?type=2', '平昌县驷马镇人民政府': '/public/column/6603061?type=2', '平昌县青云镇人民政府': '/public/column/6603621?type=2', '平昌县兰草镇人民政府': '/public/column/6603221?type=2', '平昌县澌岸镇人民政府': '/public/column/6603361?type=2', '平昌县粉壁镇人民政府': '/public/column/6603321?type=2', '平昌县得胜镇人民政府': '/public/column/6603261?type=2', '平昌县元山镇人民政府': '/public/column/6603161?type=2', '平昌县灵山镇人民政府': '/public/column/6603741?type=2', '平昌县土兴镇人民政府': '/public/column/6603481?type=2', '平昌县云台镇人民政府': '/public/column/6603181?type=2', '平昌县三十二梁镇人民政府': '/public/column/6604061?type=2', '平昌县板庙镇人民政府': '/public/column/6603201?type=2', '平昌县邱家镇人民政府': '/public/column/6603301?type=2', '平昌县笔山镇人民政府': '/public/column/6603121?type=2', '平昌县泥龙镇人民政府': '/public/column/6603661?type=2', '平昌县岩口镇人民政府': '/public/column/6603701?type=2', '平昌县镇龙镇人民政府': '/public/column/6603141?type=2', '平昌县望京镇人民政府': '/public/column/6603281?type=2', '平昌县江家口镇人民政府': '/public/column/6604071?type=2'}

bumen_zhengce_list = {'平昌县发展和改革局': '/public/column/6601861?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县经济和信息化局': '/public/column/6601881?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县教育科技局': '/public/column/6601901?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县公安局': '/public/column/6601921?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县民政局': '/public/column/6601941?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县司法局': '/public/column/6601961?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县财政局': '/public/column/6601981?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县人力资源和社会保障局': '/public/column/6602001?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县自然资源和规划局': '/public/column/6602021?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县住房和城乡建设局': '/public/column/6602041?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县交通运输局': '/public/column/6602061?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县水利局': '/public/column/6602081?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县农业农村局': '/public/column/6602101?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县商务局': '/public/column/6602121?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县文化广播电视体育和旅游局': '/public/column/6602141?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县卫生健康局': '/public/column/6602161?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县退役军人事务局': '/public/column/6602181?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县应急管理局': '/public/column/6602201?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县审计局': '/public/column/6602221?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县市场监督管理局': '/public/column/6602241?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '巴中市平昌生态环境局': '/public/column/6602261?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县统计局': '/public/column/6602281?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县信访局': '/public/column/6602321?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县林业局': '/public/column/6602341?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县医疗保障局': '/public/column/6602361?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县行政审批和数据局': '/public/column/6602381?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县综合行政执法局': '/public/column/6602401?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '四川平昌经济开发区管理委员会': '/public/column/6604364?type=4&action=list&nav=2&sub=0&catId=6717327',
                      '平昌县金宝新区管理委员会': '/public/column/6602841?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县佛头山管理委员会': '/public/column/6602881?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县同州街道办事处': '/public/column/6603021?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县江口街道办事处': '/public/column/6603041?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县金宝街道办事处': '/public/column/6604081?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县白衣镇人民政府': '/public/column/6603081?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县涵水镇人民政府': '/public/column/6603541?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县岳家镇人民政府': '/public/column/6603561?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县西兴镇人民政府': '/public/column/6603521?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县龙岗镇人民政府': '/public/column/6603241?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县土垭镇人民政府': '/public/column/6603461?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县佛楼镇人民政府': '/public/column/6603581?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县响滩镇人民政府': '/public/column/6603101?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县大寨镇人民政府': '/public/column/6603501?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县驷马镇人民政府': '/public/column/6603061?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县青云镇人民政府': '/public/column/6603621?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县兰草镇人民政府': '/public/column/6603221?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县澌岸镇人民政府': '/public/column/6603361?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县粉壁镇人民政府': '/public/column/6603321?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县得胜镇人民政府': '/public/column/6603261?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县元山镇人民政府': '/public/column/6603161?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县灵山镇人民政府': '/public/column/6603741?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县土兴镇人民政府': '/public/column/6603481?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县云台镇人民政府': '/public/column/6603181?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县三十二梁镇人民政府': '/public/column/6604061?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县板庙镇人民政府': '/public/column/6603201?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县邱家镇人民政府': '/public/column/6603301?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县笔山镇人民政府': '/public/column/6603121?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县泥龙镇人民政府': '/public/column/6603661?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县岩口镇人民政府': '/public/column/6603701?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县镇龙镇人民政府': '/public/column/6603141?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县望京镇人民政府': '/public/column/6603281?type=4&action=list&nav=2&sub=0&catId=6717326',
                      '平昌县江家口镇人民政府': '/public/column/6604071?type=4&action=list&nav=2&sub=0&catId=6717326'}

bumen_departid = {'平昌县人民政府办公室': [1205, 2334], '平昌县发展和改革局': [815], '平昌县经济和信息化局': [276], '平昌县教育科技局': [304],
                  '平昌县公安局': [1152], '平昌县民政局': [1259], '平昌县司法局': [432], '平昌县财政局': [247], '平昌县人力资源和社会保障局': [1264],
                  '平昌县自然资源和规划局': [1272], '平昌县住房和城乡建设局': [1278], '平昌县交通运输局': [2001], '平昌县水利局': [372], '平昌县农业农村局': [1299],
                  '平昌县商务局': [351], '平昌县文化广播电视体育和旅游局': [1322], '平昌县卫生健康局': [10], '平昌县退役军人事务局': [182], '平昌县应急管理局': [1328],
                  '平昌县审计局': [404], '平昌县市场监督管理局': [353], '巴中市平昌生态环境局': [418], '平昌县统计局': [1990], '平昌县乡村振兴局': [1086],
                  '平昌县信访局': [1335], '平昌县林业局': [287], '平昌县医疗保障局': [1337], '平昌县行政审批和数据局': [1338], '平昌县综合行政执法局': [1341],
                  '四川平昌经济开发区管理委员会': [622], '平昌县金宝新区管理委员会': [13], '平昌县佛头山管理委员会': [480], '平昌县同州街道办事处': [2088],
                  '平昌县江口街道办事处': [99], '平昌县金宝街道办事处': [2208], '平昌县白衣镇人民政府': [57], '平昌县涵水镇人民政府': [14], '平昌县岳家镇人民政府': [697],
                  '平昌县西兴镇人民政府': [647], '平昌县龙岗镇人民政府': [573], '平昌县土垭镇人民政府': [993], '平昌县佛楼镇人民政府': [853],
                  '平昌县响滩镇人民政府': [662], '平昌县大寨镇人民政府': [804], '平昌县驷马镇人民政府': [27], '平昌县青云镇人民政府': [931],
                  '平昌县兰草镇人民政府': [540], '平昌县澌岸镇人民政府': [1893], '平昌县粉壁镇人民政府': [831], '平昌县得胜镇人民政府': [34],
                  '平昌县元山镇人民政府': [2059], '平昌县灵山镇人民政府': [48], '平昌县土兴镇人民政府': [959], '平昌县云台镇人民政府': [722],
                  '平昌县三十二梁镇人民政府': [394], '平昌县板庙镇人民政府': [1561], '平昌县邱家镇人民政府': [2287], '平昌县笔山镇人民政府': [227],
                  '平昌县泥龙镇人民政府': [900], '平昌县岩口镇人民政府': [1044], '平昌县镇龙镇人民政府': [2020], '平昌县望京镇人民政府': [1012],
                  '平昌县江家口镇人民政府': [2270]}

bumen_phone = {'平昌县人民政府办公室': [("17311067255", "吴晓龙")], '平昌县发展和改革局': [("15328278750", "龙寿林"), ("13547305868", "周良建")],
               '平昌县经济和信息化局': [("15328278750", "邓雁霞"), ("13541774000", "熊志军")],
               '平昌县教育科技局': [("13550496908", "苟兴旺"), ("19983620031", "李英超")],
               '平昌县公安局': [("13608246668", "王  雷"), ("13568496220", "王  勇")],
               '平昌县民政局': [("17761147717", "符春雷"), ("18008271618", "韩  旭")],
               '平昌县司法局': [("18282701152", "邢文军"), ("13629072299", "姜朝晖")],
               '平昌县财政局': [("13980290308", "董育强"), ("18784268548", "雷  鸣")],
               '平昌县人力资源和社会保障局': [("13881691265", "余定军"), ("15983991351", "何文波")],
               '平昌县自然资源和规划局': [("13981691930", "夏  宇"), ("13795938108", "王川江")],
               '平昌县住房和城乡建设局': [("13981671182", "邹  坪"), ("15828918700", "杨国儒")],
               '平昌县交通运输局': [("13518479888", "苟中良"), ("15284711687", "彭乔木")],
               '平昌县水利局': [("15284739111", "谢其雄"), ("15282752823", "于丹梅")],
               '平昌县农业农村局': [("13980294599", "胥英豪"), ("13550489480", "徐  勇")],
               '平昌县商务局': [("19181698333", "赵  强"), ("18981698187", "唐  立")],
               '平昌县文化广播电视体育和旅游局': [("17760591777", "向  东"), ("19940723533", "黄  瀚")],
               '平昌县卫生健康局': [("15983981358", "周勇华"), ("19960320001", "潘铄灵")],
               '平昌县退役军人事务局': [("13568489000", "何星明"), ("13408276600", "刘平原")],
               '平昌县应急管理局': [("18090447899", "冯政荣"), ("18382703343", "何  睿"),("18783859751","刘慧")],
               '平昌县审计局': [("13568485317", "何明军"), ("13547320966", "温德超")],
               '平昌县市场监督管理局': [("13778791101", "苟耀华"), ("13550481122", "何文超")],
               '巴中市平昌生态环境局': [("13795940707", "靳弘章"), ("17726556235", "蔡承华")],
               '平昌县统计局': [("13541780061", "苟  尧"), ("18227386900", "刘华平")], '平昌县乡村振兴局': [("", ""), ("", "")],
               '平昌县信访局': [("15284736888", "向伟林"), ("13881691264", "高唯泰")],
               '平昌县林业局': [("13568475833", "孙继禹"), ("13678278985", "白 芬")],
               '平昌县医疗保障局': [("13568461999", "刘晓波"), ("15228564777", "袁涌钧"), ("19983610140", "徐毅")],
               '平昌县行政审批和数据局': [("13458956999", "陈雨珍"), ("17790440080", "梁  周")],
               '平昌县综合行政执法局': [("17882709999", "吴  栋"), ("15282755773", "黄清盛")],
               '四川平昌经济开发区管理委员会': [("13980295027", "贾  健"), ("18282708920", "陈诗海")],
               '平昌县金宝新区管理委员会': [("13608246018", "刘  东"), ("18384473994", "董  炀")],
               '平昌县佛头山管理委员会': [("15808272918", "杨海波"), ("15282746136", "赖丽名")],
               '平昌县同州街道办事处': [("13981651901", "苟  磊"), ("15082732318", "肖  玲")],
               '平昌县江口街道办事处': [("13547313303", "张宇鸣"), ("13981655925", "任晓华")],
               '平昌县金宝街道办事处': [("13458954195", "张  堋"), ("15182778567", "张容华")],
               '平昌县白衣镇人民政府': [("18728717171", "吴  飞"), ("18113764079", "雷  枭")],
               '平昌县涵水镇人民政府': [("13981695925", "杨  斌"), ("17308097900", "冯  凡")],
               '平昌县岳家镇人民政府': [("18123410260", "王文川"), ("18280118785", "林  安")],
               '平昌县西兴镇人民政府': [("13678278567", "袁  毅"), ("19983613007", "林  森")],
               '平昌县龙岗镇人民政府': [("13881655966", "李越翰"), ("18728789825", "吴泽军")],
               '平昌县土垭镇人民政府': [("13981661300", "李佳平"), ("13699443727", "李宏标")],
               '平昌县佛楼镇人民政府': [("18090203188", "李世伟"), ("18582555832", "何宗庚")],
               '平昌县响滩镇人民政府': [("15282766786", "杨永富"), ("18398989378", "曾爱辉")],
               '平昌县大寨镇人民政府': [("13350476357", "张海钦"), ("15082708793", "杨  雄")],
               '平昌县驷马镇人民政府': [("13551793088", "夏照祥"), ("19983658665", "吴攀宇")],
               '平昌县青云镇人民政府': [("13881691516", "姚  健"), ("18808125418", "王理申")],
               '平昌县兰草镇人民政府': [("13981656465", "刘  谚"), ("18223367259", "韩海军")],
               '平昌县澌岸镇人民政府': [("17311036777", "张  玲"), ("18980290598", "方  鑫")],
               '平昌县粉壁镇人民政府': [("13678272390", "向国平"), ("19181686097", "刘  阳")],
               '平昌县得胜镇人民政府': [("18111339665", "李生荣"), ("19983609902", "赵晓艳")],
               '平昌县元山镇人民政府': [("13550492699", "王  敏"), ("15328266698", "杨  霞")],
               '平昌县灵山镇人民政府': [("15082745677", "何杨春"), ("13551783958", "邓仕林")],
               '平昌县土兴镇人民政府': [("13551786061", "赵  芳"), ("13990309069", "刘  焱")],
               '平昌县云台镇人民政府': [("13778771678", "潘曙光"), ("15882710237", "王从兴")],
               '平昌县三十二梁镇人民政府': [("19960155959", "马宏秋"), ("13982591818", "李小雨")],
               '平昌县板庙镇人民政府': [("13698275666", "李晓庆"), ("15528671372", "顾志成")],
               '平昌县邱家镇人民政府': [("13568485376", "张  胤"), ("15228560799", "李  雄")],
               '平昌县笔山镇人民政府': [("13547311956", "陈其勇"), ("15828939411", "唐思兵")],
               '平昌县泥龙镇人民政府': [("19160170839", "张春林"), ("19960303688", "王通文")],
               '平昌县岩口镇人民政府': [("13547307736", "邹  卓"), ("18682778927", "孙  杰")],
               '平昌县镇龙镇人民政府': [("19130553176", "苟子荀"), ("17780754357", "白世宁")],
               '平昌县望京镇人民政府': [("13778798285", "李   森"), ("18398983020", "张蓝心")],
               '平昌县江家口镇人民政府': [("18282712666", "杨明强"), ("18282759485", "吴小静")]}

xlsx_name = '网站监测反馈v3.0.xlsx'
# 标题样式

tittle_font = Font(size=20, bold=True)
header_font = Font(size=13, bold=True)

# 私人测试新功能群
key_person = '7de50f0c-a890-4a72-8c50-d50b8b6e5f3c'
# 测试小群的key

key_cs = '425a53f6-696e-46c1-9d4a-fae8940b136f'
# 正式群key
key_zs = '6c00ba33-68ab-403e-bab2-2b9134a7d7f6'

# 获取当前的星期几（0=星期一，6=星期日）
current_weekday = datetime.datetime.now().weekday()
# current_year_mon_day = datetime.datetime.now().date()

# 如果当前是星期一，选择正式群的key，否则选择测试小群的key
key_choose = key_zs if current_weekday == 0 else key_cs

up_time_conf = {'机关简介': 365, '政府工作报告': 365, '规划计划': 365, '政策': 365, '统计信息': 90, '行政权力': 90, '预算/决算': 365, '收费项目': 365,
                '政府采购': 180, '重大项目': 90, '重大民生信息': 90, '其他法定信息': 90, '教育科技': 90, '养老服务': 90, '社会救助': 90, '就业创业': 90,
                '社会保障': 60, '招考录用': 90, '司法监督': 90, '价格信息': 90, '住房保障': 90, '涉农补贴': 90, '农产品价格监测': 90, '应急管理': 60,
                '监测预警': 90, '审计监督': 90, '市场监管': 90, '环评公示': 90, '环保督察': 60, '环境质量公报': 90, '执法检查': 90, '乡村振兴': 90,
                '行政许可/处罚': 90, '医疗保障': 90, '教育科技': 90, '公共文化服务': 90, '放管服改革': 90, '卫生健康': 60, '价格监测': 90, '民生保障': 90}

# 基层政务公开领域和负责单位映射
jczwgk_area_comp_dic = {'公共文化服务': '平昌县文化广播电视体育和旅游局', '就业领域': '平昌县人力资源和社会保障局', '涉农补贴': '平昌县农业农村局', '食品药品': '平昌县市场监督管理局',
                        '社会救助': '平昌县民政局', '卫生健康': '平昌县卫生健康局', '养老服务': '平昌县民政局', '义务教育': '平昌县教育科技和体育局', '公共法律': '平昌县司法局',
                        '税收管理': '国家税务总局平昌县税务局', '广播电视和网络视听': '平昌县文化广播电视体育和旅游局', '旅游领域': '平昌县文化广播电视体育和旅游局',
                        '社会保险': '平昌县人力资源和社会保障局', '自然资源': '平昌县自然资源和规划局', '城市综合执法': '平昌县综合行政执法局', '户籍管理': '平昌县公安局',
                        '财政预决算': '平昌县财政局', '市政服务': '平昌县住房和城乡建设局', '农村危房改造': '平昌县住房和城乡建设局',
                        '国有土地上房屋征收与补偿': '平昌县住房和城乡建设局', '保障性住房': '平昌县住房和城乡建设局', '新闻出版版权': '县委宣传部', '生态环境': '巴中市平昌生态环境局',
                        '统计领域': '平昌县统计局', '公共资源交易': '县公共资源交易服务中心', '交通运输': '平昌县交通运输局', '扶贫领域': '平昌县乡村振兴局',
                        '重大建设项目': '平昌县发展和改革局', '安全生产': '平昌县应急管理局', '救灾领域': '平昌县应急管理局'}

database_cs = {
    "host": "yuxiaohaishidalao.shop",
    "user": "root",
    "password": "vas9624..",
    "database": "smartpc"
}
database_zs_nat = {
    "host": "10.167.39.125",
    "user": "kfvasing",
    "password": "vas9624..",
    "database": "smartpingchangdb"
}
database_zs_net = {
    "host": "222.215.24.208",
    "user": "kfvasing",
    "password": "vas9624..",
    "database": "smartpingchangdb"
}
database = database_zs_nat

# 考核类型 17：机器人-栏目超期   18：机器人-统计信息缺失  19：机器人-政府信息公开年报缺失
menu_over_update = '机器人-栏目超期'
miss_tj_year = '机器人-统计信息缺失'
zf_year_report = '机器人-政府信息公开年报缺失'
finish_score = '统计扣分情况发送'
zc_over_time = '机器人-政策超期'

# # 考核类型映射字典
# score_dic = {menu_over_update: '机器人-栏目超期', miss_tj_year: '机器人-统计信息缺失', zf_year_report: '机器人-政府信息公开年报缺失'}

# 按照星期几确定是否考核,这里是false才考核，注意
is_record = current_weekday != 0
# is_record = 0

# 如果当前是星期一，选择正式群的key，否则选择测试小群的key # 考核消息暂时发测试群
# record_key_choose = key_zs if current_weekday == 0 else key_cs
record_key_choose = key_cs

xlsx_score_name = '本周考核反馈 v1.0.xlsx'

proxies = None
# 测试新功能时打开，避免发错
# key_choose = key_person
# record_key_choose = key_choose


qy_id = 'ww10b2b295ab660549'
# 数字平昌2.0
secret_szpc = 'vwoopFGBA92smZ28oF03KPMM0DN6lXz2lM4VCYDU14c'
# 农村污水
# secret_ncws = 'XM1DfioQGtKJIoRWHsm7IrfgA0h0shTyO72v9ZsjuyA'
# 数字平昌agentid
agent_id_szpc = 1000133


def getproxies(up=False):
    global proxies  # 在函数内部修改全局变量，需要声明 global
    if up or proxies is None:
        # 提取代理API接口，获取1个代理IP
        api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o6zqx71jh7hiii663qrt&num=1&signature=ae5jtj55np18yfpsjrra5gagd1ljuymx&pt=1&sep=1&transferip=1"

        # 获取API接口返回的代理IP
        proxy_ip = requests.get(api_url, verify=False).text

        # 用户名密码认证(私密代理/独享代理)
        username = "d4348123377"
        password = "vas962464"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
        }
    print('代理：', proxies)
    return proxies


def make_request_get(url, params=None, proxies=None):
    if not url.startswith('http'):
        url = 'http://www.scpc.gov.cn' + url
    try:

        response = requests.get(url, params=params, proxies=proxies)

    except Exception as e:
        print('网络波动', url)
        try:
            print(url)
            response = requests.get(url, params=params, proxies=getproxies())
        except Exception as e:
            print('代理过期', url)
            response = requests.get(url, params=params, proxies=getproxies(up=True))

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    return response, soup


if __name__ == '__main__':
    pass
    # url_test = 'http://www.ccgp-sichuan.gov.cn/freecms/site/sichuan/ggxx/info/2023/8a69c8b18c0bd8aa018c1dd48e712503.html?noticeType=00102'
    # response = make_request_get(url_test)
    # print(response.status_code)
    # print(response.text)
