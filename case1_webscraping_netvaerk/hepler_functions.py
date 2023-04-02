from bs4 import BeautifulSoup as bs
import requests

# This function requests a url and returns a beautiful soup object
def get_soup(url):
    html = requests.get(url).text
    soup = bs(html, "html.parser")
    return soup

# This function returns a list of hrefs from all a tags in a beautiful soup object
def get_hrefs(soup):
    hrefs = []
    for a in soup.find_all("a"):
        if a.has_attr("href"):
            hrefs.append(a['href'])
    return hrefs

# This function sorts out hrefs that are urls. 
# It takes a list of hrefs as input.
def sort_hrefs(hrefs):
    urls = []
    for href in hrefs:
        if href.startswith("http"):
            urls.append(href)
    return list(set(urls))

# This function extracts the base url from a url
def get_base_url(url):
    base_url = url.split("/")[0] + "//" + url.split("/")[2]
    return base_url

# This function takes in a list of urls and a base url returns a list of external urls
def sort_external_internal_urls(urls, base_url):
    external_urls = []
    internal_urls = []
    for url in urls:
        if not url.startswith(base_url):
            external_urls.append(url)
        else:
            internal_urls.append(url)
    return list(set(external_urls)), list(set(internal_urls))

# This function takes in a base_url and loops through all internal links on the page and collects all external urls
def get_external_urls_from_internal_links(base_url):
    soup = get_soup(base_url)
    hrefs = get_hrefs(soup)
    urls = sort_hrefs(hrefs)
    external_urls, internal_urls = sort_external_internal_urls(urls, base_url)

    for internal_url in internal_urls:
        soup = get_soup(internal_url)
        hrefs = get_hrefs(soup)
        new_urls = sort_hrefs(hrefs)
        new_external_urls, new_internal_urls = sort_external_internal_urls(new_urls, base_url)
        for new_internal_url in new_internal_urls:
            if new_internal_url not in internal_urls:
                internal_urls.append(new_internal_url)
        
        external_urls = list(set(external_urls + new_external_urls))

    return external_urls



sik_external_urls2 = get_external_urls_from_internal_links("https://www.sik.dk")
len(sik_external_urls2)

sik_external_urls2

sik_external_urls3 = get_external_urls_from_internal_links('https://boligejer.dk/ejerskifteforsikring')

sik_external_urls3