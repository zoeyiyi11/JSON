import json
import urllib

url = []
response = []
data = []

url.append("https://shopicruit.myshopify.com/admin/orders.json?page=1&access_token=c32313df0d0ef512ca64d5b336a0d7c6")
url.append("https://shopicruit.myshopify.com/admin/orders.json?page=2&access_token=c32313df0d0ef512ca64d5b336a0d7c6")
url.append("https://shopicruit.myshopify.com/admin/orders.json?page=3&access_token=c32313df0d0ef512ca64d5b336a0d7c6")


try:
	for i in range (0,3):
		response.append(urllib.urlopen(url[i]))
		data.append(json.loads(response[i].read()))

	print "Data received"
except BaseException as e:
	print "ERROR"
	exit(1)

#print data
orders = []
for i in range(0, 3):
	orders += data[i]["orders"]

print orders[49]["id"]

totalRevenue = 0

for order in orders:
	if (order["financial_status"] == "paid") and (order["cancelled_at"] == None):
		totalRevenue += float(order["total_price"])

print totalRevenue