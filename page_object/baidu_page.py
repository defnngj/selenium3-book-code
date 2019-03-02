from base import BasePage


class BaiduPage(BasePage):
    """百度Page层，百度页面封装操作到的元素"""
    url = "https://www.baidu.com"

    def search_input(self, search_key):
        self.by_id("kw").send_keys(search_key)

    def search_button(self):
        self.by_id("su").click()

