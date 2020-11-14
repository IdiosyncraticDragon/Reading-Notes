# Linux用户权限管理

[TOC]

## 要点

- linux通过ID来辨别用户身份，而不是账户名
- 每个使用者有UID（user ID）和GID（group ID）
  - UID: /etc/passwd
  - GID: /etc/passwd和/etc/group
- UID的范围划分

| id 範圍                 | 該 ID 使用者特性                                             |
| ----------------------- | ------------------------------------------------------------ |
| 0 (系統管理員)          | 當 UID 是 0 時，代表這個帳號是『系統管理員』！               |
| 1~999 (系統帳號)        | 保留給系統使用的 ID，其實除了 0 之外，其他的 UID 權限與特性並沒有不一樣。預設 1000 以下的數字讓給系統作為保留帳號只是一個習慣。根據系統帳號的由來，通常這類帳號又約略被區分為兩種：1~200：由 distributions 自行建立的系統帳號；201~999：若使用者有系統帳號需求時，可以使用的帳號 UID。 |
| 1000~60000 (可登入帳號) | 給一般使用者用的。事實上，目前的 linux 核心 (3.10.x 版)已經可以支援到 4294967295 (2^32-1) 這麼大的 UID 號碼 |

- Linux的账号信息记录在/etc/passwd中
- /etc/passwd中的定义规范

```txt
帳號名稱:密碼:UID:GID:使用者資訊說明欄:/home目录所在处:預設登入時所取得的 shell名稱

例如：
liguiying:x:1000:1000:,,,:/home/liguiying:/usr/bin/zsh
```

注：密碼已經挪到 /etc/shadow 中，因此在此都是 x。早期使用者加密過的密碼記錄在 /etc/passwd 第二個欄位，但這個檔案的權限是任何人均可讀取， 因此，有心人士可以查閱到加密過的密碼，再以暴力破解法就可能可以獲取所有人的密碼。因此，密碼欄位已經移動到另一個檔案去， 這就是 /etc/shadow 的由來。

- 使用者的初始组群記載在 /etc/passwd 檔案的第四個欄位（GID），不過該 GID 對應到人類認識的群組名稱就得到 /etc/group 當中查詢。 
- /etc/group中的定义规范

```txt
群組名稱:群組密碼(目前很少使用):GID:加入此群組的帳號，使用逗號 (,) 分隔每個帳號
```

- 检查账户信息

```bash
id 用户名


(base) ➜  ~ id liguiying
uid=1000(liguiying) gid=1000(liguiying) groups=1000(liguiying),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev)
```

或

```bash
grep liguiying /etc/passwd /etc/group /etc/shadow
```

- Linux 權限的目的是在『保護某些人的檔案資料』,權限都是『設定在檔案/目錄』上， 不是設定在帳號上面的
- Linux 的檔案權限在設定上，主要依據三種身份來決定，包括

```txt
owner / 檔案擁有者：就是檔案所屬人
group / 群組：這個檔案附屬於那一個群組團隊
others / 其他人：不是 user 也沒加入 group 的帳號，就是其他人。
```

- Linux文档权限分三种，包括

```txt
r: read，可讀的意思
w: write，可寫入/編輯/修改的意思
x: eXecutable，可以執行的意思
```

- Linux使用者能使用系統上面的資源與權限有關，因此簡易的帳號管理之後，就需要與權限搭配設計。
  - 一般用戶只能夠修改屬於自己的檔案的 rwx 權限
  - 群組可能需要共享某些檔案資料
- ACL 是 Access Control List 的縮寫，主要的目的是在提供傳統的 owner,group,others 的 read,write,execute 權限之外的細部權限設定。

```bash
# 查看ACL是否启动
dmesg | grep -i acl
```

- 指令

```bash
setfacl -m 為設定的指令與選項 文档
針對個人： u:帳號名稱:rwx-
針對群組： g:群組名稱:rwx-
```

```bash
getfacl 文档
```

