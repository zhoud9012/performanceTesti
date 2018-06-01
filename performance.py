# -*-coding:utf8-*-
# 性能测试基类
import re
import time
import requests
import threading


class Performance(threading.Thread):
    def __init__(self, url="", method="get", header={}, body="", body_type="json"):
        threading.Thread.__init__(self)
        self.url = url
        self.method = method
        self.header = header
        self.body = body
        self.body_type = body_type

    def run(self):
        self.test_performance()

    def test_performance(self):
        start_time = time.time()
        try:
            response = self.send_request()
            if response.status_code == 200:
                status = "success"
            else:
                status = "fail"
        except Exception as e:
            print(e)
            status = "except"
        end_time = time.time()
        spend_time = end_time - start_time
        return status, spend_time

    def send_request(self):
        if re.search(self.method, 'GET', re.IGNORECASE):
            response = requests.get(self.url, headers=self.header)
        else:
            if self.body_type == "json":
                response = requests.post(self.url, headers=self.header, json=self.body)
            elif self.body_type == "file":
                response = requests.post(self.url, headers=self.header, files=self.body)
            elif self.body_type == "data":
                response = requests.post(self.url, headers=self.header, data=self.body)
        return response
