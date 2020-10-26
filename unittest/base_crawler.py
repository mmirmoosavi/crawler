from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from time import sleep
from tqdm import tqdm


class TwitterCrawler():
    TWITTER_URL = 'https://twitter.com/'
    SCROLL_PAUSE_TIME = 4

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = Chrome(executable_path='drivers/chromedriver', options=options)

    def search_twitter(self, **kwargs):
        self.driver.get(
            '{}search?q=since:{} until:{} {} "{}"'.format(self.TWITTER_URL, kwargs['since'], kwargs['until'],
                                                           kwargs['words'], kwargs['exact_phrases']))
        sleep(self.SCROLL_PAUSE_TIME)

    def extract_all_posts(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        sleep(self.SCROLL_PAUSE_TIME)
        with tqdm() as pbar:
            while True:
                # Scroll down to bottom
                posts = self.driver.find_elements_by_xpath(
                    '//article/div/div/div/div[2]/div[2]/div[2]/div[1]/div')

                print('posts_length : ', len(posts))
                for elem in posts:
                    print(elem.text)
                    print('+++++++++++')
                print('==================')
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                sleep(self.SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                pbar.update()

    def tearDown(self):
        # self.driver.close()
        pass

if __name__ == '__main__':
    crawler = TwitterCrawler()
    crawler.setUp()
    twitter_adv_search_parameters = {'words': 'کرونا', 'exact_phrases': 'ویروس چینی', 'since': '2020-10-24',
                                     'until': '2020-10-26'}
    crawler.search_twitter(**twitter_adv_search_parameters)
    crawler.extract_all_posts()
    crawler.tearDown()
