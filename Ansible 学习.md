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



## playbooks

执行playbooks

```bash
ansible-playbook playbook.yml -f 10
```

并行的级别 是10。

Playbooks 的格式是YAML.

playbook 由一个或多个 ‘plays’ 组成.它的内容是一个以 ‘plays’ 为元素的列表.

在 play 之中,一组机器被映射为定义好的角色.在 ansible 中,play 的内容,被称为 tasks,即任务.在基本层次的应用中,一个任务是一个对 ansible 模块的调用,这在前面章节学习过.

1. hosts **行的内容是一个或多个组或主机的 patterns,以逗号为分隔符,**remote_user 就是账户名:

```yaml
---
- hosts: webservers
  remote_user: root
```

2. 在每一个 task 中,可以定义自己的远程用户:

```yaml
---
- hosts: webservers
  remote_user: root
  tasks:
    - name: test connection
      ping:
      remote_user: yourname
```

3. 支持从 sudo 执行命令:

   ```yaml
   ---
   - hosts: webservers
     remote_user: yourname
     sudo: yes
   
   ```

4. 可以仅在一个 task 中,使用 sudo 执行命令,而不是在整个 play 中使用 sudo:

```yaml
---
- hosts: webservers
  remote_user: yourname
  tasks:
    - service: name=nginx state=started
      sudo: yes
```

5. 也可以登陆后,sudo 到不同的用户身份,而不是使用 root:

```yaml
---
- hosts: webservers
  remote_user: yourname
  sudo: yes
  sudo_user: postgres
```

6. 在使用 sudo 时指定密码,可在运行 ansible-playbook 命令时加上选项 `--ask-sudo-pass` 
7. 如果使用 sudo 时,playbook 疑似被挂起,可能是在 sudo prompt 处被卡住,这时可执行 Control-C 杀死卡住的任务,再重新运行一次.
8. 每一个 play 包含了一个 task 列表（任务列表）
9. 一个 task 在其所对应的所有主机上（通过 host pattern 匹配的所有主机）执行完毕之后,下一个 task 才会执行
10. 在运行 playbook 时（从上到下执行）,如果一个 host 执行 task 失败,这个 host 将会从整个 playbook 的 rotation 中移除. 如果发生执行失败的情况,请修正 playbook 中的错误,然后重新执行即可.
11. 每个 task 的目标在于执行一个 moudle, 通常是带有特定的参数来执行.在参数中可以使用变量
12. modules 具有”幂等”性,意思是如果你再一次地执行 moudle（译者注:比如遇到远端系统被意外改动,需要恢复原状）,moudle 只会执行必要的改动,只会改变需要改变的地方.所以重复多次执行 playbook 也很安全.
13. 对于 command module 和 shell module,重复执行 playbook,实际上是重复运行同样的命令.如果执行的命令类似于 ‘chmod’ 或者 ‘setsebool’ 这种命令,这没有任何问题.也可以使用一个叫做 ‘creates’ 的 flag 使得这两个 module 变得具有”幂等”特性 （不是必要的）.
14. 每一个 task 必须有一个名称 name
15. 一种基本的 task 的定义,service moudle 使用 key=value 格式的参数,这也是大多数 module 使用的参数格式:

```yaml
tasks:
  - name: make sure apache is running
    service: name=httpd state=running
```

比较特别的两个 modudle 是 command 和 shell ,它们不使用 key=value 格式的参数,而是这样:

```yaml
tasks:
  - name: disable selinux
    command: /sbin/setenforce 0
```

使用 command module 和 shell module 时,我们需要关心返回码信息,如果有一条命令,它的成功执行的返回码不是0, 你或许希望这样做:

```yaml
tasks:
  - name: run this command and ignore the result
    shell: /usr/bin/somecommand || /bin/true
```

或者

```yaml
tasks:
  - name: run this command and ignore the result
    shell: /usr/bin/somecommand
    ignore_errors: True
```

16. 如果 action 行看起来太长,你可以使用 space（空格） 或者 indent（缩进） 隔开连续的一行:

```yaml
tasks:
  - name: Copy ansible inventory file to client
    copy: src=/etc/ansible/hosts dest=/etc/ansible/hosts
            owner=root group=root mode=0644
```

17. 在 action 行中可以使用变量.

```yml
tasks:
  - name: create a virtual host file for {{ vhost }}
    template: src=somefile.j2 dest=/etc/httpd/conf.d/{{ vhost }}
```

18. Handlers: 在发生改变时执行的操作。比如多个 resources 指出因为一个配置文件被改动,所以 apache 需要重新启动,但是重新启动的操作只会被执行一次.

这里有一个例子,当一个文件的内容被改动时,重启两个 services:

```yaml
- name: template configuration file
  template: src=template.j2 dest=/etc/foo.conf
  notify:
     - restart memcached
     - restart apache
  handlers:
    - name: restart memcached
      service:  name=memcached state=restarted
    - name: restart apache
      service: name=apache state=restarted
```

‘notify’ 下列出的即是 handlers.

Handlers 也是一些 task 的列表,通过名字来引用,它们和一般的 task 并没有什么区别.Handlers 是由通知者进行 notify, 如果没有被 notify,handlers 不会执行.不管有多少个通知者进行了 notify,等到 play 中的所有 task 执行完成之后,handlers 也只会被执行一次.

Handlers 最佳的应用场景是用来重启服务,或者触发系统重启操作.除此以外很少用到了.



## 实践案例





