import json
import urllib



#url for all pages of json data
url = []
response = []
data = []

url.append("https://shopicruit.myshopify.com/admin/orders.json?page=1&access_token=c32313df0d0ef512ca64d5b336a0d7c6")
url.append("https://shopicruit.myshopify.com/admin/orders.json?page=2&access_token=c32313df0d0ef512ca64d5b336a0d7c6")
url.append("https://shopicruit.myshopify.com/admin/orders.json?page=3&access_token=c32313df0d0ef512ca64d5b336a0d7c6")


#read in json orders to data[] list
try:
	for i in range (0,3):
		response.append(urllib.urlopen(url[i]))
		data.append(json.loads(response[i].read()))
	print "Received Data"

except BaseException as e:
	print "ERROR"
	exit(1)


#place all individual orders into orders[] list
orders = []
for i in range(0, 3):
	orders += data[i]["orders"]

totalRevenue = 0


#add total_price to totalRevenue if the order has been paid and has not been cancelled
for order in orders:
	if (order["financial_status"] == "paid") and (order["cancelled_at"] == None):
		totalRevenue += float(order["total_price"])


print ("The total revenue for the Shopify store is $%.2f" %(totalRevenue))
