from poium import Page, PageElement, PageElements


class SomePage(Page):
    elem_id = PageElement(id_='id')
    elem_name = PageElement(name='name')
    elem_class = PageElement(class_='class')
    elem_tag = PageElement(tag='input')
    elem_link_text = PageElement(link_text='this_is_link')
    elem_partial_link_text = PageElement(partial_link_text='is_link')
    elem_xpath = PageElement(xpath='//*[@id="kk"]')
    elem_css = PageElement(css='#id')


class BaiduPage(Page):
    search_input = PageElement(id_='kw', timeout=5)
    search_button = PageElement(id_='su', timeout=30)


class LoginPage(Page):
    """
    登录page类
    """
    username = PageElement(css='#loginAccount', describe="用户名")
    password = PageElement(css='#loginPwd', describe="密码")
    login_button = PageElement(css='#login_btn', describe="登录按钮")
    user_info = PageElement(css="a.nav_user_name > span", describe="用户信息")


class ResultPage(Page):
    # 定位一组元素
    search_result = PageElements(xpath="//div/h3/a")
