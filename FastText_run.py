from gensim.models import FastText
import jieba
import numpy as np
import os
from word2extract import *
import codecs

def get_word_vector(word):
# 获取词向量


    word_vector = model.wv.__getitem__(word)#获取的方式，不是model[word]

    return word_vector

def get_sentence_vector(sentence):
# 句向量
    cut_words = jieba.lcut(sentence)

    sentence_vector = None

    for word in cut_words:
        word_vector = get_word_vector(word)

        if sentence_vector is not None:
            sentence_vector += word_vector
        else:
            sentence_vector = word_vector

    sentence_vector = sentence_vector / len(cut_words)

    return sentence_vector

def get_txt_vector(txt):
# 文本向量
    Content_txt=open(txt,'r',encoding='utf-8').read()
    cut_words = jieba.lcut(Content_txt)

    sentence_vector = None

    for word in cut_words:
        word_vector = get_word_vector(word)

        if sentence_vector is not None:
            sentence_vector += word_vector
        else:
            sentence_vector = word_vector

    sentence_vector = sentence_vector / len(cut_words)

    return sentence_vector


def cos_sim(vector_a, vector_b):####但是太高了，基本上全是99%，所以本文不用
# 计算余弦相似度
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

def simlarityCalu(vector1,vector2):
    # try:
        vector1Mod=np.sqrt(vector1.dot(vector1))
        vector2Mod=np.sqrt(vector2.dot(vector2))
        if vector2Mod!=0 and vector1Mod!=0:
            simlarity=(vector1.dot(vector2))/(vector1Mod*vector2Mod)####修改过了，注意一下！！！！
            # if simlarity==0.9999999999999999or simlarity==1.0000000000000002or simlarity==1.0:
            #     simlarity=(vector1.dot(vector2))/(vector1Mod*vector2Mod)-0.01*vector1Mod
        # else:
        #     simlarity=0
            return simlarity
        else:
            return 0



path_jib = "E:\\实体归一化_01\\疾病gather\\万方加百度筛选后的疾病"
files= os.listdir(path_jib)
model = FastText.load('E:\万方文献\data\先分词次去停用\wf_mag_fasttest.model.bin')


if __name__ == "__main__":
    # a = get_sentence_vector("头疼而且有点呕吐")测试是否可以用########
    # b = get_sentence_vector("最近头疼眼花")
    # print(cos_sim(a, b))测试是否可以用########


    ##创建过度文本
    p1_keywords = 'E:\万方文献\data_test\P11_keywords.txt'
    p2_keywords = 'E:\万方文献\data_test\P12_keywords.txt'
    p1_keywords_new='E:\万方文献\data_test\P11_keywords_new.txt'

    #输入名称
    jbms=input('请输入要查找的疾病名称：')
    JBMS=jbms.split(' ')

    for jb in JBMS:

            compare_list = []
            print('                     ')

            pvec_list=[]
            p1 = 'E:\\实体归一化_01\\疾病gather\\好大夫搜索测试600\\'+jb+'.txt'

            compare = {}
            getKeywords(p1, p1_keywords)
            with open(p1_keywords, 'r',encoding='utf-8')as fi:
                key_word=fi.readlines()
                for j in key_word:
                    p1_keywords_newkey=j.replace('\\n','')
                    pvec_list.append(j)
            with open(p1_keywords_new,'w',encoding='utf-8')as fp:
                pvec_list_str=str(pvec_list).replace('\\n','').replace("'",'').replace(',','').replace('[','').replace(']','').replace('    ','').replace('   ','').replace('  ','').replace(' ','',1)

                fp.write(pvec_list_str)

            p1_vec =get_txt_vector(p1_keywords_new)
            print(p1_vec)

            for file in files:  # 遍历文件夹
                f = os.path.basename(file)
                name_s = f.replace('.txt', '')

                # print(name)
                p2 = path_jib + '\\' + f
                # print(f)输出名称，可以看出来到了哪个出了问题
                # p2 = './data/糖尿病.txt'
                getKeywords(p2, p2_keywords)

                p2_vec = get_txt_vector(p2_keywords)
                print(p2_vec)
                try:
                    sim =simlarityCalu(p1_vec, p2_vec)
                    print(sim)
                    sim_4 = round(sim, 4)
                    compare[name_s] = sim_4
                except:
                    continue


            n = 10
        ########################################################################进行排序
            L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
            L = L[:n]
            print(jb)
            print(L)
            # print(simlarityCalu(p1_vec,p2_vec))
            with open("E:\\万方文献\\data\\先分词次去停用\\test01.txt",'a')as ft:###保存文档
                ft.write(jb+"\n")
                ft.write(str(L)+"\n")



