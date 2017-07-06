## duck_go_search 1.0 
#### This API is published on - https://pypi.python.org/pypi/duck_go_search/1.0
#### A command line utility for search on duckduckgo.com
#### Building in Python (lxml + requests + urllib)
#### Dependencies -
1. ``` lxml ```
2. ``` requests ```
3. ``` urllib ```

#### API Documentation - 


#### Installation 
```
pip install duck_go_search
```


#### Use 
```python
from duck_go_search.search import duck_go_search

# creating a search object
search_obj = duck_go_search()

# setting up proxy (if any)
search_obj.setup_proxy('http', 'http://proxyserver.com:8080')
search_obj.setup_proxy('https', 'https://proxyserver.com:8080')

# setting up the limit for number of results
search_obj.set_query_limit(7)

# creating a query
search_obj.query(["keyword_1", "keyword_2"])

""" printing search results, a list 
    of search objects is returned """
    
# search link
print search_obj.search_results[0].link

# search title
print search_obj.search_results[0].title

# search description
print search_obj.search_results[0].description

# markup data 
print search_obj.search_results[0].html_data
```		
