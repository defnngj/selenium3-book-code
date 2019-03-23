from poium import Page, PageElement


class BBSPage(Page):
    search_box = PageElement(id_="com.meizu.flyme.flymebbs:id/r9")
    search_button = PageElement(id_="com.meizu.flyme.flymebbs:id/rc")
    search_result = PageElement(id_="com.meizu.flyme.flymebbs:id/er")
