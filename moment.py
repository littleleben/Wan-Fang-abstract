f1=open('E:\万方文献\data\wf_mag_jieba.txt','r')
f2=open('E:\万方文献\data\wf_mag_jieba01.txt','w')

X=f1.read()
Y=X.replace('.','').replace('±','').replace('  ',' ')

f2.write(Y)