# -*- coding: utf-8 -*-
# 百度新聞

import json
import re
import requests
from requests import RequestException
from lxml import etree


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def getXpath(html):
    return etree.HTML(html)


def write_to_file(content):
    with open('news.text', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False))


def parseXpath(xpath):
    ul = xpath.xpath('//*[@id="pane-news"]//a')
    for li in ul:
        yield {
            'title': li.xpath('text()')[0],
            'url': li.xpath('@href')[0]
        }


def main():
    url = "http://news.baidu.com/"
    html = get_page(url)
    s1 = getXpath(html)
    for item in parseXpath(s1):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()
