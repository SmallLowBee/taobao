import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TBMS:
    def __init__(self):
        self.time = input('输入秒杀时间(按照这个格式输: 2019-12-23 18:44:01):')
        self.driver = webdriver.Chrome()

    def scan_code_to_log_in_and_open_shopping_cart(self):
        self.driver.get('https://login.taobao.com/member/login.jhtml')
        self.__wait_to_login()
        self.driver.find_element_by_xpath('//*[@id="mc-menu-hd"]').click()
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_id('J_SelectAll2').click()

    def __wait_to_login(self):
        # 20秒内完成登录
        print('扫描二维码登录')
        time_num = 21
        num = 1
        while True:
            print('请在 ', time_num - num, ' 秒之内完成扫码登录')
            time.sleep(1)
            num += 1
            if time_num <= num:
                return

    def click_settlement(self):
        self.__wait_until_the_specified_time()
        while True:
            try:
                self.driver.find_element_by_link_text("结 算").click()
                wait = WebDriverWait(self.driver, 10)
                # self.driver.find_elements_by_link_text('提交订单').click()
                self.driver.find_element_by_class_name('go-btn').click()
                print('扫码结算')
                time.sleep(60)
                break
            except:
                self.driver.refresh()
                continue

    def __wait_until_the_specified_time(self):
        scheduled_time = time.strptime(self.time, '%Y-%m-%d %H:%M:%S')
        scheduled_time = time.mktime(scheduled_time)
        while True:
            nowtime = time.time()
            if nowtime >= scheduled_time:
                return

    def main(self):
        self.scan_code_to_log_in_and_open_shopping_cart()
        self.click_settlement()


if __name__ == '__main__':
    tb = TBMS()
    tb.main()
