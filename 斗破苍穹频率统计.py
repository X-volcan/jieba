# 我的第一个python文件
import jieba
import jieba.analyse

jieba.analyse.set_stop_words("stop_words.txt")  #加载停词文件，跳过某些词不统计
jieba.load_userdict("userdict.txt")  #加载自定义字典
dict = {}
text = ''
path = 'D:/VsCode/jieba分词/dpcq.txt'  #处理文件的路径，也可直接在源代码目录下选择“文件名称+后缀”
file = open(path, encoding='gb18030')
for line in file:  #去掉空格
    line = line.strip()
    text += line
w = jieba.analyse.extract_tags(text, topK=20,
                               withWeight=True)  #里面的数据是元组形式：（“关键字”，权值）
i = 1
with open('word.txt', 'w') as os:
    for line in w:  #通过循环来访问生成器
        os.write(str(i) + '.')  #只是为了表明序号
        for a in line:  #双重循环来写入数据
            os.write(str(a))  #写入必须是字符串型，对于浮点数类型的权值得先进行转换
            os.write('\t')
        i += 1
        os.write('\n')