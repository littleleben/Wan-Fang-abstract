# -*- coding: utf-8 -*-
import codecs
import numpy
import gensim
import numpy as np
from word2extract import *
import os
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import random
from scipy import spatial
import re
from gensim.models import KeyedVectors
from gensim.models import word2vec

wordvec_size=300



def avg_feature_vector(file_name, model):
    index2word_set = set(model.wv.index2word)
    with codecs.open(file_name, 'r') as f:
        sentence=f.read()

        words = sentence.split()
        feature_vec = np.zeros((wordvec_size, ), dtype='float32')
        n_words = 0
        for word in words:
            if word in index2word_set:
                n_words += 1
                feature_vec = np.add(feature_vec, model[word])
        if (n_words > 0):
            feature_vec = np.divide(feature_vec, n_words)
        return feature_vec

def avg_feature_vector_utf(file_name, model):
    index2word_set = set(model.wv.index2word)
    with codecs.open(file_name, 'r',encoding='utf-8') as f:
        sentence=f.read()

        words = sentence.split()
        feature_vec = np.zeros((wordvec_size, ), dtype='float32')
        n_words = 0
        for word in words:
            if word in index2word_set:
                n_words += 1
                feature_vec = np.add(feature_vec, model[word])
        if (n_words > 0):
            feature_vec = np.divide(feature_vec, n_words)
        return feature_vec






def get_char_pos(string,char):
    chPos=[]
    try:
        chPos=list(((pos) for pos,val in enumerate(string) if(val == char)))
    except:
        pass
    return chPos





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

    # print(soup)



def list_deal(list_str):
    remove_1_i_txt=list_str.replace(' ','')###去掉所有的空格
    # print(remove_blank_i_txt)
    remove_2_i_txt = str(remove_1_i_txt).replace('\n', '')  ###去掉所有的空格
    remove_3_i_txt = str(remove_2_i_txt).replace('\xa0', '')
    return remove_3_i_txt


path_jib = "E:\\实体归一化_01\\疾病gather\\万方加百度筛选后的疾病"
files= os.listdir(path_jib)


if __name__ == '__main__':

    # model = gensim.models.Word2Vec.load('E:\万方文献\data\先分词次去停用\gensim.word2vec')

    word2vec_file=open('E:\万方文献\data\先分词次去停用\gensim.txt','r')
    model = KeyedVectors.load_word2vec_format(word2vec_file, binary=False)

    p1_keywords = 'E:\万方文献\data_test\P11_keywords.txt'
    p2_keywords = 'E:\万方文献\data_test\P12_keywords.txt'
    p1_keywords_new='E:\万方文献\data_test\P11_keywords_new.txt'

    jbms=input('请输入要查找的疾病名称：')
    JBMS=jbms.split(' ')


    for jb in JBMS:

            compare_list = []
            print('                     ')

            pvec_list=[]
            p1 = 'E:\\实体归一化_01\\疾病gather\\好大夫搜索测试600\\'+jb+'.txt'

            compare = {}
            getKeywords_utf(p1, p1_keywords)
            with open(p1_keywords, 'r')as fi:
                key_word=fi.readlines()
                for j in key_word:
                    p1_keywords_newkey=j.replace('\\n','')
                    pvec_list.append(j)
            with open(p1_keywords_new,'w',encoding='utf-8')as fp:
                pvec_list_str=str(pvec_list).replace('\\n','').replace("'",'').replace(',','').replace('[','').replace(']','').replace('    ','').replace('   ','').replace('  ','').replace(' ','',1)

                fp.write(pvec_list_str)

            p1_vec =avg_feature_vector_utf(p1_keywords_new, model)
            print(p1_vec)

            for file in files:  # 遍历文件夹
                f = os.path.basename(file)
                name_s = f.replace('.txt', '')

                # print(name)
                p2 = path_jib + '\\' + f
                print(f)
                # p2 = './data/糖尿病.txt'
                getKeywords(p2, p2_keywords)

                p2_vec = avg_feature_vector(p2_keywords, model)
                print(p2_vec)
                try:
                    sim =simlarityCalu(p1_vec, p2_vec)
                    print(sim)
                    sim_4 = round(sim, 4)
                    compare[name_s] = sim_4
                except:
                    continue


            n = 10
        ########################################################################
            L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
            L = L[:n]
            print(jb)
            print(L)
            # print(simlarityCalu(p1_vec,p2_vec))
            with open("E:\\万方文献\\data\\先分词次去停用\\test01.txt",'a')as ft:
                ft.write(jb+"\n")
                ft.write(str(L)+"\n")

