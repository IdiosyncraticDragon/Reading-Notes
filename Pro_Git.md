# Pro Git
> record: Guiying Li

## 信息查看
- 查看用户配置信息
```
>git config user.name
>git config user.email
>git config --list
```
- 查看目前冲突合并或是文件修改的情况：
```
git status
```
- 查看当前版本和父代版本和branch的情况:
```
git log --oneline --decorate
```
- 查看作为提交对象的远程服务器
```
git remote -v
```
结果实例：
```
> git remote -v
origin  liguiying@211.86.151.136:~/gitProject/Dynamic-Network-Surgery.git (fetch)
origin  liguiying@211.86.151.136:~/gitProject/Dynamic-Network-Surgery.git (push)
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

## 撤销最近修改
用git checkout – file可以丢弃工作区的修改：
```
git checkout -- readme.txt
```
命令git checkout – readme.txt意思就是，把readme.txt文件在工作区的修改全部撤销，这里有两种情况：
- 一种是readme.txt自修改后还没有被放到暂存区，撤销修改就回到和版本库一模一样的状态；
- 一种是readme.txt已经添加到暂存区后，又作了修改，撤销修改就回到添加到暂存区后的状态。
总之，就是让这个文件回到最近一次git commit或git add时的状态。

## 临时存放修改 stash
使用git的时候，我们往往使用branch解决任务切换问题，例如:
- 我们往往会建一个自己的分支去修改和调试代码, 如果别人或者自己发现原有的分支上有个不得不修改的bug，我们往往会把完成一半的代码 commit提交到本地仓库，然后切换分支去修改bug，改好之后再切换回来。这样的话往往log上会有大量不必要的记录。其实如果我们不想提交完成一半或者不完善的代码，但是却不得不去修改一个紧急Bug，那么使用
```
> git stash
```
就可以将你当前未提交到本地（和服务器）的代码推入到Git的栈中，这时候你的工作区间和上一次提交的内容是完全一样的，所以你可以放心的修 Bug，等到修完Bug，提交到服务器上后，再使用
```
git stash apply
```
将以前一半的工作应用回来。也许有的人会说，那我可不可以多次将未提交的代码压入到栈中？答案是可以的。当你多次使用'git stash'命令后，你的栈里将充满了未提交的代码，这时候你会对将哪个版本应用回来有些困惑，
```
git stash list
```
命令可以将当前的Git栈信息打印出来，你只需要将找到对应的版本号，例如使用
```
git stash apply stash@{1}
```
就可以将你指定版本号为stash@{1}的工作取出来，当你将所有的栈都应用回来的时候，可以使用
```
git stash clear
```
来将栈清空。

## git pull 冲突
- 先将本地修改存储，使用git stash
```
>git stash
```
- 将server上的信息pull下来
```
>git pull
```
- 还原之前存储的修改，解决冲突
```
git stash pop stash@{0}
```
系统提示如下类似的信息：
```
Auto-merging c/environ.c
CONFLICT (content): Merge conflict in c/environ.c
```
意思就是系统自动合并修改的内容，但是其中有冲突，需要解决其中的冲突。
- 解决文件中的冲突
在文件中，会通过如下的记号标记发生冲突的地方
```
<<<<<<<<<<<<<< Updated upstream
        xxxxxxxxx
===========
        yyyyyyyyy
>>>>>>>>>>>>>> Stashed change
```
手动修改
