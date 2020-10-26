from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep


class TwitterCrawler(unittest.TestCase):
    TWITTER_URL = 'https://twitter.com/'

    def setUp(self):
        self.driver = Chrome(executable_path='../drivers/chromedriver')

    def test_search_twitter(self):
        self.driver.get('{}search?q=کرونا'.format(self.TWITTER_URL))

    def test_find_search_element(self):
        self.driver.get('{}explore'.format(self.TWITTER_URL))
        search_box = self.driver.find_element_by_xpath('//input[@data-testid="SearchBox_Search_Input"]')
        search_box.send_keys('کرونا')
        search_box.clear()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
