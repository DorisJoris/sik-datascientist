
from case1_webscraping_netvaerk.hepler_functions import get_external_urls_from_internal_links, get_base_url


import math
import networkx as nx

sik_Graph = nx.DiGraph()

sik_url = "https://www.sik.dk"

sik_Graph.add_node(sik_url, orden=0)

sik_external_urls = get_external_urls_from_internal_links(sik_url)


#According to Siteefy.com there are around 1.132.268.801 websites on the internet,
#of which only around 18% are active.
#If we naively assume that the number of external websites that sik.dk links to is representative of
#the average number of external links on any website and that all websites link to random external websites,
#we can caluculate the expected maximum degree of separation between sik.dk and any other website on the internet,
#as follows:

max_degree_of_separation = math.ceil(math.log(1132268801, len(sik_external_urls)))



# This function takes in a networkx graph, a base url, a external base url and an order number 
# and adds a node for the external base url to the graph and connects it to the base url.
def add_external_url_to_graph(graph, base_url, external_base_url, orden):
    graph.add_node(external_base_url, orden=orden)
    graph.add_edge(base_url, external_base_url)
    return graph


sik_external_urls[0]

sik_Graph = add_external_url_to_graph(sik_Graph, sik_url, get_base_url(sik_external_urls[0]), 1)

sik_Graph.nodes(data=True)
sik_Graph.edges()

sik_Graph.nodes(data=False)


url_dict = {}
url_dict[sik_url] = get_external_urls_from_internal_links(sik_url)

