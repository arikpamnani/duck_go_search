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
	
class duck_go_search:	
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
		curr_page = 1

		num_results = 0
		limit_exceeded = 0	# bool	

		while(num_results < self.max_queries and (not limit_exceeded)):
			self.setup_baseURL(curr_page)
			url = self.base_url[0] + query + self.base_url[1]

			try:
				data = requests.get(url)
			except:
				print "Connection Refused."
				break
			
			html_data = html.fromstring(data.text)		

			no_result_expression = HTMLTranslator().css_to_xpath('div.result--no-result')
			no_result = html_data.xpath(no_result_expression)

			expression = HTMLTranslator().css_to_xpath('div.links_main')		
			results = html_data.xpath(expression)		

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
			
				if(result_url == ""):
					limit_exceeded = 1
					break

				self.search_results.append(search_obj)
				num_results += 1

				if(num_results >= self.max_queries):
					break
			
			curr_page += 1

if __name__ == "__main__":
	x = duck_go()
	x.set_query_limit(10)
	x.query(["table", "tennis"])
	try:
		print x.search_results[0].link
		print x.search_results[0].title
		print x.search_results[0].description
	except IndexError:
		print -1

