from scrapy import Spider, Item, Field

class Repo(Item):
    name = Field()

class DockerHubSpider(Spider):
    name, start_urls = 'dockerhubspider', ['https://registry.hub.docker.com/search?q=a&page=1&n=100&s=stars']

    def parse(self, response):
        return [Repo(name=str(e.extract()).strip()) for e in response.css("h2::text")]
