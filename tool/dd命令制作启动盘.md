# mac dd 命令将制作 centos7 iso usb 启动盘

标签（空格分隔）： 其他

---

查看所有的 disk

```
diskutil list
```

```
/dev/disk1
 #: TYPE NAME SIZE IDENTIFIER
 0: FDisk_partition_scheme *7.7 GB disk1
 1: Windows_NTFS 未命名 7.7 GB disk1s1
```

解除其挂载

```
diskutil unmountDisk /dev/disk2
```
用 dd 命令将 iso 写入

```
sudo dd if=/Users/jpuyy/Downloads/CentOS-7.0-1406-x86_64-Minimal.iso of=/dev/disk2 bs=1m
```
