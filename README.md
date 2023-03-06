# DIG-server

## Test Server Deploy Setting 
> Amazon Linux 2 기준입니다.

- shells
```shell
#git, docker, docker-compose 설치
sudo yum install git -y

sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chmod 666 /var/run/docker.sock

sudo curl -L https://github.com/docker/compose/releases/download/1.25.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

#git clone
git clone https://github.com/project-DIG/Daliy-In-GSM-Backend-FastAPI.git

//requirements 설치
cd Daliy-In-GSM-Backend-FastAPI/
pip3 install -r requirements.txt

#실행
docker-compose up
```

- 포트 8000번을 열어줍니다

- DB 관련 작업은 불가능할 수 있습니다
