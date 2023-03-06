# DIG-server

## Test Server Deploy Setting 
> Amazon Linux 2 기준입니다.

- install git
```shell
sudo yum install git -y
```
- clone git repository

```shell
git clone https://github.com/project-DIG/Daliy-In-GSM-Backend-FastAPI.git
```

- install requirement.txt using pip
```shell
cd Daliy-In-GSM-Backend-FastAPI/
pip3 install -r requirements.txt
```

> run server

```shell
python3 -m gunicorn -k uvicorn.workers.UvicornWorker --access-logfile ./http-log.log main:app --bind 0.0.0.0:8000 --workers 2
```

- open security group port 8000
  - AWS 혹은 다른 클라우드 공급자 의 서버 보안그룹을 8000 포트로 뚫어줍니다.
