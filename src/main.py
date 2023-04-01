from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawler.pipelines import CrawlerPipeline
from crawler.spiders.test import TestSpyder
from crawler.pipelines import items

def main():
    settings = get_project_settings()
    print(settings)
    process = CrawlerProcess(settings)

    process.crawl("MammaMia")
    process.start()
    
    print(items)

if __name__ == '__main__':
    main()