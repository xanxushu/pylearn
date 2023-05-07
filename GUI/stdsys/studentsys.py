import tkinter 
import tkinter.messagebox
import random

global en_zh

def language():    
    lan=tkinter.Tk()
    lan.title("language preference / 语言")
    choice=tkinter.Label(lan,text="Please choose your language preference\n请选择你的语言偏好",anchor='n')
    lang=tkinter.Frame(lan)
    lan_value=tkinter.IntVar()
    chinese=tkinter.Radiobutton(lang,text="简体中文",variable=lan_value,value=1,command=lambda:changelangc(lan))
    english=tkinter.Radiobutton(lang,text="English",variable=lan_value,value=2,command=lambda:changelange(lan))
    choice.pack()
    chinese.pack()
    english.pack()
    lang.pack()
    lan.mainloop()

def changelange(lan):
    if tkinter.messagebox.askokcancel('attention','Do you want to choose English?'):
        global en_zh
        en_zh=True
        lan.destroy()

def changelangc(lan):
    if tkinter.messagebox.askokcancel('温馨提示','您确定选择简体中文吗？'):
        global en_zh
        en_zh=False
        lan.destroy()
    
def signin():
    global en_zh
    signos=tkinter.Tk()
    signos['width']=1000
    signos['height']=800
    name=tkinter.Label(signos,width=8)
    id=tkinter.Label(signos,width=8)
    id_=tkinter.Label(signos,width=8)
    def captcha():
        charlist=[]
        for i in range(48,58):
            charlist.append(chr(i))
        for j in range(65,91):
            charlist.append(chr(j))
        for k in range(97,123):
            charlist.append(chr(k))
        capnum=[]
        for num in range(0,5):
            capnum.append(random.randint(0,61))
        return charlist[int(capnum[0])]+charlist[int(capnum[1])]+charlist[int(capnum[2])]+charlist[int(capnum[3])]+charlist[int(capnum[4])]
    check=tkinter.Label(signos,width=8,text=captcha())
    checkos=tkinter.Entry(signos,width=20)
    nameos=tkinter.Entry(signos,width=20)
    idos=tkinter.Entry(signos,width=20)
    idos_=tkinter.Entry(signos,width=20)
    def isright(name,first,second,right):
        acf=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\ccount.txt","r")
        paf=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\password.txt",'r')
        accfile=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\ccount.txt","a")
        passfile=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\password.txt","a")

        if en_zh:
            if name in acf.readlines():
                if tkinter.messagebox.showerror('Error','This account has already existed'):
                    pass
            if first!=second:
                if tkinter.messagebox.showerror('Error','passwords are not the same!'):
                    pass
            if right!=check['text']:
                if tkinter.messagebox.askyesno('Error','CAPTCHA is not correct!'):
                    check['text']=captcha()
            if name not in acf.readlines() and first==second and right==check['text']:
                accfile.writelines(name)
                accfile.close()
                passfile.writelines(first)
                passfile.close()
                acf.close()
                if tkinter.messagebox.showinfo('Attention','regsiter compeleted!'):
                    pass
                signos.destroy()
        else:
            if name in acf.readlines():
                if tkinter.messagebox.showerror('警告','该账户已经存在！'):
                    pass
            if first!=second:
                if tkinter.messagebox.showerror('警告','两次密码输入不同！'):
                    pass
            if right!=check['text']:
                if tkinter.messagebox.showerror('警告','验证码不正确'):
                    check['text']=captcha()
            if name not in acf.readlines() and first==second and right==check['text']:
                accfile.writelines(name)
                accfile.close()
                passfile.writelines(first)
                passfile.close()
                acf.close()
                if tkinter.messagebox.showinfo('温馨提示','你已成功注册！'):
                    pass
                signos.destroy()
    confirm=tkinter.Button(signos,width=8,command=lambda:isright(nameos.get(),idos.get(),idos_.get(),checkos.get()))
    cancle=tkinter.Button(signos,width=8,command=lambda:signos.destroy())
    def see():
        idos['show']='*'
        idos_['show']='*'
    seen=tkinter.Button(signos,command=lambda:see())
    global en_zh
    if en_zh:
        signos.title("signin")
        name['text']='username'
        id['text']='password'
        id_['text']='again'
        confirm['text']='OK'
        cancle['text']='cancle'
        seen['text']='coverid'
    else:
        signos.title("注册")
        name['text']='用户名'
        id['text']='密码'
        id_['text']='确认密码'
        confirm['text']='确定'
        cancle['text']='取消'
        seen['text']='隐藏密码'
    name.place(x=500,y=100)
    nameos.place(x=580,y=100)
    id.place(x=500,y=150)
    idos.place(x=580,y=150)
    id_.place(x=500,y=200)
    idos_.place(x=580,y=200)
    check.place(x=500,y=250)
    checkos.place(x=580,y=250)
    confirm.place(x=500,y=350)
    cancle.place(x=600,y=350)
    seen.place(x=700,y=350)
    signos.mainloop()

def mainos():
    studentos=tkinter.Tk()
    studentos.mainloop()

    
def login():
    global en_zh
    log=tkinter.Tk()
    log['width']=1000
    log['height']=800
    name=tkinter.Label(log,width=8)
    id=tkinter.Label(log,width=8)
    nameos=tkinter.Entry(log,width=20)
    idos=tkinter.Entry(log,width=20)
    def isindata(username,password):
        acf=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\ccount.txt")
        paf=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\password.txt")
        accfile=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\ccount.txt","a")
        passfile=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\password.txt","a")

        if username in acf.readlines() and password==paf.readlines()[acf.readlines().index(username)]:
            log.destroy()
            mainos()     
        elif username not in acf.readlines():
            print(username)
            print(acf.readlines())
            if en_zh:
                if tkinter.messagebox.askyesno('Attention','You do not have an account.\nSign in now?'):
                    signin()
            else:
                if tkinter.messagebox.askyesno('温馨提示','您还没有帐户。\n要现在注册吗？'):
                    signin()
        elif username in acf.readlines() and password!=paf.readlines()[acf.readlines().index(username)]:
            if en_zh:
                if tkinter.messagebox.showinfo('Attention','password is not correct,please try again'):
                    pass
            else:
                if tkinter.messagebox.showinfo('温馨提示','密码输入错误，请重试！'):
                    pass
        acf.close()
        paf.close()
    confirm=tkinter.Button(log,width=8,command=lambda:isindata(nameos.get(),idos.get()))
    cancle=tkinter.Button(log,width=8,command=lambda:log.destroy())
    def see():
        idos['show']='*'
    seen=tkinter.Button(log,command=lambda:see())
    global en_zh
    if en_zh:
        log.title("login")
        name['text']='username'
        id['text']='password'
        confirm['text']='OK'
        cancle['text']='cancle'
        seen['text']='coverid'
    else:
        log.title("登录")
        name['text']='用户名'
        id['text']='密码'
        confirm['text']='确定'
        cancle['text']='取消'
        seen['text']='隐藏密码'
    name.place(x=500,y=350)
    nameos.place(x=580,y=350)
    id.place(x=500,y=400)
    idos.place(x=580,y=400)
    confirm.place(x=500,y=450)
    cancle.place(x=600,y=450)
    seen.place(x=700,y=450)
    
    log.mainloop()


def main():
    global en_zh
    pp=open("C:\\Users\Lenovo\OneDrive\code\python\system\GUI\stdsys\ccount.txt")
    print(pp.readlines())
    language()
    signin()
    login()

if __name__=="__main__":
    main()