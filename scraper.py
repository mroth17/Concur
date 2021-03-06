# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://open.concur.com/")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
count = 0
for normal in root.cssselect("#us_content > div > div.col-sm-7.col-xs-6.col-md-9.scrollable.nopadding > table > tbody > tr:nth-child(1) > td:nth-child(3) > div"):
  count = count + 1
  
 
  
  
#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['normal'], data=count)
#
# # An arbitrary query against the database
#scraperwiki.sql.select("* from data where 'name'='NORMAL symbol'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
