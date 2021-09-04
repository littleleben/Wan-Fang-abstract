import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from multiprocessing import Pool
import multiprocessing

def browser_headers(url_):

    headers ={

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Cookie': 'searchHistory=W3siQ3JlYXRlVGltZSI6IjIwMjAtMDItMjBUMjI6MDE6MDkuNjUxNTc2OCswODowMCIsIkhpdENvdW50IjoxMDQ3MDIsIlVybCI6InE95a2m5L2NLeS4k-S4mj0o5YaF56eR5a2mKSbotYTmupDnsbvlnotfZmw95a2m5L2N6K665paHIiwiRmF2b3VyaXRlQ29udGVudCI6Ilt7XCJLZXlcIjpcInFcIixcIlZhbHVlXCI6XCLlrabkvY0t5LiT5LiaPSjlhoXnp5HlraYpXCJ9LHtcIktleVwiOlwi6LWE5rqQ57G75Z6LX2ZsXCIsXCJWYWx1ZVwiOlwi5a2m5L2N6K665paHXCJ9XSIsIlF1ZXJ5IjpudWxsfSx7IkNyZWF0ZVRpbWUiOiIyMDIwLTAyLTIwVDE1OjE2OjE3LjI4MTA3MjkrMDg6MDAiLCJIaXRDb3VudCI6NTI4NSwiVXJsIjoicT3lrabkvY0t5LiT5LiaPSjkurrkvZPop6PliZbkuI7nu4Tnu4fog5rog47lraYpJui1hOa6kOexu-Wei19mbD3lrabkvY3orrrmlociLCJGYXZvdXJpdGVDb250ZW50IjoiW3tcIktleVwiOlwicVwiLFwiVmFsdWVcIjpcIuWtpuS9jS3kuJPkuJo9KOS6uuS9k-ino-WJluS4jue7hOe7h-iDmuiDjuWtpilcIn0se1wiS2V5XCI6XCLotYTmupDnsbvlnotfZmxcIixcIlZhbHVlXCI6XCLlrabkvY3orrrmlodcIn1dIiwiUXVlcnkiOiLlrabkvY0t5LiT5LiaPSjkurrkvZPop6PliZbkuI7nu4Tnu4fog5rog47lraYpIn0seyJDcmVhdGVUaW1lIjoiMjAyMC0wMi0yMFQxNToxNDozNS41NjU0MTU1KzA4OjAwIiwiSGl0Q291bnQiOjUyODUsIlVybCI6InE95a2m5L2NLeS4k-S4mj0o5Lq65L2T6Kej5YmW5LiO57uE57uH6IOa6IOO5a2mKSbotYTmupDnsbvlnotfZmw95a2m5L2N6K665paHIiwiRmF2b3VyaXRlQ29udGVudCI6Ilt7XCJLZXlcIjpcInFcIixcIlZhbHVlXCI6XCLlrabkvY0t5LiT5LiaPSjkurrkvZPop6PliZbkuI7nu4Tnu4fog5rog47lraYpXCJ9LHtcIktleVwiOlwi6LWE5rqQ57G75Z6LX2ZsXCIsXCJWYWx1ZVwiOlwi5a2m5L2N6K665paHXCJ9XSIsIlF1ZXJ5Ijoi5a2m5L2NLeS4k-S4mj0o5Lq65L2T6Kej5YmW5LiO57uE57uH6IOa6IOO5a2mKSJ9XQ2; Hm_cv_af200f4e2bd61323503aebc2689d62cb=1*searchResultCreatorLink*searchResultCreatorLink; Hm_lvt_af200f4e2bd61323503aebc2689d62cb=1582206978,1582207105,1582208486,1582259742; Hm_lpvt_af200f4e2bd61323503aebc2689d62cb=1582263795; WFMed.Auth=%7b%22Context%22%3a%7b%22AccountIds%22%3a%5b%5d%2c%22Data%22%3a%5b%5d%2c%22SessionId%22%3a%225b834638-6dd8-4b25-b18f-72187196b0b5%22%2c%22Sign%22%3anull%7d%2c%22LastUpdate%22%3a%222020-02-21T05%3a43%3a16Z%22%2c%22TicketSign%22%3a%22fCfZooLONAeFzAjdzne5uA%3d%3d%22%7d',
        'Host': 'med.wanfangdata.com.cn',
        'Referer': 'http://med.wanfangdata.com.cn/Periodical/gxbjyxyjysj',
           }
    request =urllib.request.Request(url=url_,headers=headers)


    content = urllib.request.urlopen(request).read().decode()


    return content




def worker(url_single):


    single_content = browser_headers(url_single)
    s_soup = BeautifulSoup(single_content, 'lxml')
    s_abstracts = s_soup.findAll('div', class_='abstracts')
    # print(s_abstracts)

    for s_abs in s_abstracts:
        URL_ALL_CONCENT.append(s_abs.get_text())



# ##测试
# if __name__ == '__main__':
#     URL_ALL_CONCENT = []
#
#     url_single=['http://med.wanfangdata.com.cn/Paper/Detail/PeriodicalPaper_jcyxylc201703014']
#     for i in url_single:
#
#         worker(i)
#
#         print(str(URL_ALL_CONCENT))
#         f = open('F:\\万方文献爬取\\wf_mag_Concent_ALLnew近5年.txt', 'a')
#         f.write(str(URL_ALL_CONCENT))
#         f.close()



if __name__ == '__main__':
    f = open('F:\\万方文献爬取\\wf_mag_urlnew近5年_去英文后.txt', 'r')
    URL_NEW_ALL = eval(f.read())

    URL_ALL_CONCENT = []
    # pool = multiprocessing.Pool(processes=8)
    num_i = 0
    for url_single in URL_NEW_ALL:
        # print(url_single)
        num_i=num_i+1
        try:
            worker(url_single)
        except:
            continue

        if num_i%10==0:
            print('完成%d个'%num_i)

        if URL_ALL_CONCENT:
            f = open('F:\\万方文献爬取\\wf_mag_Concent_ALLnew近5年_去英文后.txt', 'a')
            f.write(str(URL_ALL_CONCENT)+'\n')
            f.close()
            URL_ALL_CONCENT = []
        else:
            continue

        if num_i==30000:
            break




