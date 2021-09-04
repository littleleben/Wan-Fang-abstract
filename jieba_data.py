import jieba

L=[]
space=' '
fr = open('E:\万方文献\data\wf_mag_Concent_ALL.txt', 'r',encoding='utf-8')
Concent_txt=fr.readlines()

fwd = open('E:\万方文献\data\wf_mag_jieba.txt', 'a')

def stopwordslist():
    stopwords = [line.strip() for line in open('E:\万方文献\data\stopword.txt', encoding='gbk').readlines()]
    return stopwords


def seg_depart(sentence):
    # 对文档中的每一行进行中文分词

    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

for line in Concent_txt:
    line_seg = seg_depart(line)
    fwd.write(line_seg + '\n')




fr.close()
fwd.close()
print('success!!!')