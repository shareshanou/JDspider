# 导入tkinter模块
import tkinter as tk
# 导入pymysql模块
import pymysql
# 导入tkinter.messagebox模块
import tkinter.messagebox

# 定义一个函数，用于连接MySQL数据库，并执行SQL语句
def execute_sql(sql):
    # 连接本地的MySQL数据库，需要指定host, user, password, database等参数
    conn = pymysql.connect(host="localhost", user="root", password="123456", database="sql", charset="utf8")
    # 创建一个游标对象，用于执行SQL语句
    cursor = conn.cursor()
    # 执行SQL语句，并返回受影响的行数
    rowcount = cursor.execute(sql)
    # 提交事务，使修改生效
    conn.commit()
    # 关闭游标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
    # 返回受影响的行数
    return rowcount

# 定义一个函数，用于验证登录信息是否正确
def login():


    # 获取输入框中的用户名和密码
    username = entry_username.get()
    password = entry_password.get()
    # 判断用户名和密码是否为空
    if not (username and password):
        tk.messagebox.showwarning(title="警告", message="用户名或密码不能为空")
        return
    # 构造SQL语句，查询用户表中是否有匹配的用户名和密码
    sql = f"select * from userlogin where username = '{username}' and password = '{password}'"
    # 执行SQL语句，并获取返回的行数
    rowcount = execute_sql(sql)
    # 如果返回的行数大于0，说明登录成功，否则登录失败

    if rowcount > 0:
        tk.messagebox.showinfo(title="提示", message="登录成功")
        # 销毁登录窗口
        window_login.destroy()
        # 调用菜单窗口函数，打开菜单窗口

        menu_window()
    else:
        tk.messagebox.showerror(title="错误", message="用户名或密码错误")

# 定义一个函数，用于注册新用户
def register(elsetk=None):
    # 获取输入框中的用户名和密码

    username = entry_username.get()
    password = entry_password.get()
    # 判断用户名和密码是否为空
    if not (username and password):
        tk.messagebox.showwarning(title="警告", message="用户名或密码不能为空")
        return
    # 构造SQL语句，查询用户表中是否已经存在该用户名
    sql = f"select * from userlogin where username = '{username}'"
    # 执行SQL语句，并获取返回的行数
    rowcount = execute_sql(sql)
    # 如果返回的行数大于0，说明该用户名已被注册，否则可以注册新用户
    if rowcount > 0:
        tk.messagebox.showerror(title="错误", message="该用户名已被注册")
    else:
        # 构造SQL语句，向用户表中插入新用户的信息
        sql = f"insert into userlogin (username, password) values ('{username}', '{password}')"
        # 执行SQL语句，并获取返回的行数
        rowcount = execute_sql(sql)
        # 如果返回的行数大于0，说明注册成功，否则注册失败
        if rowcount > 0:
            tk.messagebox.showinfo(title="提示", message="注册成功")
            # 销毁注册窗口
            window_register.destroy()
            # 调用登录窗口函数，打开登录窗口
            login_window()
        elsetk.messagebox.showerror(title="错误", message="注册失败")

# 定义一个函数，用于打开登录窗口
def login_window():
    # 创建一个全局变量，用于保存登录窗口对象
    global window_login
    # 创建一个登录窗口对象
    window_login = tk.Tk()
    # 设置窗口标题
    window_login.title("登录")
    # 设置窗口大小和位置
    window_login.geometry("300x200+500+200")
    # 创建并添加一个标签，显示"用户名"
    tk.Label(window_login, text="用户名").place(x=50, y=50)
    # 创建并添加一个输入框，用于输入用户名
    global entry_username
    entry_username = tk.Entry(window_login)
    entry_username.place(x=100, y=50)
    # 创建并添加一个标签，显示"密码"
    tk.Label(window_login, text="密码").place(x=50, y=100)
    # 创建并添加一个输入框，用于输入密码，显示为"*"
    global entry_password
    entry_password = tk.Entry(window_login, show="*")
    entry_password.place(x=100, y=100)
    # 创建并添加一个按钮，用于登录，绑定login函数
    tk.Button(window_login, text="登录", command=login).place(x=100, y=150)
    #注册
    tk.Button(window_login, text="注册", command=register_window).place(x=150, y=150)

    # 进入主循环，等待用户交互
    window_login.mainloop()

# 定义一个函数，用于打开注册窗口
def register_window():
    window_login.destroy()
    # 创建一个全局变量，用于保存注册窗口对象
    global window_register
    # 创建一个注册窗口对象

    window_register = tk.Tk()
    # 设置窗口标题
    window_register.title("注册")
    # 设置窗口大小和位置
    window_register.geometry("300x200+500+200")
    # 创建并添加一个标签，显示"用户名"
    tk.Label(window_register, text="用户名").place(x=50, y=50)
    # 创建并添加一个输入框，用于输入用户名
    global entry_username
    entry_username = tk.Entry(window_register)
    entry_username.place(x=100, y=50)
    # 创建并添加一个标签，显示"密码"
    tk.Label(window_register, text="密码").place(x=50, y=100)
    # 创建并添加一个输入框，用于输入密码，显示为"*"
    global entry_password
    entry_password = tk.Entry(window_register, show="*")
    entry_password.place(x=100, y=100)
    # 创建并添加一个按钮，用于注册，绑定register函数
    tk.Button(window_register, text="注册", command=register).place(x=100, y=150)

    #window_register.destroy()

    tk.Button(window_register, text="取消", command=window_register.destroy).place(x=150, y=150)
    #window_register.destroy()
    # 进入主循环，等待用户交互
    window_register.mainloop()

# 定义一个函数，用于打开菜单窗口
def menu_window():
    import 主菜单

# 调用登录窗口函数，打开登录窗口
login_window()

