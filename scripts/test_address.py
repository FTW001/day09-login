import sys
import os

sys.path.append(os.getcwd())
from page.page_in import PageIn
from tool.get_driver import GetDriver


class TestAddress:
    # 初始化
    def setup_class(self):
        # 获取 PageAddress
        self.address = PageIn().page_get_pageaddress()
        # 获取PageLogin 并且登录成功
        PageIn().page_get_pagelogin().page_login_address()
        # 点击 地址管理
        self.address.page_click_manage()

    # 结束
    def teardown_class(self):
        # 关闭driver对象
        GetDriver.quit_driver()

    # 测试方法
    def test01_add_address(self,name="张三", phone="13800001111", address="京城81号", code="100010"):
        # 调用地址管理新增业务方法
        self.address.page_address(name, phone, address, code)
        # 组合收件人 和电话
        expect = name+"  "+phone
        # 测试看效果
        print("判断 {} in {}".format(expect, self.address.page_get_name_iphone()))
        # 断言
        assert expect in self.address.page_get_name_iphone()
