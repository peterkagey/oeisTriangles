# oeisTriangles
Follow this Twitter bot [@oeisTriangles](https://twitter.com/oeisTriangles).

[![Sequence A258993](https://user-images.githubusercontent.com/10198714/114285278-e824ac00-9a0a-11eb-95f1-023cb5fb34ac.png)](https://twitter.com/oeisTriangles/status/1379628962754686979?s=20)

### Steps to make your own version of this Bot.
Clone the repo, make a Twitter account, sign up for a developer account at https://developer.twitter.com/, add your API keys/secrets to the `secrets.py`.
In order to prevent your secrets from being posted to Github, run the following command to ignore changes to that file:
```
git update-index --skip-worktree secrets.py
```
Now modify the source however you'd like. When you're ready to make sure things are running smoothly on Docker, run
```
docker build -t oeis-tri .
```
Then run locally on port `9000`:
```
docker run -p 9000:8080 oeis-tri
```
Then run this command literally as written, perhaps changing the empty JSON object at the end if your `handler` function uses it:
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```
If it works, then it's time to push your docker image to Amazon Elastic Container Registry. So go to [Amazon ECR](https://console.aws.amazon.com/ecr/repositories) and create a respository called `oeis-tri`.

Now it's time to push your Docker image to ECR. Get your AWS id (here I'm using `123456789`) and server location (here I'm using `us-east-1`) and log in via your bash terminal:
```
aws ecr get-login-password \
    --region us-east-1 \
| docker login \
    --username AWS \
    --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com
```
Find your of your Docker image ID with `docker images` (here mine is `7f7a1f7c47e7`), and (making sure to use your id and server location) run:
```
docker tag 7f7a1f7c47e7 123456789.dkr.ecr.us-east-1.amazonaws.com/oeis-tri
```
Now push your docker image up to ECR:
```
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/oeis-tri
```

Next go to [AWS Lambda](https://console.aws.amazon.com/lambda/home?region=us-east-1), create a function, select "container image", browse ECR for the image you just pushed up, test it out via AWS Lambda, add a "EventBridge (CloudWatch Events)" trigger via the configurations menu, and set it up to fire as often as you'd like. 
