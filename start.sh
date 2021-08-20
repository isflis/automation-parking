docker rm -f $(docker ps -a -q)
docker rmi $(docker images -a -q)

docker build -t ui-test .
docker run -it -w /usr/workspace -v $(pwd):/usr/workspace ui-test bash
