# 构建镜像
docker build -t streamlit:dev3 .

# 启动容器
docker run -p 80:80 streamlit:dev3
