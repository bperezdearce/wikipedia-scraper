import scrapy
import html
import re  
import unicodedata 
import csv
from bs4 import BeautifulSoup  

class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    start_urls = ["https://es.wikipedia.org/wiki/Wikipedia:Art%C3%ADculos_destacados"]

    def parse(self, response):
        articles = response.css('.div-col.columns.column-width a')[:10] 

        for article in articles:
            title = article.css("::text").get()
            link = response.urljoin(article.attrib["href"])

            yield response.follow(link, callback=self.parse_article, meta={"title": title, "link": link})

    def parse_article(self, response):
        title = response.meta["title"]
        link = response.meta["link"]

        primer_parrafo_html = response.css("p").get()
        primer_parrafo = ""

        if primer_parrafo_html:
            soup = BeautifulSoup(primer_parrafo_html, "html.parser")

            for sup in soup.find_all("sup"):
                sup.extract()

            primer_parrafo = soup.get_text(separator=" ", strip=True)

        primer_parrafo = html.unescape(primer_parrafo)
        primer_parrafo = unicodedata.normalize("NFKC", primer_parrafo)
        primer_parrafo = re.sub(r"[\xa0\u200b\u200c\u200d]", " ", primer_parrafo)
        primer_parrafo = re.sub(r"\s+", " ", primer_parrafo)
        primer_parrafo = re.sub(r"\s([,.])", r"\1", primer_parrafo)
        primer_parrafo = primer_parrafo.strip()

        with open("articulos.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([title, primer_parrafo, link])

        yield {
            "titulo": title,
            "primer_parrafo": primer_parrafo,
            "url": link
        }