# Ansible 学习

> 参考： http://ansible.com.cn/docs/intro.html 
>
> 参考： https://www.w3cschool.cn/automate_with_ansible/ 

ansible的项目地址在：https://github.com/ansible/ansible， 它只需要在一个管理机器（可以是一个个人笔记本）上安装即可，不需要在各个管理机器上安装/运行任何软件，因此非常方便。

[TOC]

## 安装

1. 从源码安装配置

开一个专门的虚拟环境（可选）：

```bash
conda create -n ansible
#激活环境
conda activate ansible
#或
source activate ansible
```

下载项目源码、安装

```bash
git clone git@github.com:ansible/ansible.git --recursive
cd ./ansible
source ./hacking/env-setup
```

2. 直接安装

   ```bash
   sudo apt-get install ansible
   ```

   或者

   ```bash
   sudo pip install ansible
   ```



## 配置

需要配置的内容包括，ssh免密、inventory和ansible.cfg配置。

### 配置管理机器与所有目标机器的ssh免密码登录

第一步:在本地机器上使用ssh-keygen产生公钥私钥对

```bash
ssh-keygen
```

第二步:用ssh-copy-id将公钥复制到远程机器中

```bash
ssh-copy-id -i .ssh/id_rsa.pub  用户名字@xx.xx.x.xxx
```

第三步，验证登录

```bash
ssh 用户名字@xx.xxx.xx.xxx
```

### 配置inventory 文件

编辑(或创建)/etc/ansible/hosts 并在其中所有需要管理的服务器ip（或者网址），这些服务器已经可以ssh免密码登录。

```
[组名（可以没有）]
xxxx.xxxx.xxx.xx
example.com
```

一台服务器可以同时属于 webserver组 和 dbserver组.这时属于两个组的变量都可以为这台主机所用.

端口号不是默认设置时,可明确的表示为:

```bash
badwolf.example.com:5309
```

更细致的设置，是给每个ip域名设定一些相关属性（例如变量名、端口等）方便在后面的playbook或者ansible使用中简化调用。

如

```bash
jumper ansible_ssh_port=5555 ansible_ssh_host=192.168.1.50
```

在这个例子中,通过 “jumper” 别名,会连接 192.168.1.50:5555。



### 配置ansible.cfg

文件位置在`/etc/ansible/ansible.cfg`。详细配置说明如下。

```cfg

```





## 使用

### 快速使用

查看全体连接

```bash
ansible all -m ping -u 用户名 --sudo
```

只查看某个组

```bash
ansible dgroup -m ping -u liguiying 
```

只查看某台机器

```bash
ansible d1 -m ping -u liguiying 
```

若有对本机操作的需求，建议于 `/etc/ansible/hosts` 补上 local 的设定。

```bash
[local]
localhost ansible_connection=local
```

远程运行命令用-m选项：

```bash
ansible 变量  -a 'echo Hello World.'
```

### 详细说明