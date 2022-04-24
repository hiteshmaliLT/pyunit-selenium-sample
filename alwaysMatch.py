from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time
import sys

if len(sys.argv) < 4:
    print("4 argsuments must required, 1.platform 2.browserName 3.version 4.selenium_version")

# user = "chandrajeetn"
# key = "Ste8T3IpWrPErZkJTwu8wEEbllI3LqX0DXnQnWFsR0BjzKdHh7"
# grid = "stage-hub.lambdatest.com/wd/hub"

# url = "https://mlqanormal1:WuQC25ZvNl9dUOfsoWe67qo9sAxGLIMutLSolYdwTFEpxNNZa0@stage-hub.lambdatest.com/wd/hub"

 url = "https://hiteshmlambdatest:EVhnNat5N8cksDV6LJuUtXHcmK7Vdjpb5eZE4MBV5gK1FRrJSt@hub.lambdatest.com/wd/hub"


ltOptions = {
    "browserName": sys.argv[2],
    "build": sys.argv[1] + sys.argv[2] + sys.argv[4],
    "console": True,
    "geoLocation": "US",
    "network": True,
    "platformName": sys.argv[1],
    "selenium_version": sys.argv[4],
    "version": sys.argv[3]
}

chromeOptions = webdriver.ChromeOptions()
firefoxOptions = webdriver.FirefoxOptions()
edgeOptions = webdriver.EdgeOptions()
ieOptions = webdriver.IeOptions()
operaOptions = webdriver.IeOptions()
safariOptions = webdriver.IeOptions()

print(sys.argv[2])

if sys.argv[2] == 'chrome':
    mobile_emulation = {"deviceName": "iPhone X"}
    chromeOptions.add_experimental_option("mobileEmulation", mobile_emulation)
    chromeOptions.add_argument("use-fake-ui-for-media-stream")
    chromeOptions.add_argument("use-fake-device-for-media-stream")
    chromeOptions.set_capability("browserName", DesiredCapabilities.CHROME)
    chromeOptions.set_capability("LT:Options", ltOptions)
elif sys.argv[2] == "firefox":
    firefoxOptions.set_preference("dom.webnotifications.serviceworker.enabled", False)
    firefoxOptions.set_preference("dom.webnotifications.enabled", False)
    firefoxOptions.add_argument('--headless')
elif sys.argv[2] == "edge":
    edgeOptions.set_capability("setPageLoadStrategy", "eager")
elif sys.argv[2] == "ie":
    ieOptions.set_capability("setUseTechnologyPreview", True)
    ieOptions.set_capability("ie.usePerProcessProxy", True)
    ieOptions.set_capability("requireWindowFocus", False)
    ieOptions.set_capability("ie.browserCommandLineSwitches", "-private")
    ieOptions.set_capability("ie.ensureCleanSession", True)
elif sys.argv[2] == "opera":
    opera = {"args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream"]}
    operaOptions.set_capability("OperaOptions", opera)
    operaOptions.set_capability("browserName", "opera")
elif sys.argv[2] == "safari":
    safari = {"setUseTechnologyPreview": True}
    safariOptions.set_capability("safariOptions", safari)
    safariOptions.set_capability("browserName", "safari")

args = {
    "platform": sys.argv[1],
    "browserName": sys.argv[2],
    "version": sys.argv[3],
    "selenium_version": sys.argv[4],
    "acceptInsecureCerts": True,
    "acceptSslCerts": True,
    "build": sys.argv[1] + sys.argv[2] + sys.argv[4],
    "console": "true",
    "enableNetworkThrottling": True,
    "extendedDebuging": True,
    "geoLocation": "HK",
    "headless": False,
    "network": True,
    "performance": False,
    "resolution": "1920x1080",
    "tunnel": False,
    "tunnelIdentifier": "",
    "video": True,
    "visual": False,
    "w3c": True
}
driver = None
print(chromeOptions.to_capabilities())
print(firefoxOptions.to_capabilities())
print(edgeOptions.to_capabilities())
print(ieOptions.to_capabilities())
print(DesiredCapabilities.INTERNETEXPLORER)

if sys.argv[2] == "chrome":
    for arg, value in args.items():
        chromeOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=url, options=chromeOptions)
elif sys.argv[2] == "firefox":
    for arg, value in args.items():
        firefoxOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=url, options=firefoxOptions)
elif sys.argv[2] == "edge":
    for arg, value in args.items():
        edgeOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=url, options=edgeOptions)
elif sys.argv[2] == "ie":
    for arg, value in args.items():
        ieOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=url, options=ieOptions)
elif sys.argv[2] == "opera":
    for arg, value in args.items():
        operaOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=url, options=operaOptions)
elif sys.argv[2] == "safari":
    for arg, value in args.items():
        safariOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=url, options=safariOptions)
else:
    print("wrong browserName passed")
    exit(1)

print("session created ", driver.session_id)
driver.get("https://www.google.com")
time.sleep(1)
driver.quit()
