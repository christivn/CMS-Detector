import requests

cmsData = [
    ["Woocommerce",["/woocommerce/assets/","/wp-content/","/wp-includes/"]],
    ["Wordpress",["/wp-content/","/wp-includes/"]],
    ["Joomla",["/templates/","joomla"]],
    ["Drupal",["/sites/default/","/themes/"]],
    ["Prestashop",["/modules/","prestashop"]],
    ["Wix",["wix","/unpkg/"]],
    ["Weebly",["\"www.weebly.com\""]],
    ["Jimdo",["jimdo","/cms/"]],
    ["Godaddy Builder",["/isteam/","wsimg.com"]],
    ["IONOS Builder",["ionos-brand"]]
]

def analyze(url):
    if "https://" or "http://" not in url:
        url = "https://"+url

    cmsDetected = "None"

    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)
        html = response.text.lower()

        for i in range((len(cmsData))):
            if cmsDetected!="None": break
            icounter = 0
            for x in range(len(cmsData[i][1])):
                if cmsData[i][1][x] in html:
                    icounter+=1
                else:
                    break
                if icounter == len(cmsData[i][1]):
                    cmsDetected = cmsData[i][0]
                    break

        return cmsDetected
    except:
        return cmsDetected