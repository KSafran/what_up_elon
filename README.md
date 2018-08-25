# Elon, WYD?
Elon has been acting strange lately. We should keep an eye on him.

I'll be playing around with deploying web apps on AWS using docker.

# Instructions
Start an EC2 instance
-Make sure the security group has port 80 open to the public (0.0.0.0)
Clone the repo
```
sudo yum install git
git clone https://github.com/KSafran/what_up_elon.git
```

SSH into the instance, clone the repo, and run the following
```
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```
Restart the ssh session to apply that ec2-user permission command above
Then build the docker image and run a container
```
docker build -t flask_app .
docker run -d -p 80:80 flask_app
```
