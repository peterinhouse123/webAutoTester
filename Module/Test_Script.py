#管理 與讀取 測試腳本
from selenium.webdriver import Chrome

class Test_Script():
    def __init__(self,work_driver):
        self.driver = work_driver #type: Chrome

    def Get_element(self,desc,desc_type):
        item = False
        try:
            if desc_type == "css":
                item = self.driver.find_element_by_css_selector(desc)
            if desc_type == "xpath":
                item = self.driver.find_element_by_xpath(desc)
            return item
        except Exception as e:
            print("--------------Test_Script_Error ----------------")
            print(e)
            print("------------------------------------------------")
        return False

    def Click(self,desc,desc_type):
        ele = self.Get_element(desc,desc_type)
        if ele == False:
            return False
        ele.click()
        return True


    def Send_Key(self,desc,desc_type,key):
        ele = self.Get_element(desc, desc_type) #type: Chrome.find_element_by_class_name()
        if ele == False:
            return False
        ele.send_keys(key)
        return True

    def Check_url(self, chk_txt):
        if chk_txt == self.driver.current_url:
            return True
        return False

    def Check_url_Exist(self, chk_txt):
        if chk_txt in self.driver.current_url:
            return True
        return False

    def Check_text(self, desc, desc_type, chk_txt):
        ele = self.Get_element(desc, desc_type)
        if ele == False:
            return False
        ele_txt = ele.text
        if ele_txt == chk_txt:
            return True
        return False

    def Check_text_Exist(self, desc, desc_type, chk_txt):
        ele = self.Get_element(desc, desc_type)
        if ele == False:
            return False
        # print(ele)
        ele_txt = ele.text
        # print(ele_txt)
        if chk_txt in ele_txt :
            return True
        return False

    def Check_Img(self,template_img_path):
        pass