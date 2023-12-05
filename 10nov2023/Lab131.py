
class Browser:
    def __init__(self, browser):
        self.browser = browser


    def open_browser(self, browser = "Chrome"):
        print("write the code to open the browser"+ browser)


b = Browser("Edge")
b.open_browser()