from tkinter import ttk#导入 tkinter 的 ttk 模块，它提供了一些主题化的控件
from tkinter import filedialog as fd
import requests#导入 requests 模块，它允许你发送 HTTP 请求
import time
import tkinter.messagebox as msgbox#导入 tkinter.messagebox 模块，它提供了各种消息框
import threading#导入 threading 模块，它允许你创建和管理线程
import pymysql#导入 pymysql 模块，它允许你连接和操作 MySQL 数据库
from pandas.io import json#导入 json 模块，它允许你编码和解码 JSON 数据
from tkinter import *#导入 tkinter 的所有内容，它提供了基本的控件和常量
from PIL import ImageTk, Image # 导入PIL库来支持jpg和png格式的图片,
import random#导入 random 模块，它提供了各种随机数生成器
from tkinter import Tk, StringVar, Entry, Radiobutton, Button, Canvas, messagebox#导入 tkinter 的一些特定控件，如 Tk, StringVar, Entry, Radiobutton, Button, Canvas, messagebox
import csv#导入 csv 模块，它允许你读写 CSV 文件
import math#导入 math 模块，它提供了各种数学函数和常量
import tkinter as tk
import pandas as pd
import re#导入 re 模块，它提供了正则表达式操作
import jieba
import PIL.Image#导入 PIL.Image 模块，它允许你创建和打开图像
import numpy as np
import wordcloud#导入 wordcloud 模块，它允许你从文本数据生成词云
import matplotlib.pyplot as plt
from gensim import corpora, models#导入 gensim 的 corpora 和 models 模块，它们提供了文本分析和主题建模的工具
import tkinter as tk#以 tk 为别名导入 tkinter 模块，这样可以简化代码的书写
from tkinter import filedialog#导入 tkinter 的 filedialog 模块，它提供了打开和保存文件的对话框
import pandas as pd#以 pd 为别名导入 pandas 模块，它提供了用于处理表格数据的数据结构和分析工具
from os import path
import jieba#导入 jieba 模块，它提供了中文文本分词的工具
import numpy as np#以 np 为别名导入 numpy 模块，它提供了用于科学计算的数值数组和操作
import matplotlib.pyplot as plt#以 plt 为别名导入 matplotlib 的 pyplot 模块，它提供了用于数据可视化的绘图函数



# 创建主窗口
frame_plow = tk.Tk()
frame_plow.title('爬虫程序')
frame_plow.geometry('780x600')
# 创建一个Notebook组件
notebook = ttk.Notebook(frame_plow)
notebook.pack(fill='both', expand=True)
# 创建第一个标签页，用于显示菜单页面
frame_menu = tk.Frame(notebook)
notebook.add(frame_menu, text='欢迎页面')
#设置顶部
frame_top = tk.Frame(frame_menu)
frame_top.pack(side="top", fill="x")


# 使用time模块
import time
local_time = time.localtime() # 获取当地时间
format_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time) # 格式化时间
print(format_time) # 输出时间

# 使用datetime模块
import datetime
now_time = datetime.datetime.now() # 获取当前日期和时间
format_time = now_time.strftime('%Y-%m-%d %H:%M:%S') # 格式化时间
print(format_time) # 输出时间
label_username = tk.Label(frame_top, text="时间："+format_time) # 使用登陆注册.py文件中的username变量
label_username.pack(side="left", padx=10)
label_welcome = tk.Label(frame_top, text="欢迎使用20级八班cheems小组开发的京东爬虫！")
label_welcome.pack(side="left")
def exit():
    frame_plow.destroy()
button_help = tk.Button(frame_top, text="退出",command=exit) # 使用函数
button_help.pack(side="right", padx=10)

#-----------------------爬取id-------------------------
frame_plowid = tk.Frame(notebook)
notebook.add(frame_plowid, text='爬取id')
# 创建一个文本框对象，用于显示输出结果
textid = tk.Text(frame_plowid)
textid.config(width=100, height=2)
# 将文本框对象放置在窗口的指定位置
textid.place(x=50, y=200)
def search():
    # 获取输入的网址
    url = entry.get()
    # 发送请求，获取响应
    response = requests.get(url)
    # 提取HTML代码
    html = response.text
    # 定义正则表达式，匹配商品ID
    pattern = re.compile(r'/(\d+).html')
    # 从HTML代码中搜索商品ID
    match = pattern.search(html)
    # 如果找到了商品ID，显示在标签上
    if match:
        item_id = match.group(1)
        labelid.config(text="商品ID是：" + item_id)
        textid.insert(tk.END, "商品ID是：" + item_id + "\n")
    else:
        labelid.config(text="没有找到商品ID")
# 创建输入框
entry = tk.Entry(frame_plowid)
entry.pack()
# 创建按钮
button = tk.Button(frame_plowid, text="搜索", command=search)
button.pack()
# 创建标签
labelid = tk.Label(frame_plowid, text="输入商品网址获取商品ID")
labelid.pack()
#-----------------------京东爬虫-------------------------

frame_jdmain = tk.Frame(notebook)
notebook.add(frame_jdmain, text='京东爬虫')
frame_jd = tk.Frame(frame_jdmain)
frame_jd.pack()

def jd_crawl_comment(item_id, pagenum):
    list_ = []
    start_page = 1
    end_page = pagenum
    for p in range(start_page, end_page + 1):
        print(p)
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv995&productId=' + str(
            item_id) + '&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'
        url = url.format(p)
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            #'Referer': 'https://item.jd.com/1981570.html'
        }
        content = requests.get(url=url, headers=headers).content.decode('gbk')
        content = content.strip('fetchJSON_comment98vv995();')
        print(content)
        obj = json.loads(content)
        comments = obj['comments']
        print(comments)
        fp = open('jingdong.txt', 'a', encoding='utf-8')
        for comment in comments:
            name = comment['referenceName']
            id = comment['id']
            con = comment['content']
            creationTime = comment['creationTime']
            img_url = comment['userImageUrl']
            score = comment['score']
            item = {
                'name': name,
                'id': id,
                'con': con,
                'time': creationTime,
                'img_url': img_url,
            }
            string = str(item)

            print(id, con, score, creationTime)
            list_.append([id, con, score, creationTime])
            fp.write(string + '\n')

        fp.close()
        print('%s-page---finish' % p)
        time.sleep(5)
    return list_
def write_to_csv(list_, header, outputfile):
    with open(outputfile, 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for l in list_:
            writer.writerow(l)
    f.close()
def run():

    item_id = entry11.get()
    pagenum = entry12.get()
    outputfile = entry13.get()

    try:
        item_id = int(item_id)
        pagenum = int(pagenum)
        assert outputfile.endswith(".csv")
    except:

        msgbox.showerror("错误", "输入错误，请检查输入是否正确。")
        return

    loading_label.config(text="恭喜你运行成功")

    t = threading.Thread(target=executecore, args=(item_id, pagenum, outputfile))
    t.start()

def executecore(item_id, pagenum, outputfile):

    list_ = jd_crawl_comment(item_id, pagenum)
    header = ['id', '评论', '打分', '时间']
    write_to_csv(list_, header, outputfile)

def clear():
    entry11.delete(0, tk.END)
    entry12.delete(0, tk.END)
    entry13.delete(0, tk.END)

title_label = tk.Label(frame_jd, text="京东评论爬虫", font=("Arial", 16))
title_label.pack()
loading_label = tk.Label(frame_jd, text="", font=("Arial", 12))
loading_label.pack()
frame = tk.Frame(frame_jd)
frame.pack()
label11 = tk.Label(frame, text="输入ID:")
label12 = tk.Label(frame, text="输入爬取页数:")
label13 = tk.Label(frame, text="输入导出文件名:")
entry11 = tk.Entry(frame)
entry12 = tk.Entry(frame)
entry13 = tk.Entry(frame)
label11.grid(row=0, column=0)
entry11.grid(row=0, column=1)
label12.grid(row=1, column=0)
entry12.grid(row=1, column=1)
label13.grid(row=2, column=0)
entry13.grid(row=2, column=1)
button1 = tk.Button(frame_jd, text="确定", command=run)
button2 = tk.Button(frame_jd, text="取消", command=clear)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)


#-----------------------评分筛查-------------------------
frame_select = tk.Frame(notebook)
notebook.add(frame_select, text='评分筛查')

frame_selecttwo = tk.Frame(frame_select)
frame_selecttwo.pack(side="top", fill="x")


# 定义一个函数，用于筛选和导出csv文件中的评论
def filter_and_export():
    # 获取输入框和选择按钮的值
    import_file = file_var.get()
    export_file = export_var.get()
    score = score_var.get()
    # 检查输入是否为空
    if not import_file or not export_file:
        messagebox.showerror("错误", "请输入文件名")
        return
    # 尝试打开输入文件
    try:
        with open(import_file, 'r',encoding='utf-8') as csv_in:
            csv_reader = csv.DictReader(csv_in)
            # 尝试创建输出文件
            try:
                with open(export_file, 'w', encoding='utf-8') as csv_out:
                    csv_writer = csv.DictWriter(csv_out, fieldnames=csv_reader.fieldnames)
                    csv_writer.writeheader()
                    # 遍历输入文件的每一行，根据打分进行筛选
                    for row in csv_reader:
                        if row['打分'] == score:
                            csv_writer.writerow(row)
                # 筛选成功，显示提示信息
                messagebox.showinfo("成功", "文件筛选成功")
            except Exception as e:
                # 创建输出文件失败，显示错误信息
                messagebox.showerror("错误", f"无法创建输出文件: {e}")
                print(e)
    except Exception as e:
        # 打开输入文件失败，显示错误信息
        messagebox.showerror("错误", f"无法打开输入文件: {e}")


# 创建输入框和选择按钮的变量
file_var = StringVar() # 输入文件名的变量
export_var = StringVar() # 输出文件名的变量
score_var = StringVar() # 选择打分的变量
score_var.set("1") # 默认值为1

# 创建输入框和选择按钮的标签和控件
file_label = tk.Label(frame_selecttwo, text="要筛选的文件名:") # 修改了这里，使用tk.Label而不是Label
file_label.grid(row=0, column=0, padx=10, pady=10)
file_entry = Entry(frame_selecttwo, textvariable=file_var) # 输入框用于输入要筛选的文件名
file_entry.grid(row=0, column=1, padx=10, pady=10)
export_label = tk.Label(frame_selecttwo, text="要导出的文件名:") # 修改了这里，使用tk.Label而不是Label
export_label.grid(row=1, column=0, padx=10, pady=10)
export_entry = Entry(frame_selecttwo, textvariable=export_var) # 输入框用于输入要导出的文件名
export_entry.grid(row=1, column=1, padx=10, pady=10)
score_label = tk.Label(frame_selecttwo, text="选择打分:") # 修改了这里，使用tk.Label而不
# 继续创建输入框和选择按钮的标签和控件
score_label = tk.Label(frame_selecttwo, text="选择打分:") # 修改了这里，使用tk.Label而不是Label
score_label.grid(row=2, column=0, padx=10, pady=10)
scores = ["1分", "2分", "3分", "4分", "5分"] # 打分的列表
for i, score in enumerate(scores):
    score_radio = Radiobutton(frame_selecttwo, text=score, variable=score_var, value=score[0]) # 选择按钮用于选择打分
    score_radio.grid(row=2, column=i+1, padx=10, pady=10)

# 创建确定按钮和取消按钮
ok_button = Button(frame_selecttwo, text="确定", command=filter_and_export) # 确定按钮用于筛选和导出文件
ok_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

#---------------------------------图片生成--------------
frame_more= tk.Frame(notebook)
notebook.add(frame_more, text='图片生成')
def 词频_京东商品评论_柱状图(inputfile, topN, output):
    f = open(inputfile, encoding='utf8')
    data = pd.read_csv(f)
    string = ''
    comments = data['评论']
    for c in comments:
        string += str(c) + '\n'
    print(string)
    txt = string
    words = jieba.lcut(txt)
    dic_ = {}
    stopwords = ['其他', '很多', '不是', '非常', '这个', '那个', '真的', '可以', '没有', "就是", "这里"]
    for word in words:
        if len(word) == 1:
            continue
        else:
            rword = word
        dic_[rword] = dic_.get(rword, 0) + 1
    for word in stopwords:
        try:
            del (dic_[word])
        except:
            pass
    items = list(dic_.items())
    items.sort(key=lambda x: x[1], reverse=True)
    labels = []
    sizes = []
    wordlist = list()
    for i in range(topN):
        word, count = items[i]
        labels.append(word)
        sizes.append(count)
        wordlist.append(word)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    f, ax = plt.subplots()
    rect = ax.barh(range(len(sizes)), sizes, tick_label='')
    plt.yticks(np.arange(len(labels)), labels)
    plt.legend((rect,), ("前"+str(topN)+"关键词",))
    plt.savefig(output)
def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    entry_filename.delete(0, 'end')
    entry_filename.insert(0, filename)
def run_词频():
    textcl.delete(1.0, tk.END)
    try:
        textcl.insert(tk.END, "加载中...\n")
        topN = int(entry_output2.get())
        output = entry_output3.get()
        词频_京东商品评论_柱状图(filename, topN, output)
        textcl.insert(tk.END, "运行成功！\n")
        textcl.insert(tk.END, "已经生成关键词柱状图")
    except Exception as ees:
        textcl.insert(tk.END, "出现错误！\n")
        textcl.insert(tk.END, str(ees) + "\n")
def dataPreprocessing(file_name):

    reviews = pd.read_csv(file_name, encoding="utf-8")
    reviews = reviews.drop_duplicates()
    content = reviews['评论']
    strinfo = re.compile('京东|头盔|帽子|商家|自营')
    content = content.apply(lambda x: strinfo.sub('', x))
    contentCut = content.apply(lambda x: list(jieba.cut(x)))
    stopWords = pd.read_csv("stop_words_chinese.txt", sep=" ", encoding="utf-8", header=None)
    stopWords = list(stopWords[0]) + ["，", ""] + ["。", ""] + ["\n", ""] + ["！", ""] + ["？", ""] + [" ", ""] + ["?", ""]
    contentStop = contentCut.apply(lambda x: [i for i in x if i not in stopWords])
    return contentStop
def create_wordcloud(contentStop, image_name):
    text = ' '.join(map(str, (contentStop)))
    img = PIL.Image.open("词云1.jpg")
    mask = np.array(img)
    wc = wordcloud.WordCloud(font_path="msyh.ttc", mask=mask, width=1000, height=700, background_color='white',
                             max_words=100)
    wc.generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    wc.to_file(image_name)
def LdaModel(contentStop): #LDA主题分析模型函数，K值取10，将分析结果输出到控制台
    # 主题分析
    content_dict = corpora.Dictionary(contentStop)  # 建立词典
    content_corpus = [content_dict.doc2bow(i) for i in contentStop]  # 建立语料库
    # 构建LDA模型
    content_lda = models.LdaModel(content_corpus, num_topics=10, id2word=content_dict)
    print("\n对评价进行LDA主题分析结果如下")
    for i in range(10):
        print("主题%d:" % i)
        print(content_lda.print_topic(i))
    # 将LDA主题分析结果统计到一个文本文件中
    with open("LDA_result.txt", "w", encoding="utf-8") as f:
        for i in range(10):  # 假设K值为10
            f.write("主题{}：\n".format(i + 1))
            for word, prob in content_lda.show_topic(i):  # 获取每个主题的前10个关键词和概率
                f.write("{}: {:.4f}\n".format(word, prob))  # 写入文件，保留四位小数
            f.write("\n")
def executee():
    image_name = entry2.get()
    textcl.delete(1.0, tk.END)
    try:
        textcl.insert(tk.END, "加载中...\n")
        contentStop = dataPreprocessing(filename)
        create_wordcloud(contentStop, image_name)

        textcl.insert(tk.END, "运行成功！\n")
        textcl.insert(tk.END, "生成的词云图片保存在" + image_name + "\n")
    except Exception as e:
        textcl.insert(tk.END, "出现错误！\n")
        textcl.insert(tk.END, str(e) + "\n")

def shujuchuli():

    textcl.delete(1.0, tk.END)
    try:
        textcl.insert(tk.END, "加载中...\n")
        contentStop = dataPreprocessing(filename)

        LdaModel(contentStop)
        textcl.insert(tk.END, "运行成功！\n")
        textcl.insert(tk.END, "已经生成LDA_result.txt文件")
    except Exception as es:
        textcl.insert(tk.END, "出现错误！\n")
        textcl.insert(tk.END, str(es) + "\n")



label_filename=tk.Label(frame_more, text='请选择您要分析的文件：')
label_filename.place(x=0,y=50)
entry_filename=tk.Entry(frame_more, width=40)
entry_filename.place(x=150,y=50)
button_browse=tk.Button(frame_more, text='浏览文件', command=browse_file)
button_browse.place(x=460,y=50)
label_output2=tk.Label(frame_more, text='输入关键词数N：')
label_output2.place(x=0,y=100)
entry_output2=tk.Entry(frame_more, width=40)
entry_output2.place(x=150,y=100)
label_output3=tk.Label(frame_more, text='词频柱状图文件名(.后缀)：')
label_output3.place(x=0,y=150)
entry_output3=tk.Entry(frame_more, width=40)
entry_output3.place(x=150,y=150)
button_词频=tk.Button(frame_more, text='点击生成词频柱状图', command=run_词频)
button_词频.place(x=460,y=150)
label2 = tk.Label(frame_more, text="输入词云文件名(.后缀)：")
label2.place(x=0,y=200)
entry2 = tk.Entry(frame_more, width=40)
entry2.place(x=150,y=200)
button = tk.Button(frame_more, text="点击生成词云", command=executee)
button.place(x=460,y=200)

label3 = tk.Label(frame_more, text="LDA主题分析模型是一种基于概率图模型的文本主题分析方法，它可以自动发现文本数据中隐藏的主题结构。")
label3.place(x=0,y=260)
button = tk.Button(frame_more, text="点击进行LDA主题分析", command=shujuchuli)
button.place(x=460,y=290)

textcl = tk.Text(frame_more)
textcl.config(width=80, height=4)
textcl.place(x=0,y=340)







#显示词云，数据图片
#-------------------------------------图片查看-----------------------
frame_picture = tk.Frame(notebook)
notebook.add(frame_picture, text='图片查看')
# 创建左侧Frame
left_frame = Frame(frame_picture, width=200, height=400)
left_frame.pack(side=LEFT, padx=10, pady=5)

# 创建右侧Frame
right_frame = Frame(frame_picture, width=500, height=600)
right_frame.pack(side=RIGHT, padx=10, pady=5)

# 创建词云按钮
cloud_button = Button(left_frame, text="词云")
cloud_button.pack(pady=5)
# 创建词云文件尾缀选择
cloud_var = StringVar()
cloud_var.set(".png")
cloud_png = Radiobutton(left_frame, text=".png", variable=cloud_var, value=".png")
cloud_jpg = Radiobutton(left_frame, text=".jpg", variable=cloud_var, value=".jpg")
cloud_png.pack()
cloud_jpg.pack()
# 创建词云文件名输入框
cloud_entry = Entry(left_frame)
cloud_entry.pack(pady=5)
# 创建关键词按钮
keyword_button = Button(left_frame, text="柱状图关键词")
keyword_button.pack(pady=5)
# 创建关键词文件尾缀选择
keyword_var = StringVar()
keyword_var.set(".png")
keyword_png = Radiobutton(left_frame, text=".png", variable=keyword_var, value=".png")
keyword_jpg = Radiobutton(left_frame, text=".jpg", variable=keyword_var, value=".jpg")
keyword_png.pack()
keyword_jpg.pack()
# 创建关键词文件名输入框
keyword_entry = Entry(left_frame)
keyword_entry.pack(pady=5)
# 创建散点图按钮

# 创建散点图文件尾缀选择

# 创建散点图文件名输入框


# 创建图片显示标签
image_label = Label(right_frame)
image_label.pack()

# 定义显示图片的函数
def show_image(button):
    # 根据不同的按钮获取对应的文件名和尾缀
    if button == "词云":
        filename = cloud_entry.get() + cloud_var.get()
    elif button == "关键词":
        filename = keyword_entry.get() + keyword_var.get()



    image = Image.open (filename).convert ('RGB')
    image = image.resize((680, 400))
    pic = ImageTk.PhotoImage (image)
    image_label.config(image=pic)
    image_label.pic = pic


# 为每个按钮添加事件处理函数
cloud_button.config(command=lambda: show_image("词云"))
keyword_button.config(command=lambda: show_image("关键词"))





frame_help= tk.Frame(notebook)
notebook.add(frame_help, text='帮助')

# 创建标签和文本框
label = tk.Label(frame_help, text="点击查询数据库")
label.pack()
texthp = tk.Text(frame_help)
texthp.pack()
# 定义查询函数
def query(db_name, table_name):
    # 连接数据库
    connection = pymysql.connect(host="localhost", user="root", password="123456", db=db_name)
    cursor = connection.cursor()
    # 执行查询语句
    sql = "select * from " + table_name
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    # 清空文本框
    texthp.delete(1.0, "end")
    # 显示查询结果
    for row in result:
        texthp.insert("end", row)
        texthp.insert("end", "\n")
    # 关闭数据库连接
    connection.close()

# 定义按钮函数
def notice():
    query("sql", "notice_table")

def jingdong():
    query("sql", "jingdong_table")

def other():
    query("sql", "help_table")

# 创建按钮
notice_button = tk.Button(frame_help, text="更新通知", command=notice)
notice_button.pack(side="left")
jingdong_button = tk.Button(frame_help, text="京东", command=jingdong)
#jingdong_button.pack(side="left")
other_button = tk.Button(frame_help, text="帮助", command=other)
other_button.pack(side="left")




# 创建画布
canvas = tk.Canvas(frame_menu)
canvas.pack(fill="both", expand=True)

# 创建一个爬虫类
class Spider:
    def __init__(self, x, y, color):
        self.x = x # 爬虫的x坐标
        self.y = y # 爬虫的y坐标
        self.color = color # 爬虫的颜色
        self.angle = random.randint(0, 359) # 爬虫的初始角度
        self.speed = random.randint(1, 2) # 爬虫的速度
        self.body = canvas.create_oval(x-10, y-10, x+10, y+10, fill=color) # 爬虫的身体
        self.legs = [] # 爬虫的腿
        for i in range(8): # 创建8条腿
            leg = canvas.create_line(x, y, x+20*math.cos(math.radians(self.angle+i*45)), y+20*math.sin(math.radians(self.angle+i*45)), fill=color)
            self.legs.append(leg)

    def move(self):
        # 计算爬虫的新坐标
        new_x = self.x + self.speed * math.cos(math.radians(self.angle))
        new_y = self.y + self.speed * math.sin(math.radians(self.angle))
        # 判断爬虫是否碰到边界，如果是，就改变角度
        if new_x < 10 or new_x > 590:
            self.angle = 180 - self.angle
        if new_y < 10 or new_y > 590:
            self.angle = 360 - self.angle
        # 更新爬虫的坐标
        self.x = new_x
        self.y = new_y
        # 移动爬虫的身体和腿
        canvas.move(self.body, self.speed * math.cos(math.radians(self.angle)), self.speed * math.sin(math.radians(self.angle)))
        for i in range(8):
            canvas.coords(self.legs[i], new_x, new_y, new_x+20*math.cos(math.radians(self.angle+i*45)), new_y+20*math.sin(math.radians(self.angle+i*45)))
# 创建一个爬虫列表
spiders = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(6): # 创建6只爬虫，每只不同颜色
    spider = Spider(random.randint(100, 500), random.randint(100, 500), colors[i])
    spiders.append(spider)

# 让爬虫动起来
while True:
    if frame_plow.winfo_exists(): # 判断窗口是否存在
        if frame_menu.winfo_exists():
            if canvas.winfo_exists(): # 判断画布是否存在
                for spider in spiders: # 遍历每只爬虫，让它移动一次
                    spider.move()
                    frame_plow.update() # 更新窗口
            else:
                    break # 退出循环

# 运行主循环
frame_plow.mainloop()