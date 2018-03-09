#git入门

###删除远端分支和tag

 - 删除远程分支：

```
$ git push origin --delete <branchName>
```

 - 删除tag：

```
$ git push origin --delete tag <tagname>
```

###删除子模块：

 1. **根据路径删除子模块的记录** ```$ git rm --cached [path] ```
 
 2. **清理子模块配置** 编辑`.gitmodules`文件，将子模块的相关配置节点删除掉 

 3. **清理子模块配置** 编辑`.git/config`文件，将子模块的相关配置节点删除掉 

 4. **清理脏文件** 手动删除子模块残留的目录 
