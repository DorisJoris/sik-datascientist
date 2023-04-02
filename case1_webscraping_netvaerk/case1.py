
from case1_webscraping_netvaerk.hepler_functions import get_external_urls_from_internal_links, get_base_url


import math
import networkx as nx

sik_Graph = nx.Graph()

sik_url = "https://www.sik.dk"

sik_Graph.add_node(sik_url, orden=0)

sik_external_urls2 = get_external_urls_from_internal_links(sik_url)


#According to Siteefy.com there are around 1.132.268.801 websites on the internet,
#of which only around 18% are active.
#If we naively assume that the number of external websites that sik.dk links to is representative of
#the average number of external links on any website and that all websites link to random external websites,
#we can caluculate the expected maximum degree of separation between sik.dk and any other website on the internet,
#as follows:

max_degree_of_separation = math.ceil(math.log(1132268801, len(sik_external_urls)))








