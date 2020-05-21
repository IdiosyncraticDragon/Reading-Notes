# Ansible 学习

> 参考： http://ansible.com.cn/docs/intro.html 
>
> 参考： https://www.w3cschool.cn/automate_with_ansible/ 

ansible的项目地址在：https://github.com/ansible/ansible， 它只需要在一个管理机器（可以是一个个人笔记本）上安装即可，不需要在各个管理机器上安装/运行任何软件，因此非常方便。

## 安装

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



