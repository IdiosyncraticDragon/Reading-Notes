[TOC]

# 环境安装

### windows



首先要安装nodejs，我在windows安装的。nodejs安装好后就有npm，我是在windows下安装的，nodejs直接装应用程序就行了。

安装electron

```bash
npm i -D electron@latest
```

demo环境

```bash
git clone https://github.com/electron/electron-api-demos
cd electron-api-demos
npm install
npm start
```



### WSL

```bash
sudo apt-get install -y nodejs
git clone https://github.com/electron/electron-api-demos
cd electron-api-demos
npm install
npm start
```

# Javascript散点复习



# Nodejs学习

hello world程序

```javascript
const http = require('http')

const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((req, res) => {
          res.statusCode = 200
          res.setHeader('Content-Type', 'text/plain')
          res.end('你好世界\n')
})

server.listen(port, hostname, () => {
          console.log(`服务器运行在 http://${hostname}:${port}/`)
})
```

运行：

```bash
node hello.js
```



引入本地模块。在 Node.js 模块系统中，每个文件都被视为独立的模块。

```js
const circle = require('./circle.js');
```





# Electron学习

electron的图标长得和atom很像，强烈怀疑有相关性。





## 资料

[1] 官网：http://www.electronjs.org/