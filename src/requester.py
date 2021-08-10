import requests
from multiprocessing import Pool
from os import cpu_count


class Requester:
    def __init__(self):
        self.results_of_requests = None
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/99.0.7113.93 Safari/537.36'

    def get_page(self, page_num):
        url = f'https://vkfaces.com/vk/users/100/1/{page_num}'
        return requests.get(url, headers={'User-Agent': self.user_agent}).text

    def execution(self, page_num):
        with Pool(cpu_count()) as pool:
            self.results_of_requests = pool.map(self.get_page,
                                                range(1, page_num // 2 if page_num > 3 else page_num + 1))
        return self.results_of_requests
