# 1. 개요
* nginx timeout 예제
* nginx는 연결된 세션이 60초(default) 동안 아무런 통신을 하지 않는다면 연결은 종료

# 2. 준비
* nginx
* docker

# 3. webapp 실행방법
* docker를 이용하여 python webapp을 실행합니다.

```sh
docker run --rm -d --name=timeoutapp -p 9000:80 choisunguk/nginx-timeout:v1 
```

* api는 2개가 있습니다. timeout은 70후에 응답을 리턴합니다.
  * curl localhost:9000/normal
  * curl localhost:9000/timeout

* 도커 컨테이너를 삭제하려면 아래 명령어를 입력하세요.
```sh
docker kill timeoutapp
```

# 4. nginx 실행
* nginx 설정파일을 복사하고 설정을 재로드합니다.
```sh
cp ./nginx.conf /etc/nginx/conf.d/timeout_demo.conf
systemctl reload nginx
```

* /etc/hosts파일에 도메인을 설정합니다.
```sh
echo "127.0.0.1 timeout-demo.com" >> /etc/hosts
```
