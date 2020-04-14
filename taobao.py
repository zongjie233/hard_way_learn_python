# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time
from os import path

driver = webdriver.Chrome()


def login(url):
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        driver.get(url)
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= buytime:
            try:
                # 点击抢购
                if driver.find_element_by_id("J_LinkBuy"):
                    print("点吖！！！")
                    driver.find_element_by_id("J_LinkBuy").click()
                    time.sleep(0.09)
                    while now >= buytime:
                        try:
                            print("买吖！！！")
                            driver.find_element_by_class_name('go-btn').click()
                            driver.find_element_by_link_text('提交订单').click()
                        except:
                            time.sleep(0.02)
            except:
                time.sleep(0.08)
        print(now)
        time.sleep(0.05)


if __name__ == "__main__":
    times = input("请输入抢购时间：时间格式：2018-11-06 10:08:00.000000")
    # 时间格式："2018-09-06 11:20:00.000000"
    url = input("请输入抢购地址")
    login(url)
    buy(times)