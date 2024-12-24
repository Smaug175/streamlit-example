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

streamlit run app.py --server.port=80 --server.address=0.0.0.0
```
