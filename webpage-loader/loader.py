from selenium import webdriver

class loader:
    def __init__():
        super()

        # Set no images flag
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images':2}
        chromeOptions.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
    
    def __exit__(self, type, value, traceback):
        self.driver.quit()

    def render_page(url):
        driver.get(url)
        driver.page_source()