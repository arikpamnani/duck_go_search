## duck_go_search 1.0
#### A command line utility for search on duckduckgo.com
#### Building in Python (lxml + requests + urllib)
#### API Documentation - 


#### Installation 
```python
pip install duck_go_search
```


#### Use 
```python
from duck_go_search.search import duck_go_search

# creating a search object
search_obj = duck_go_search()

# setting up proxy (if, any)
search_obj.setup_proxy('http', 'http://proxyserver.com:8080')
search_obj.setup_proxy('https', 'https://proxyserver.com:8080')

# setting up the limit for number of results
search_obj.set_query_limit(7)

# creating a query
search_obj.query(["keyword_1", "keyword_2"])

# printint the search results
print search_obj.search_results[0].link
print search_obj.search_results[0].title
print search_obj.search_results[0].description
print search_obj.search_results[0].html_data
```		
