# structure and interpretation of computer language



## 安装scheme

在WSL 1下安装

下载地址：http://www.gnu.org/software/mit-scheme/

```
sudo apt-get install -y gcc make libncurses-dev libx11-dev debhelper m4 autotools-dev libssl-dev libmhash-dev libmcrypt-dev libgdbm-dev libpq-dev libncurses5-dev libx11-dev libxt-dev libdb-dev libltdl-dev
tar -xvzf mit-scheme-10.1.11-x86-64.tar.gz
cd mit-scheme-10.1.11/src
./configure --prefix=/home/liguiying/installed/scheme
make
sudo make install

```



```scheme
(define <name> value)
(define (<name> <formal parameters>) <body>)
(cond (<p1> <e1>)
      (<p2> <e2>)
      .
      .
      .
      (<pn>, <en>)
      )
(if <predicate> <consequent> <alternative>)
(and <e1> ... <en>)
(or <e1> ... <en>)
(not <e>)
```

编译运行文件

假设test.scm

```scheme
(cf "test.scm")
(load "test")
```

