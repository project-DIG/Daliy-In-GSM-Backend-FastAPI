# DIG-server

## Test Server Deploy Setting 
> Amazon Linux 2 기준입니다.

- shells
```shell
//git, docker, docker-compose 설치
sudo yum install git -y
curl -fsSL https://get.docker.com/ | sudo sh
sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

//git clone
git clone https://github.com/project-DIG/Daliy-In-GSM-Backend-FastAPI.git

//requirements 설치
cd Daliy-In-GSM-Backend-FastAPI/
pip3 install -r requirements.txt

//실행
docker-compose up
```

- open security group port 8000
  - AWS 혹은 다른 클라우드 공급자 의 서버 보안그룹을 8000 포트로 뚫어줍니다.
