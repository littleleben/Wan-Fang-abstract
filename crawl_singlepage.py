

def collect_singlepage(singlename):

    url_model = 'med.wanfangdata.com.cn'

    singlename_rep = str(singlename).replace('Periodical/','PeriodicalPaper_')

    url_add_name= url_model + '/Paper/Detail' + singlename_rep


    url_new = 'http://' +url_add_name

    return url_new


def combine_url(url_new):
    # Years=range(2015,2020+1)###2015年到2020年的
    Years=range(2019,2020+1)###2019年到2020年的
    # Years = range(2004,2004 + 1)
    dates=['01','02','03','04','05','06','07','08','09','10','11','12']
    # dates=['01']

    num=[]

    for i in range(1,11):
        num.append(str(i).rjust(2, '0'))

    for y in Years:
        for d in dates:
            for n in num:
                try:
                    url_new_single=url_new+str(y)+str(d)+'0'+str(n)
                    URL_NEW_ALL.append(url_new_single)
                except:
                    continue


f = open('F:\\万方文献爬取\\wf_mag_Namewash.txt', 'r')
dict_wf_mag_Name = eval(f.read())

URL_NEW_ALL=[]


# print(dict_wf_mag_Name)

for s_name in dict_wf_mag_Name:
    url_s=collect_singlepage(s_name)

    combine_url(url_s)


print(URL_NEW_ALL)
f = open('F:\\万方文献爬取\\wf_mag_urlnew近2年_每期10篇.txt', 'w')
f.write(str(URL_NEW_ALL))


