import sys

print("len of sys",len(sys.argv))

import time
import os
from threading import Thread
from selenium import webdriver



for i in range(0,len(sys.argv)):
	print(sys.argv[i])

username = "mlqanormal1"
access_key = "WuQC25ZvNl9dUOfsoWe67qo9sAxGLIMutLSolYdwTFEpxNNZa0"


def get_browser(caps):
	return webdriver.Remote(
            command_executor="https://{}:{}@stage-hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities=caps
        )

# You can configure your test capabilities here
# browsers = [
#     {"build": 'PyunitTest sample build bigsur Implicit',"name": "Test 17", "platform": "win10","browserName": "Firefox", "version": "82", "selenium_version": "4.1.0"},
#     {"build": 'PyunitTest sample build bigsur Implicit',"name": "Test 18", "platform": "bigsur","browserName": "Firefox", "version": "81", "selenium_version": "4.1.0"},
#     {"build": 'PyunitTest sample build bigsur Implicit',"name": "Test 19", "platform": "win11","browserName": "Firefox", "version": "80", "selenium_version": "4.1.0"}
# ]
browsers = [
	{"build": 'PyunitTest sample build bigsur Implicit',"name": "Test 1", "platform": sys.argv[1],"browserName": sys.argv[2], "version": sys.argv[3], "selenium_version": sys.argv[4]}
]

print(browsers)

browsers_waiting = []

# Running the test cases
def get_browser_and_wait(browser_data):
	print ("starting %s" % browser_data["name"])
	browser = get_browser(browser_data)
	browser.get("https://lambdatest.com")
	browsers_waiting.append({"data": browser_data, "driver": browser})
	print ("%s ready" % browser_data["name"])
	while len(browsers_waiting) < len(browsers):
		print ("browser %s sending heartbeat while waiting" % browser_data["name"])
		browser.get("https://lambdatest.com")
		browser.set_window_size(1600, 1200)
		time.sleep(10)
		print (browser.get_window_size())
		# browser.maximize_window()
		# print (browser.get_window_size())


thread_list = []
for i, browser in enumerate(browsers):
	t = Thread(target=get_browser_and_wait, args=[browser])
	thread_list.append(t)
	t.start()

for t in thread_list:
	t.join()


for i, b in enumerate(browsers_waiting):
	b["driver"].implicitly_wait(10)
	print ("Implicit wait completed")
	print ("browser %s's title: %s" % (b["data"]["name"], b["driver"].title))
	b["driver"].quit()
