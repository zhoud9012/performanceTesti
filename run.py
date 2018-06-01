# -*-coding:utf8-*-
import performance
import sys

# 取数组的百分比值，如90%响应时间
# 90%响应时间的获取规则，参考loadrunner官方文档
# 1. Sort the transaction instances by their value.
# 2. Remove the top 10% instances.
# 3. The highest value left is the 90th percentile.
def get_percent_time(data_list, percent):
    data_list = sorted(data_list)
    if len(data_list)*(1-percent) <= 1:
        r_length = 1
    else:
        r_length = len(data_list)*(1-percent)
        r_length = int(round(r_length))
    data_list = data_list[:len(data_list)-r_length]
    return data_list[-1]

# 设置并发数
thread_count = sys.argv[2] 
thread_count = int(thread_count) 
# 所有线程花费时间列表
spend_time_list = []
# 最大响应时间
max_time = 0
# 最小响应时间
min_time = 3600
# 小于3秒的请求数
less_than_3_total = 0
# 大于3秒的请求数
more_than_3_total = 0
# 成功的请求数
success_total = 0
# 失败的请求数
fail_total = 0
# 异常的请求数
except_total = 0
# 总请求数
total = 0
# 请求地址
url = sys.argv[1] 
# 请求头
header = {"Market-Version": "3.1"}
i = 0
# 所有线程总花费时间
time_total = 0
while i < thread_count:
    pf = performance.Performance(url=url, header=header)
    status, spend_time = pf.test_performance()
    spend_time_list.append(spend_time)
    total += 1
    if status == "success":
        success_total += 1
    elif status == "fail":
        fail_total += 1
    elif status == "except":
        except_total += 1
    if spend_time > max_time:
        max_time = spend_time
    if spend_time < min_time:
        min_time = spend_time
    if spend_time > 3:
        more_than_3_total += 1
    else:
        less_than_3_total += 1
    time_total += spend_time
    pf.start()
    i += 1


# 平均响应时间
avg_time = time_total/thread_count
# 响应时间列表从小到大排序
spend_time_list = sorted(spend_time_list)
print("平均响应时间：%s" % avg_time)
print("最大响应时间：%s" % max_time)
print("最小响应时间：%s" % min_time)
print("90%%响应时间：%s" % (get_percent_time(spend_time_list, 0.9)))
print("99%%响应时间：%s" % (get_percent_time(spend_time_list, 0.99)))
print("80%%响应时间：%s" % (get_percent_time(spend_time_list, 0.8)))
print("总请求数：%s" % total)
print("成功请求数：%s" % success_total)
print("失败请求数：%s" % fail_total)
print("异常请求数：%s" % except_total)
print("大于3秒的请求数：%s" % more_than_3_total)
print("小于3秒的请求数：%s" % less_than_3_total)
