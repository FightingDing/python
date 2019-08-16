# -*- coding: utf-8 -*-

import json
import re
import requests
from requests import RequestException


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(html):
    pattern = re.compile('<li.*?list-item.*?data-title="(.*?)".*?data-score="(.*?)".*?>.*?<img.*?src="(.*?)".*?/>',
                         re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'title': item[0],
            'score': item[1],
            'image': item[2]
        }


def write_to_file(content):
    with open('xiaoxi.text', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False))


def main():
    url = "https://movie.douban.com/cinema/nowplaying/shanghai/"
    html = get_page(url)
    L = []
    for item in parse_page(html):
        L.append(item)
        # print(item)
        # write_to_file(item)

    L.sort(key=lambda x: x['score'], reverse=True)
    print('L.size:', L)


if __name__ == '__main__':
    main()
