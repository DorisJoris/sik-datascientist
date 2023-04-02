from case1_webscraping_netvaerk.hepler_functions import get_soup, get_hrefs, sort_links, get_external_urls
from case1_webscraping_netvaerk.hepler_functions import get_external_urls_from_internal_links


import math
import networkx as nx

sik_Graph = nx.Graph()

sik_url = "https://www.sik.dk"

sik_Graph.add_node(sik_url, orden=0)

sik_soup = get_soup(sik_url)
sik_hrefs = get_hrefs(sik_soup)
sik_internal_links, sik_urls = sort_links(sik_hrefs)
sik_external_urls = get_external_urls(sik_urls, sik_url)
len(sik_external_urls)
sik_external_urls2 = get_external_urls_from_internal_links(sik_url)


#According to Siteefy.com there are around 1.132.268.801 websites on the internet,
#of which only around 18% are active.
#If we naively assume that the number of external websites that sik.dk links to is representative of
#the average number of external links on any website and that all websites link to random external websites,
#we can caluculate the expected maximum degree of separation between sik.dk and any other website on the internet,
#as follows:

max_degree_of_separation = math.ceil(math.log(1132268801, len(sik_external_urls)))







sik_internal_links[3:12]
sik_urls[3:12]
len(sik_external_urls)


