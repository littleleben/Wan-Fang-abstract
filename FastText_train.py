from gensim.models import FastText

def my_function():
    train_file='E:\万方文献\data\先分词次去停用\wf_mag_jieba.txt'
    corpus=open(train_file, 'r')
    model = FastText(corpus,sg=1,size=200, window=3, min_count=1, iter=10, min_n=3, max_n=6, word_ngrams=0)
    model.save('E:\万方文献\data\先分词次去停用\wf_mag_fasttest.model.bin')

if __name__ == '__main__':
    my_function()