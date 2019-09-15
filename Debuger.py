from Module import Selenium_Port
from Module import Test_Script
import time

class main():
    def __init__(self):
        self.Selenium_Port = Selenium_Port.Selnium_Port(Binary_File_Path= "Tool/chrome/chrome.exe",Chrome_Driver_Path="Tool/chromedriver.exe")
        # self.Test_Script = Test_Script.Test_Script()
        self.Driver = self.Selenium_Port.Init_Driver()
    def Good_Hand_Run_Test(self):
        Driver = self.Driver
        Script = Test_Script.Test_Script(Driver)

        Driver.get("https://www.google.com.tw")
        Script.Click(desc='//div[@class="FPdoLc VlcLAe"]/center/input[@value="好手氣"]',desc_type="xpath")
        chk = Script.Check_url_Exist("doodles")
        if chk == True:
            print("好手氣~~測試成功")
        else:
            print("測試失敗")

    def Search_Test(self):
        #resultStats
        Driver = self.Driver
        Script = Test_Script.Test_Script(Driver)
        Driver.get("https://www.google.com.tw")
        Script.Send_Key(desc='//input[@title="Google 搜尋"]',desc_type="xpath",key="測試搜索\n")
        time.sleep(2)
        chk = Script.Check_text_Exist(desc="#resultStats",desc_type="css",chk_txt="結果")
        if chk == True:
            print("搜索~~測試成功")
        else:
            print("測試失敗")




if __name__ == '__main__':
    obj = main()
    obj.Search_Test()
