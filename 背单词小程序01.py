from tkinter import *
import random
from tkinter import messagebox
import os, sys
os.chdir(sys.path[0])
root=Tk()
root.title("欢迎使用")
group=LabelFrame(root,text='   欢迎使用，请选择词库   \n并选好后点击左上角关闭按钮',padx=10,pady=10)
group.pack(padx=10,pady=10)
LANGS=[
    ('四级词汇',1),
    ('六级词汇',2),
    ('考研词汇',3),
    ('雅思词汇',4)]
v=IntVar()
v.set(2)
for lang,num in LANGS:
    b=Radiobutton(group,text=lang,variable=v,value=num)
    b.pack(anchor=W)
mainloop()
def trans(filename):
    f=open(filename,'r',encoding='utf-8')
    s=f.read()
    f.close()
    f=open("单词.txt",'w',encoding='utf-8')
    f.write(s)
    f.close()
if v.get()==1:
    trans('四级词汇.txt')
elif v.get()==2:
    trans('六级词汇.txt')
elif v.get()==3:
    trans('考研词汇.txt')
else:
    trans('雅思词汇.txt')

#设置框架和背景
root=Tk()
root.title('PYTHON背单词')
root['width']=300
root['height']=400
mainframe=Frame(root)
mainframe.pack()
blank=Frame(root,height=30,width=50)
blank.pack()


#设置变量
l=StringVar()   #l是剩余未背单词数
a1=StringVar()   #a1是单词
a2=StringVar()   #a2是音标
a3=StringVar()   #a3是词义
a4=StringVar()   #a4是复习时的词义提示
a5=StringVar()   #a5是复习时用户从键盘中输入的单词
a6=StringVar()   #a6输出测试结果
a7=StringVar()   #a7是回答错误时显示的正确结果
i=StringVar()    #i是当前背到的单词数
n=StringVar()    #n是本次计划背的单词数
N=StringVar()    #N显示当前复习到的单词数
nd=StringVar()   #nd是本次删除的单词数
ng=StringVar()   #ng是本次已掌握的单词数
nng=StringVar()  #nng是本次未掌握的的单词数

ng.set('0')      #将已掌握的单词初值设为0
nng.set('0')      #将未掌握的单词初值设为0

#定义createfile函数，首次运行时创建文件
def createfile(filename):
    try:
        f=open(filename,'r',encoding='utf-8')  #读取unicode格式的文件
        f.close()
    except:
        f=open(filename,'w',encoding='utf-8')   #写入unicode格式的文件
        f.write('')
        f.close()

#创建文件，用途从文件名可知
createfile('选取单词.txt')
createfile('复习.txt')
createfile('斩.txt')
createfile('已掌握单词.txt')
createfile('难词.txt')

#定义empty函数，清空中间文件
def empty():
    f3=open('复习.txt','w',encoding='utf-8')
    f3.write('')
    f3.close()
    f2=open('选取单词.txt','w',encoding='utf-8')
    f2.write('')
    f2.close()

#设置内部结构：

#第一行设置
Label(mainframe,text='python背单词',font=('楷体',25)).grid(column=1,row=0)

#第二行设置
Label(mainframe,text='剩余单词数:',height=2,font=('隶书',13))\
                 .grid(column=0,row=1,columnspan=1,sticky=('E'))
Label(mainframe,textvariable=l,width=10,height=2,font=('隶书',13))\
            .grid(row=1,column=1)
f1=open('单词.txt','r',encoding='utf-8')
s1=f1.read()
s1=s1.strip()
f1.close()
words=s1.split('\n')
l.set(str(len(words)))

#第三行设置
Label(mainframe,text='本次共背',height=2,font=('隶书',13)).grid(row=2,column=0,sticky=('E'))
entry1=Entry(mainframe,textvariable=n,width=18)\
                                    .grid(row=2,column=1)
n.set(' ')
Label(mainframe,text='个单词',height=2,font=('隶书',13)).grid(row=2,column=2,sticky=('W'))

#第四行设置
#定义begin函数,开始背单词
def begin(*args):        #*args传入参数
    empty()              #调用empty函数，防止因用户随机终止背诵任务而在中间文件内残留数据
    n1=int(n.get())
    f1=open('单词.txt','r',encoding='utf-8-sig')  #encoding='utf-8-sig',防止开头出现错误字符“\ufeff”
    s1=f1.read()
    s1=s1.strip()
    f1.close()
    words=s1.split('\n')                        #读取单词表
    rd=random.sample(range(0,len(words)),n1)   #生成n个随机数，对应n个单词的编号
    i.set(1)                               
    word=words[rd[0]].split('/')               #word中包含单词，音标和词义
    a1.set(word[0])                        #将第一个单词显示出来
    a2.set(word[1])
    a3.set(word[2])
    f2=open('选取单词.txt','w',encoding='utf-8') #将n个单词放入名为"选取单词"的文件中
    for j in range(0,n1):                  
        str1=words[rd[j]]+'\n'
        f2.write(str1)
    f2.close()

bt1=Button(mainframe,text='开始',command=begin,bg='lightblue',width=15,height=2,font=('隶书',13))\
     .grid(row=3,column=1)                      #设置“开始”按钮,调用begin函数

#第五行设置
Label(mainframe,text='当前第  ',height=2,font=('隶书',13))\
            .grid(column=0,row=4,columnspan=1,sticky=('E'))
Label(mainframe,textvariable=i,width=1)\
                    .grid(row=4,column=1)
Label(mainframe,text='个单词',height=2,font=('隶书',13))\
        .grid(column=2,row=4,columnspan=1,sticky=('W'))

#第六行设置
Label(mainframe,text='单词    ',height=2,font=('宋体',13)).grid(row=5,column=0,sticky=('W','E'))
Label(mainframe,text='音标',height=2,font=('宋体',13)).grid(row=5,column=1)
Label(mainframe,text='词义  ',height=2,font=('宋体',13)).grid(row=5,column=2,sticky=('W','E'))

#第七行设置
Label(mainframe,textvariable=a1,width=50,font=('宋体',13),fg='purple')\
            .grid(row=6,column=0,sticky=E)
Label(mainframe,textvariable=a2,width=30,font=('宋体',13),fg='purple')\
            .grid(row=6,column=1,sticky=('W','E'))
Label(mainframe,textvariable=a3,width=50,font=('宋体',13),fg='purple')\
            .grid(row=6,column=2,sticky=W)

#第八行设置
#定义Next函数，背下一个单词
def Next(*args):
    f2=open('选取单词.txt','r',encoding='utf-8')
    s2=f2.read()
    s2=s2.strip()                        #strip()方法去除文本前后的换行符
    f2.close()
    words=s2.split('\n')                 #将单词放入名为words的列表中
    if len(words)>0:
        f3=open('复习.txt','a+',encoding='utf-8')  #弹出words中的第一个单词，并放入名为"复习"的文件中
        str3=words.pop(0)+'\n'
        f3.write(str3)
        f3.close()
        f2=open('选取单词.txt','w',encoding='utf-8')  #去掉"选取单词"文件中的第一个单词
        str2='\n'.join(words)
        f2.write(str2)
        f2.close()
    if int(i.get())==int(n.get()):       #表明背完了单词
        messagebox.showinfo("提示","你已经背完了，快去复习吧！")   #弹出小窗口
    else:
        word=words[0].split('/')      #word中包含单词，音标和词义
        a1.set(word[0])               #显示下一个单词
        a2.set(word[1])
        a3.set(word[2])
        k=int(i.get())
        i.set(str(k+1))               #i的值增加1

bt2=Button(mainframe,text='下一个',command=Next,width=15,bg='lightblue',height=2,font=('隶书',13))\
                                          .grid(row=7,column=2)  #设置“下一个”按钮，调用Next函数

#定义delete函数，删除过于简单的单词
def delete(*args):
    f2=open('选取单词.txt','r',encoding='utf-8')
    s2=f2.read()
    s2=s2.strip()                       #strip()方法去除文本前后的换行符
    f2.close()
    words=s2.split('\n')                #将单词放入名为words的列表中
    str4=words.pop(0)+'\n'
    f4=open('斩.txt','a+',encoding='utf-8')  #打开文件"斩"，将"选取单词"文件中的第一个单词添加进去
    f4.write(str4)
    f4.close()
    if int(i.get())==int(n.get()):       #表明背完了单词
        messagebox.showinfo("提示","你已经背完了，快去复习吧！")   #弹出小窗口
    else:
        word=words[0].split('/')      #word中包含单词，音标和词义
        a1.set(word[0])               #显示下一个单词
        a2.set(word[1])
        a3.set(word[2])
        k=int(i.get())
        i.set(str(k+1))               #i的值增加1
        f2=open('选取单词.txt','w',encoding='utf-8')  #去掉"选取单词"文件中的第一个单词
        str2='\n'.join(words)
        f2.write(str2)
        f2.close()    

bt3=Button(mainframe,text='斩！',command=delete,width=15,bg='lightblue',height=2,font=('隶书',13))\
                            .grid(row=7,column=0)

#定义dif函数，把较难的词汇加入“难词.txt”
def dif(*args):
    string=a1.get()+'/'+a2.get()+'/'+a3.get()+'\n'
    f=open('难词.txt','a+',encoding='utf-8')
    f.write(string)
    f.close()

Button(mainframe,text='加入难词本',command=dif,width=15,bg='lightblue',height=2,font=('隶书',13))\
                            .grid(row=7,column=1)

#第九行设置

#定义check函数，建议输入的单词是否正确
def check(*args):
    f3=open('复习.txt','r',encoding='utf-8')
    s3=f3.read()
    s3=s3.strip()
    words=s3.split('\n')
    word=words[0].split('/')
    Label(mainframe,text='正确答案是：',height=2,font=('隶书',13))\
                            .grid(column=0,row=11,columnspan=1)
    a7.set(word[0])
    answer=a5.get()
    answer=answer.strip()    #去掉回车而产生的换行符
    word[0]=word[0].strip()  #去掉空格
    if word[0]==answer:
        a6.set('回答正确！')
        f5=open('已掌握单词.txt','a+',encoding='utf-8')    #将拼写正确的单词放入"已掌握单词"文件中
        str5=words.pop(0)+'\n'
        f5.write(str5)
        f5.close()
        ng1=int(ng.get())     #掌握单词数加一
        ng.set(str(ng1+1))
    else:
        a6.set('回答错误！')
        nng1=int(nng.get())     #未掌握单词数加一
        nng.set(str(nng1+1))
        del words[0]          #直接将未掌握的单词删除
    str3='\n'.join(words)
    f3=open('复习.txt','w',encoding='utf-8')
    f3.write(str3)
    f3.close()

#定义Next1函数，复习下一个单词
def Next1(*args):
    if int(N.get())==int(n.get())-int(nd.get()):
        messagebox.showinfo("提示","本次单词背诵结束！点击‘确定’后显示背诵情况")
        
        empty()  #清空中间文件，避免对下次背单词产生干扰
        
        f1=open('单词.txt','r',encoding='utf-8-sig')   #把已掌握的单词和已删除的单词从单词.txt中删除
        s1=f1.read()
        f1.close()
        f4=open('斩.txt','r',encoding='utf-8')
        s4=f4.read()
        s4=s4.strip()
        words4=s4.split('\n')
        f5=open('已掌握单词.txt','r',encoding='utf-8')
        s5=f5.read()
        s5=s5.strip()
        words5=s5.split('\n')
        if words4!=['']:
            for i in words4:
                if i in s1:
                    i=i+'\n'
                    s1=s1.replace(i,'')
        if words5!=['']:
            for j in words5:
                if j in s1:
                    j=j+'\n'
                    s1=s1.replace(j,'')
        if v.get()==1:
            f=open('四级词汇.txt','w',encoding='utf-8')
            f.write(s1)
            f.close()
        elif v.get()==2:
            f=open('六级词汇.txt','w',encoding='utf-8')
            f.write(s1)
            f.close()
        elif v.get()==3:
            f=open('考研词汇.txt','w',encoding='utf-8')
            f.write(s1)
            f.close()
        else :
            f=open('雅思词汇.txt','w',encoding='utf-8')
            f.write(s1)
            f.close()
        f1=open('单词.txt','w',encoding='utf-8')
        f1.write('')
        f1.close()

        import matplotlib.pyplot as plt
        plt.rcParams['font.sans-serif']=['SimHei']
        sizes=int(nd.get()),int(ng.get()),int(nng.get())
        labels1='已斩单词','已掌握单词','未掌握单词'
        colors1='red','blue','yellow'
        plt.pie(sizes,labels=labels1,colors=colors1,autopct='%2.3f%%')
        plt.axis('equal')
        plt.title("背诵情况饼图",color='green',fontsize=25)
        plt.show()

    else:
        a6.set('')
        a7.set('')        #将上一个单词的相关信息去除,避免干扰答题
        f3=open('复习.txt','r',encoding='utf-8')
        s3=f3.read()
        s3=s3.strip()
        f3.close()
        words=s3.split('\n')
        rdint=random.randint(1,len(words))-1
        rdword=words[rdint]
        rdword1=rdword.split('/')
        a4.set(rdword1[2])                  #打开"复习"文件，随机选出一个单词，显示其词义
        words[0],words[rdint]=words[rdint],words[0]   #将随机选出的单词放在words开头，方便查找
        f3=open('复习.txt','w',encoding='utf-8')      #将words重新写入"复习"文件
        f3.write('\n'.join(words))
        f3.close()
        k=int(N.get())
        N.set(str(k+1))

#定义review函数，开始复习,并显示出接下来的几行
def review(*args):
    if int(i.get())<int(n.get()):
        messagebox.showinfo("提示","单词还没背完呢！")
    else:
        a1.set(' ')         #把正在显示的单词清空，避免干扰答题
        a2.set(' ')
        a3.set(' ')
        i.set(' ')
        
        Label(mainframe,text='请根据词义拼写出该单词(输入后回车)：',height=2,font=('隶书',13))\
                                .grid(column=0,row=9,columnspan=1) #第九行和第十行设置
        Label(mainframe,textvariable=a4,height=2,font=('隶书',13))\
                                .grid(column=0,row=10,columnspan=1)
        entry2=Entry(mainframe,textvariable=a5,width=18)\
                                .grid(row=10,column=1)
        
        root.bind('<Return>',check)                #通过回车键调用check()函数
        
        Button(mainframe,text='下一个',command=Next1,width=15,bg='lightblue',height=2,font=('隶书',13))\
                                .grid(column=2,row=10)  #第十一行和十二行设置
        Label(mainframe,textvariable=a6,height=2,font=('隶书',13))\
                                .grid(column=2,row=11,columnspan=3)#达到点击“复习”后才出现这几行的效果
        Label(mainframe,textvariable=a7,height=2,font=('隶书',13))\
                                .grid(column=1,row=11,columnspan=1)
        
        f3=open('复习.txt','r',encoding='utf-8')
        s3=f3.read()
        s3=s3.strip()
        f3.close()
        words=s3.split('\n')
        length=len(words)
        rdint=random.randint(1,len(words))-1
        rdword=words[rdint]
        rdword1=rdword.split('/')
        a4.set(rdword1[2])                  #打开"复习"文件，随机选出一个单词，显示其词义
        words[0],words[rdint]=words[rdint],words[0]   #将随机选出的单词放在words开头，方便查找
        f3=open('复习.txt','w',encoding='utf-8')      #将words重新写入"复习"文件
        f3.write('\n'.join(words))
        f3.close()
        n1=int(n.get())
        nd.set(str(n1-length))            #计算本次删除的单词数
        N.set('1')                #当前复习第一个单词
   
bt4=Button(mainframe,text='复习',command=review,width=15,bg='lightblue',height=2,font=('隶书',13))\
                            .grid(row=8,column=1) 
root.mainloop()

