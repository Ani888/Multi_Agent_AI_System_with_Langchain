## this main.py is to run the project locally. it central point to call

from src.tools.tools import search_web, scrape_url
from rich import print

# function calling way
# print(search_web("Latest AI news"))
# result = scrape_url("https://news.mit.edu/topic/artificial-intelligence2")
# print("scrape_url     ------------------------------------------------------" + result)

# after using  tool decorator on function now we can invoke that functions
result = search_web.invoke("Latest AI news")
print(result)


