# DIG-server

## Test Server Deploy Setting 
> Amazon Linux 2 기준입니다.
### python & python environment install
- clone git repository
```shell
cd /srv
git clone -b develop https://github.com/project-DIG/Daliy-In-GSM-Backend-FastAPI.git

- install mysql-devel ,pip3, etc for mysql-client
```shell
sudo apt-get install python3-pip python-dev python3-dev libmysqlclient-dev gcc 
```
- install requirement.txt using pip
```shell
pip3 install -r base.txt
```

> test server status

```shell
python3 manage.py runserver 0.0.0.0:8000
```
0.0.0.0:8000 을 붙혀주는 이유는 붙혀주지 않는다면 local 에서 밖에 작동하지 않음

- open security group port 8000
  - AWS 혹은 다른 클라우드 공급자 의 서버 보안그룹을 8000 포트로 뚫어줍니다.

- goto chrome & insert << your aws ec2 instance url >>:8000
![스크린샷 2022-04-30 오전 1 40 15](https://user-images.githubusercontent.com/69895368/165987538-3e5b318d-a0c4-405b-8e6a-13441f4cf20f.jpg)


