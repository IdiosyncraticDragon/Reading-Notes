# Pro Git
> record: Guiying Li

## 信息查看
```
查看目前冲突合并或是文件修改的情况：

git status

查看当前版本和父代版本和branch的情况:

git log --oneline --decorate
```

## 分支
```
在位置新建分支：

git branch xxname

注意，新建分之后不会默认切换到改分支，需要：

git checkout xxname

也可以将上面两步和在一起，一步到位：

git checkout -b xxname
```
