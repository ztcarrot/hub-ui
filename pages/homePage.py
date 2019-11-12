class homePage(object):

    def __init__(self,browser):   
        self.browser = browser

    def open(self):
        print('navigate to home page')
        self.browser.get("https://www.baidu.com/")
        
    def close(self):
        print('close browser')
        self.browser.close()
        print('browser is closed')