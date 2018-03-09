# 常用Linux命令

 - 在某种类型文件中查到某个文件

`find ./ -name "*.class" | xargs grep 'AppRegistry' -l`

 - 新增Manjaro 中文输入法问题解决
```
首先：安装中文输入法：pacman -S fcitx fcitx-libpinyin kcm-fcitx

接着：修改.xporfile

添加内容如下：

export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
export LC_CTYPE=zh_CN.UTF-8
export XMODIFIERS=@im=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
```