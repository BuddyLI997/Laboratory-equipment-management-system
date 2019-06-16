# Laboratory-equipment-management-system
一个本科的毕业设计

测试使用的环境：
1)操作系统：Windows10专业版
2) Python版本：Python 3.7
3) Django版本：Django版本 2.2.1
4) 浏览器：Chorme浏览器

如果使用了建表文件.sql 可以跳过下面三步。
--------------
创建数据库。
在命令行执行：python manage.py makemigrations 创建迁移文件。
然后执行：python manage.py migrate 创建数据库表格。
在MySQL数据库，LabAdmin中添加初始管理员账号。
---------------
如果使用了建表文件.sql 可以跳过上面三步。


在projects/settings.py中配置数据库：
查找下面的代码。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'lab2',         # 你要存储数据的库名，事先要创建之
        'USER': 'root',         # 数据库用户名
        'PASSWORD': '123456',     # 密码
        'HOST': 'localhost',    # 主机
        'PORT': '3306',         # 数据库使用的端口
    }
}

需要联网！！！其中网页用到部分资源没有在本地，如font-awesome图标库，可以自行下载，或者联网使用。

然后运行：python manage.py runserver即可运行。
登陆网址：http://localhost:8000/login/输入管理员密码即可登陆。
