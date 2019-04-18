#!/usr/bin/env python
# coding: utf-8

# # Import libraries

# In[19]:


import urllib
from urllib.request import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[53]:


def crawl(pages, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = urllib.request.urlopen(page)
                except:
                    print ("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), "lxml")
                links = soup('a') #finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.append(url)
        pages = indexed_url
    return indexed_url


# In[63]:


pagelist=["http://yusufsn.staff.ums.ac.id/"]
urls = crawl(pagelist, depth=2)


# In[64]:


urls


# In[65]:


len(urls)


# In[ ]:




