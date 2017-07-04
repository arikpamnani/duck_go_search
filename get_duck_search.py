import requests
import urllib
from lxml import html, etree
import time
from cssselect import HTMLTranslator
from urlparse import urlsplit

class Error(Exception):
	""" Base class for Exceptions """
	pass

class SearchError(Error):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message

class SearchReturn(object):
	""" class for returning 
		search objects """

	def __init__(self):
		self.link = ""
		self.title = ""
		self.description = ""
		self.html_data = ""

	def __str__(self):
		return self.link
	
class DuckDuckGoSearch:	
	def setup_baseURL(self, page):
		""" This function returns a URL for the
			corresponding page """
		
		if(page == 1):
			self.base_url = ["https://duckduckgo.com/html/?q=", "&s=&dc=&v=l&o=json&api=/d.js"]	
		else:
			num = (page-1)*30
			foo = "&s=" + str(num) + "&dc=" + str(num+1) + "&v=l&o=json&api=/d.js"
			self.base_url = ["https://duckduckgo.com/html/?q=", foo]

	def setup_proxy(self, protocol, proxy_server):
		""" This function sets up the proxy
			server parameters """

		if(protocol not in self.proxy_dict):
			self.proxy_dict[protocol] = proxy_server
		
	def clean_url(self, url):
		""" Cleans the URL -> removes front 
			hashes and %xx from the URL """
		
		http_index = url.find("http")
		url = url[http_index:]		
		cleaned_url = urllib.unquote(url)
		return cleaned_url

	def set_query_limit(self, num):
		""" Set the maximum query limit,
			default = 5 """

		if(num > 0):
			self.max_queries = num
		else:
			print "Query limit must be greater than 0!"

	def __init__(self):
		""" initialize parameters """

		self.proxy_dict = {}
		self.max_queries = 5
		self.page_to_start = 1		
		self.base_url = ["", ""]

		# array of SearchReturn objects
		self.search_results = []

	def query(self, keywords):
		""" Returns the title, links, 
			desc by performing a 
			query on the given keywords """

		query = "+".join(keywords)
		url = self.base_url[0] + query + self.base_url[1]
		print url

		try:
			data = requests.get(url)
		except:
			print "Connection Refused."
			
		html_data = html.fromstring(data.text)		

		no_result_expression = HTMLTranslator().css_to_xpath('div.clear: both')
		no_result = html_data.xpath(no_result_expression)
		print len(no_result)

		expression = HTMLTranslator().css_to_xpath('div.links_main')		
		results = html_data.xpath(expression)		

		num_results = 0
		page_number = 1

		for result in results:
			search_obj = SearchReturn()		

			title_path = HTMLTranslator().css_to_xpath('a.result__a')
			title_element = result.xpath(title_path)
			try:
				search_obj.title = title_element[0].text_content()
			except:
				search_obj.title = ""

			desc_path = HTMLTranslator().css_to_xpath('a.result__snippet')
			desc_element = result.xpath(desc_path)
			try:
				search_obj.description = desc_element[0].text_content().encode('utf-8')
			except:
				search_obj.description = ""
			
			try:
				result_url = desc_element[0].attrib['href']
			except:
				result_url = ""
			search_obj.link = self.clean_url(result_url)

			search_obj.html_data = data.text
			
			self.search_results.append(search_obj)

			# num_results += 1
			# if(num_results >= self.max_queries):
			#	break

if __name__ == "__main__":
	x = DuckDuckGoSearch()
	# x.setup_proxy("http", "http://proxy.iiit.ac.in:8080")
	# x.setup_proxy("https", "https://proxy.iiit.ac.in:8080")
	x.setup_baseURL(2)
	x.query(["library"])
	print x.search_results[30]

