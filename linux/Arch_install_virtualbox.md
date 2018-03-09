    在community 里面有virtualbox,可以直接安装。
　　
    sudo pacman -S virtualbox
　　sudo pacman -S qt
　　sudo pacman -S virtualbox-additions

　　把自己加入组：

　　gpasswd -a USERNAME vboxusers

　　安装必需模块:
　　rc.d setup vboxdrv
　　#或者
　　/etc/rc.d/vboxdrv setup

　　完了之后编辑 /etc/rc.conf 把 vboxdrv 加入 MODULES 
数组，以便开机启动时
　　自动加载VirtualBox的驱动。
　　MODULES=(… vboxdrv)
　　也可以手动加载模块：
　　sudo modprobe vboxdrv

　　然后启动VirtualBox:
　　virtualbox

　　guest 机器启动后默认是NAT 模式的网络，如果要使用 Bridged 
（桥接模式)的网络
　　话，得启用 vboxnetflt 模块：
　　sudo modprobe vboxnetflt

　　文件共享
　　对于 windows:
　　net use x: \\VBOXSVR\sharename

　　对于 linux guest:
　　mount -t vboxsf [-o OPTIONS] sharename mountpoint

　　选项那里可以添加上字符集,如：
　　nls=utf8
　　#或者iocharset=utf8
　　#nls 是iocharset 的新名字
　　如果要开机即连上共享的话，编辑/etc/fstab ,添加如下：
　　sharename mountpoint vboxsf uid=#,gid=# 0 0

　　uid和 gid后面要填写实际的用户id和组id.
　　一些实用命令：
　　列出虚拟主机：
　　VBoxManage list vms

　　启动虚拟主机：
　　VBoxManage startvm vm-name

　　参考资料：https://wiki.archlinux.org/index.php/VirtualBox
