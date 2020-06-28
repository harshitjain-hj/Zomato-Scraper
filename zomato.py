import csv
import requests
from lxml import html
import itertools

filepath = 'rest.csv'
writer = csv.writer(open(filepath, 'w'))

writer.writerow(['Type', 'Company name', 'Dining Rating', 'Dining Review', 'Delivery Rating', 'Delivery Review', 'Cuisines', 'Zone', 'Address', 'Cost', 'Timing', 'Call'])

##### only for the first time ########
# header=['rest_type','rest_name','rest_score','rest_votes','rest_reviews','rest_cuisine','rest_zone','rest_addressrest_cost','rest_timings',
# 'rest_featured_in','rest_call']
# writer.writerow(header)

def oneDArray(x):
	return list(itertools.chain(*x))


cookies = {
	'fbcity': '3',
	'zl': 'en',
	'fbtrack': '348ec2207b3d6c55a7ca231d677e419a',
	'_ga': 'GA1.2.1124886037.1475382045',
	'dpr': '1',
	'fbm_288523881080': 'base_domain=.zomato.com',
	'zhli': '1',
	'squeeze': 'e6c1d9490c106fc68a20b1907a41e849',
	'orange': '5768794',
	'__utmx': '141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:',
	'__utmxx': '141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1486207870:8035200',
	'PHPSESSID': '1549cf5ac03934a92c821460668aa0a21c9e8972',
	'__jpuri': 'https%3A//www.zomato.com/mumbai/lunch',
}

headers = {
	'Host': 'www.zomato.com',
	'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
}
print('Enter the URL')
url = input()
url = url+'?nearby=0&page='
# url = 'https://www.zomato.com/ncr/tilak-nagar-delhi-restaurants?nearby=0&page='
print('Total Pages')
limit = input()
rest_type = []
rest_name = []
rest_dinin_rate = []
rest_dinin_review = []
rest_delivery_rate = []
rest_delivery_review = []
rest_cuisine = []
rest_zone = []
rest_address = []
rest_cost = []
rest_timings = []
rest_featured_in = []
rest_call = []

final_row = []

for i in range(1, int(limit)+1):
	response = requests.get(url+str(i), headers=headers, cookies=cookies)#,cookies=cookies
	
	tree = html.fromstring(response.content)
	page_limit = int(tree.xpath('count(//*[@id="orig-search-list"]/div[*])'))
	print(page_limit)
	
	for j in range(1, page_limit):
		rest_type_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/div[1]/*/text()')
		if not rest_type_value:
			rest_type_value = ['empty']
		rest_type.append(rest_type_value)

		rest_name_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[1]/text()')
		if not rest_name_value:
			rest_name_value=['empty'] 
		rest_name.append(rest_name_value)

		rest_diningrate_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/text()')
		if not rest_diningrate_value:
			rest_diningrate_value=['empty']
		rest_dinin_rate.append(rest_diningrate_value)

		rest_diningreview_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span[2]/text()')
		if not rest_diningreview_value:
			rest_diningreview_value=['empty']
		rest_dinin_review.append(rest_diningreview_value)
		
		rest_deliveryrate_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+ ']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/span[1]/text()')
		if not rest_deliveryrate_value:
			rest_deliveryrate_value=['empty']
		rest_delivery_rate.append(rest_deliveryrate_value)

		rest_deliveryreview_value = tree.xpath('//*[@id="orig-search-list"]/div[' + str(
			j) + ']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/span[2]/text()')
		if not rest_deliveryreview_value:
			rest_deliveryreview_value = ['empty']
		rest_delivery_review.append(rest_deliveryreview_value)

		rest_zone_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[2]/b/text()') 
		if not rest_zone_value:
			rest_zone_value=['empty']
		rest_zone.append(rest_zone_value)
		
		rest_address_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[1]/div/div[2]/div[2]/div/text()') 
		if not rest_address_value:
			rest_address_value=['empty']
		rest_address.append(rest_address_value)

		rest_cuisine_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[3]/div[1]/span[2]/*/text()')
		if not rest_cuisine_value:
			rest_cuisine_value=['empty']
		rest_cuisine.append(rest_cuisine_value) 

		rest_cost_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[3]/div[2]/span[2]/text()') 
		if not rest_cost_value:
			rest_cost_value=['empty']
		rest_cost.append(rest_cost_value)

		rest_timings_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[3]/div[3]/div[1]/text()') 
		if not rest_timings_value:
			rest_timings_value=['empty']
		rest_timings.append(rest_timings_value)

		rest_featured_in_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[3]/div[4]/div/*/text()') 
		if not rest_featured_in_value:
			rest_featured_in_value=['empty']
		rest_featured_in.append(rest_featured_in_value)

		rest_call_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[2]/a[1]/@data-phone-no-str') 
		if not rest_call_value:
			rest_call_value = ['empty']
		rest_call.append(rest_call_value)
		
		rest_type = oneDArray(rest_type)
		rest_name = oneDArray(rest_name)
		rest_dinin_rate = oneDArray(rest_dinin_rate)
		rest_dinin_review = oneDArray(rest_dinin_review)
		rest_delivery_rate = oneDArray(rest_delivery_rate)
		rest_delivery_review = oneDArray(rest_delivery_review)
		rest_cuisine = oneDArray(rest_cuisine)
		rest_zone = oneDArray(rest_zone)
		rest_address = oneDArray(rest_address)
		rest_cost = oneDArray(rest_cost)
		rest_timings = oneDArray(rest_timings)
		rest_featured_in = oneDArray(rest_featured_in)
		rest_call = oneDArray(rest_call)

		rest_type = [word for word in rest_type]
		rest_name = [word.encode('utf-8').strip() for word in rest_name]
		# rest_dinin_rate = [word.encode('utf-8').strip() for word in rest_dinin_rate]
		# rest_dinin_review = [word.encode('utf-8').strip() for word in rest_dinin_review]
		# rest_delivery_rate = [word.encode('utf-8').strip() for word in rest_delivery_rate]
		# rest_delivery_review = [word.encode('utf-8').strip() for word in rest_delivery_review]
		rest_cuisine = [word for word in rest_cuisine]
		rest_zone = [word.encode('utf-8').strip() for word in rest_zone]
		rest_address = [word.encode('utf-8').strip() for word in rest_address]
		rest_cost = [word.encode('utf-8').strip() for word in rest_cost]
		rest_timings = [word for word in rest_timings]
		# rest_featured_in = [word.strip() for word in rest_featured_in]
		rest_call = [word.encode('utf-8').strip() for word in rest_call]

		final_row.append(', '.join(rest_type))
		final_row.append(rest_name[0].decode("utf-8"))
		final_row.append(rest_dinin_rate[0])
		final_row.append(rest_dinin_review[0])
		final_row.append(rest_delivery_rate[0])
		final_row.append(rest_delivery_review[0])
		final_row.append(', '.join(rest_cuisine))
		final_row.append(rest_zone[0].decode("utf-8"))
		final_row.append(b', '.join(rest_address))
		final_row.append(rest_cost[0].decode("utf-8"))
		final_row.append(rest_timings[0].replace("\n", "").replace("  ", ""))
		# final_row.append(rest_featured_in)
		final_row.append(rest_call[0].decode("utf-8").replace(" ", "").replace("+91", ""))

		writer.writerow(final_row)
		
		rest_type = []
		rest_name = []
		rest_dinin_rate = []
		rest_dinin_review = []
		rest_delivery_rate = []
		rest_delivery_review = []
		rest_cuisine = []
		rest_zone = []
		rest_address = []
		rest_cost = []
		rest_timings = []
		rest_featured_in = []
		rest_call = []

		final_row = []
