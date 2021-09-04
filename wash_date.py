import re


# def stopwordslist():
#     stopwords = [line.strip() for line in open('E:\万方文献\data\stopword.txt', encoding='gbk').readlines()]
#     return stopwords
#
# fr = open('E:\万方文献\data\wf_mag_Concent_ALL.txt', 'r',encoding='utf-8')
# fwd= open('E:\万方文献\data\wf_mag_wash01.txt', 'a')
# Waitwash=fr.readlines()
#
#
# stopwords=stopwordslist()
#
# outstr=[]
# space=' '
# for single_waitwash in Waitwash:
#     for word in single_waitwash:
#         if word not in stopwords:
#             outstr.append(word)
#     print(outstr)
#     fwd.write(str(outstr) + '\n')
#
# fwd.close()


fr2= open('E:\万方文献\data\wf_mag_wash01.txt', 'r')
fwd2=open('E:\万方文献\data\wf_mag_wash02.txt', 'w')
Wash_2=fr2.read()
Wash_Done1=Wash_2.replace("'",'').replace('摘','').replace('要','').replace('n','').replace(',','').replace(' ','').replace('[','').replace(']','')
Wash_Done2=re.sub('[a-zA-Z]','',Wash_Done1)
fwd2.write(Wash_Done2)

