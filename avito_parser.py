import requests
from time import sleep
from pprint import pprint
from selenium import webdriver
from lxml.html import fromstring
from webdriver_manager.chrome import ChromeDriverManager


def save_avito_page(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(url)
    sleep(3)
    data = driver.page_source

    with open("saved_avito_page.html", "w", encoding="utf8") as f:
        f.write(data)


def parse_avito(data):
    root = fromstring(data)

    name = root.xpath("//span[@class='title-info-title-text']/text()")[0]
    price = float(root.xpath("//span[@itemprop='price']/attribute::content")[0])
    images = root.xpath("//div[@class='gallery-img-frame js-gallery-img-frame']/attribute::data-url")
    chars_names = root.xpath("//li[@class='item-params-list-item']/span/text()")
    chars_values = root.xpath("//li[@class='item-params-list-item']/text() |"
                        "//li[@class='item-params-list-item']/a/attribute::href")

    chars_names = [n.strip() for n in chars_names]
    chars_values = [v.strip() for v in chars_values if v.strip()]

    place = root.xpath("//span[@class='item-address__string']/text()")[0].strip()
    description = root.xpath("//div[@class='item-description-text']/p/text()")[0]

    return {
        "name": name,
        "price": price,
        "euro_price": price / parse_eur(),
        "images": images,
        "chars_names": chars_names,
        "chars_values": chars_values,
        "description": description,
        "place": place,
    }


def parse_eur():
    data = requests.get("https://cbr.ru/currency_base/daily/").text
    root = fromstring(data)

    return float(root.xpath("//td[text()='Евро']/following-sibling::td/text()")[0].replace(",", "."))


if __name__ == "__main__":
    #save_avito_page("https://www.avito.ru/vladimir/avtomobili/vaz_2114_samara_2005_2341834281?utm_campaign=native&utm_medium=item_page_android&utm_source=soc_sharing_seller")
    #
    with open("saved_avito_page.html", encoding="utf8") as f:
        data = f.read()

    data = parse_avito(data)
    pprint(data)

    #print(parse_eur())

    pass







