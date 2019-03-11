运行 python manage.py runserver 命令就可以在本机上开启一个 Web 服务器：
http://127.0.0.1:8000/

执行fab deploy 更新

创建新应用
python manage.py startapp comments
一旦更改了模型，就需要迁移数据库，以便让 Django 将更改反应到数据库中。激活虚拟环境，运行如下两条命令：

python manage.py makemigrations
python manage.py migrate


https://yyp666.github.io/tuchuang/yunqi/1.JPG