## 依赖安装
pip install -r requirements.txt
## 切换环境
source activate nanoGPT
## 启动服务
uvicorn api-server:app --host '0.0.0.0' --port 9711 --reload
## test api
井盖
curl http://127.0.0.1:9711/detect_objects?image_url=https://i.328888.xyz/2023/04/17/ieHrRQ.jpeg
破损路面
curl http://127.0.0.1:9711/detect_objects?image_url=https://o2.orbitsoft.cn/wu1/uploads/K95LGJU3G0LU7BDVJEOHUO.png