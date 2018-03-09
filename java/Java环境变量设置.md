#Java环境变量设置

 > 路径申明一般都是在/etc/profile中

```
export JAVA_HOME=/usr/share/jdk1.6.0_14
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$JAVA_HOME/bin:$PATH
```
