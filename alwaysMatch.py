from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time
import sys

if len(sys.argv) < 4:
    print("4 argsuments must required, 1.platform 2.browserName 3.version 4.selenium_version")

username = "mlqanormal1"
access_key = "WuQC25ZvNl9dUOfsoWe67qo9sAxGLIMutLSolYdwTFEpxNNZa0"
grid = "stage-hub.lambdatest.com/wd/hub"

sdOptions = {"deviceName": "mobile", "deviceShortName": "m", "runId": "1v85xg", "siteConfig": {
    "authoritativeCountries": [
        "HKG"
    ],
    "canonicalDomain": "hk.20220411.dynamic.prometheus.sd.co.uk/hk-en/",
    "currency": "HKD",
    "defaultCountryCode": "HKG",
    "defaultLocale": "en-HK",
    "deliveryCountries": [
        {
            "code": "HKG",
            "name": "Hong Kong",
            "taxExcluded": True,
            "taxRate": 0
        }
    ],
    "orderNumberPrefix": "SUPERDRYHKEN"
}}

cjson = {
    "app": {
        "name": "HKG",
        "version": "en-HK"
    },
    "device": "Mobile",
    "platform": {
        "name": "ios",
        "version": " "
    }
}
ltOptions = {
    "browserName": "chrome",
    "build": "master Run ID: 1v85xg Run: ZqGV19",
    "console": True,
    "geoLocation": "HK",
    "goog:chromeOptions": {
        "mobileEmulation": {
            "deviceName": "iPhone X"
        }
    },
    "network": True,
    "platformName": "Windows 11",
    "selenium_version": "4.1.0",
    "version": "99.0"
}

chromeOptions = webdriver.ChromeOptions()
firefoxOptions = webdriver.FirefoxOptions()
edgeOptions = webdriver.EdgeOptions()
ieOptions = webdriver.IeOptions()
operaOptions = {}
safariOptions = {}

print(sys.argv[2])

if sys.argv[2] == 'chrome':
    mobile_emulation = {"deviceName": "iPhone X"}
    chromeOptions.add_experimental_option("mobileEmulation", mobile_emulation)
    chromeOptions.add_argument("use-fake-ui-for-media-stream")
    chromeOptions.add_argument("use-fake-device-for-media-stream")
    chromeOptions.set_capability("browserName", DesiredCapabilities.CHROME)
    chromeOptions.set_capability("SD:Options", sdOptions)
    chromeOptions.set_capability("cjson:metadata", cjson)
    chromeOptions.set_capability("LT:Options", ltOptions)
elif sys.argv[2] == "firefox":
    firefoxOptions.set_preference("dom.webnotifications.serviceworker.enabled", False)
    firefoxOptions.set_preference("dom.webnotifications.enabled", False)
    firefoxOptions.add_argument('--headless')
elif sys.argv[2] == "edge":
    edgeOptions.set_capability("setPageLoadStrategy", "eager")
elif sys.argv[2] == "internet explorer":
    ieOptions.set_capability("setUseTechnologyPreview", True)
    ieOptions.set_capability("ie.usePerProcessProxy", True)
    ieOptions.set_capability("requireWindowFocus", False)
    ieOptions.set_capability("ie.browserCommandLineSwitches", "-private")
    ieOptions.set_capability("ie.ensureCleanSession", True)
elif sys.argv[2] == "opera":
    opera = {"args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream"]}
    operaOptions["OperaOptions"] = opera
elif sys.argv[2] == "safari":
    safari = {"setUseTechnologyPreview": True}
    safariOptions["safariOptions"] = safari

args = {
    "platform": sys.argv[1],
    "browserName": sys.argv[2],
    "version": sys.argv[3],
    "selenium_version": sys.argv[4],
    "acceptInsecureCerts": True,
    "acceptSslCerts": True,
    "build": "alwaysMatch",
    "console": "true",
    "enableNetworkThrottling": True,
    "extendedDebuging": True,
    "geoLocation": "HK",
    "headless": False,
    "network": True,
    "performance": False,
    "platformName": "Windows 11",
    "resolution": "1920x1080",
    "tunnel": False,
    "tunnelIdentifier": "",
    "userAgent": "webdriver/7.16.16",
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
    driver = webdriver.Remote(command_executor=f'https://{user}:{key}@{grid}', options=chromeOptions)
elif sys.argv[2] == "firefox":
    for arg, value in args.items():
        firefoxOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=f'https://{user}:{key}@{grid}', options=firefoxOptions)
elif sys.argv[2] == "edge":
    for arg, value in args.items():
        edgeOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=f'https://{user}:{key}@{grid}', options=edgeOptions)
elif sys.argv[2] == "internet explorer":
    for arg, value in args.items():
        ieOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=f'https://{user}:{key}@{grid}', options=ieOptions)
elif sys.argv[2] == "opera":
    for arg, value in args.items():
        operaOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=f'https://{user}:{key}@{grid}', options=operaOptions)
elif sys.argv[2] == "safari":
    for arg, value in args.items():
        safariOptions.set_capability(arg, value)
    driver = webdriver.Remote(command_executor=f'https://{user}:{key}@{grid}', options=safariOptions)
else:
    print("wrong browserName passed")
    exit(1)

print("session created ", driver.session_id)
driver.implicitly_wait(30)
driver.get("https://www.google.com")
time.sleep(1)
driver.quit()
