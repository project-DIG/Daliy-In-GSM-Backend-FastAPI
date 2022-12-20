# DIG-server

## Test Server Deploy Setting 
> Amazon Linux 2 기준입니다.

- clone git repository
```shell
git clone -b develop https://github.com/project-DIG/Daliy-In-GSM-Backend-FastAPI.git
```

- install requirement.txt using pip
```shell
pip3 install -r requirements.txt
```

> run server

```shell
python3 main.py
```

- open security group port 8000
  - AWS 혹은 다른 클라우드 공급자 의 서버 보안그룹을 8000 포트로 뚫어줍니다.
