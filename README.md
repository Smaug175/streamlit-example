## 本地调试
### 测试登录id与密码
id = 1 

password = 123
### 安装依赖
```bash

apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
``` 

```bash

pip3 install -r requirements.txt
```
### 运行 app
```bash

streamlit run app.py --server.port=80
```

## 部署
### 运行 app
```bash

nohup streamlit run app.py --server.port=80 > log.txt 2>&1 &
```
### 查看输出
```bash

tail -f log.txt
```
### 查找并杀死进程
```bash

ps aux | grep streamlit
```
```bash

kill <pid>
```