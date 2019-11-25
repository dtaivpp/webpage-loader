from selenium import webdriver
import time

class loader:
    def __init__(self):
        # Set no images flag
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images':2}
        chromeOptions.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
    
    def __exit__(self, type, value, traceback):
        self.driver.quit()

    def render_page(self, url):
        driver.get(url)
        self._wait()
        return driver.page_source()

    def _wait(self):
        time.sleep(20)
