# Scrapy settings for zoopla0_1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zoopla0_1'

SPIDER_MODULES = ['zoopla0_1.spiders']
NEWSPIDER_MODULE = 'zoopla0_1.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zoopla0_1 (+http://www.yourdomain.com)'

# only crawl first 2 pages
DEPTH_LIMIT = 2
