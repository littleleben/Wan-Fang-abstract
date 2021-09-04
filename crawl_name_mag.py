import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


def browser_headers(url_):

    headers ={

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    }
    request =urllib.request.Request(url=url_,headers=headers)

    content = urllib.request.urlopen(request).read().decode()

    return content



def collect_homepage(i):
    url_model = 'med.wanfangdata.com.cn/Periodical/Subject?class=R{}'.format(i)
    p_n=range(1,2)###每个类别取多少页
    for p in p_n:
        try:
            url_add_num= url_model +'&p='+str(p)
            url_new = 'http://' +url_add_num

            return url_new
        except:
            continue


def parse_content(content):
    content_list = []

    soup_h3 =BeautifulSoup(content,'lxml')
    s_h3 = soup_h3.findAll('h3')
    # print(s_h3)

    href_re=re.compile('<a href="(.*?)" target')
    href_concent=href_re.findall(str(s_h3))

    for i in href_concent:
        Name_mag.append(i)






if __name__ == '__main__':
    Name_mag=[]###保存最后的英文名称，以便于后期的匹配对应的杂志

    R_num=[3,4,5,6,71,72,73,74,75,76,77,78]###不同的主页标记，如R=1，R=2...

    ###可以匹配网页摘出这些标记
    #去掉以下内容
    ###1是预防医学、卫生学
    ###2是中医医学
    ###8是特种医学
    ###9是药学
    ###A是大学学报
    ###T是医药卫生总论
    for i in R_num:
        url_c=collect_homepage(i)
        # print(url_c)
        url_c_concent=browser_headers(url_c)
        parse_content(url_c_concent)
    print(Name_mag)
    f=open('F:\\万方文献爬取\\wf_mag_Name_1页.txt','w')
    f.write(str(Name_mag))

