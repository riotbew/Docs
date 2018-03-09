关于搭建apache+python的运行环境，网上很多文章都是用cgi方式，配置非常繁琐，把很多不相干的东西都扯了进来，都没有说到要点上。对于很多新手朋友来说，估计摸不着南北。这里采用mod_python模块的方式，都是用apt-get安装，3分钟就搞定了。

1、安装apache

如果安装了apache，确保配置没有进行大幅的修改，否则可能会有影响。如果没有安装apache，通过apt-get安装：

$ sudo apt-get install apache2
Tips：如果是自行编译安装，下面提到的配置和目录根据实际情况修改。

2、安装mod_python模块

这个模块内嵌了python解释器，apache就可以通过该模块运行python脚本，然后将内容输出到浏览器。这个模块就像个桥一样，连接apache和python。安装也非常简单，apt-get直接安装：

$ sudo apt-get install libapache2-mod-python
安装完成后，查看/etc/apache2/mods-enabled/python.load，可以看到模块已经被加载进来了，完全不用自己手动添加。

$ less /etc/apache2/mods-enabled/python.load
LoadModule python_module /usr/lib/apache2/modules/mod_python.so
3、告诉apache在碰到py后缀的文件时用python执行

修改/etc/apache2/sites-enabled/000-default配置文件，找到如下配置：

<Directory /var/www/>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride None
        Order allow,deny
        allow from all
</Directory>
如果你的配置没有改动，看到的应该和上面一样。在Directory内增加三行配置，最终如下：

<Directory /var/www/>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride None
        Order allow,deny
        allow from all
        AddHandler mod_python .py
        PythonHandler test
        PythonDebug On
</Directory>
保存后，重新启动下apache：

$ sudo /etc/init.d/apache2 restart
至此环境就全部完成了，下面进行测试下。

测试

在站点根目录/var/www/下新建hello.py文件，内容如下：

1
2
3
4
from mod_python import apache
def handler(req):
    req.write("Hello World!")
    return apache.OK
确保该文件有执行权限，为了方便直接改成777：

$ chmod 777 hello.py
用浏览器访问下该文件：

http://localhost/hello.py
如果看到hello world!就表示成功了。

小结

如果碰到问题可以查下apache的日志文件，apache的日志文件再/var/log/apache2/目录下。关于mod_python的使用问题，可以到官网查阅相关手册。有什么问题可以联系我。


faq:http://www.jb51.net/article/48827.htm
