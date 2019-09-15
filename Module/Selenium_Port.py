#功能： 簡單的初始化一切麻煩的selnium工作

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
#使用chrome的webdriver

#如果需要執行完自動關閉，就要加上下面這一行
#browser.close()
class Selnium_Port():
    def __init__(self,Binary_File_Path,Chrome_Driver_Path):
        self.Binary_File_Path = Binary_File_Path
        self.Chrome_Driver_Path = Chrome_Driver_Path
        self.Option = Options()
        self.Option.binary_location = self.Binary_File_Path
        self.Driver = None

    def Init_Driver(self):
        self.Driver = Chrome(executable_path=self.Chrome_Driver_Path,chrome_options=self.Option)
        # self.Driver.get("https://google.com.tw")
        return self.Driver

if __name__ == '__main__':
    obj = Selnium_Port(Binary_File_Path= "../Tool/chrome/chrome.exe",Chrome_Driver_Path="../Tool/chromedriver.exe")

    obj.Init_Driver()
    while 1:
        time.sleep(1)