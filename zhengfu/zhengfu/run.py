from scrapy import cmdline
import logging

logging.info("begin to run crawl ...")
cmdline.execute("scrapy crawl gxb".split())
# cmdline.execute("scrapy crawl kjb".split())
# cmdline.execute("scrapy crawl sxgxt".split())
logging.info('all finished.')


# import logging
#
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings
# from twisted.internet import reactor
#
# from spiders.gxb import GxbSpider
# from spiders.kjb import KjbSpider
# from spiders.sxgxt import sxgxtSpider
#
# if __name__ == '__main__':
#     settings = get_project_settings()
#     configure_logging(settings)
#
#     runner = CrawlerRunner(settings)
#
#     runner.crawl(GxbSpider)  # 工信部
#     runner.crawl(KjbSpider)  # 科技部
#     runner.crawl(sxgxtSpider)  # 陕西省工信厅
#
#     d = runner.join()
#     d.addBoth(lambda _: reactor.stop())
#
#     # blocks process so always keep as the last statement
#     reactor.run()
#     logging.info('all finished.')
