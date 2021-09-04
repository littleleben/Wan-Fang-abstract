frow = open('/home/littleleben/一些小文件/实体归一化（2019）/万方文献/data/wf_mag_washdone01.txt', 'r')
fnow= open('/home/littleleben/一些小文件/实体归一化（2019）/万方文献/data/wf_mag_washdone02.txt', 'w')

Concent=frow.read()
Concent_new=Concent.replace('n','').replace('篇','').replace('大学','')


fnow.write(Concent_new)