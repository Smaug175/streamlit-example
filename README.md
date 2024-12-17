# 构建镜像
docker build -t streamlit:latest .

# 启动容器
docker run -p 80:80 streamlit:latest
