import scrapy
from bs4 import BeautifulSoup

from mkr1.items import HotlineItem


class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = [f"https://hotline.ua/ua/computer/noutbuki-netbuki/?p={page}" for page in range(1, 5)]


    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")

        for item in items:
            name = item.find(name="a", class_="item-title").find(
                string=True, recursive=False).strip()
            url = item.find(name="a", class_="item-title").get("href")
            price = item.find(class_="list-item__value-price").find(
                string=True, recursive=False)
            image_url = item.find(name="img").get("src")

            yield HotlineItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://hotline.ua{image_url}"]
            )


        pass
