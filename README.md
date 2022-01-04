## Pulsar Pychat

## With context

````

bin/pulsar-admin functions stop --name Chat --namespace default --tenant public

bin/pulsar-admin functions delete --name Chat --namespace default --tenant public

bin/pulsar-admin functions create --auto-ack true --py pulsar-pychat-function/src/sentiment.py --classname "sentiment.Chat" --inputs "persistent://public/default/chat2" --log-topic "persistent://public/default/chatlog2" --name Chat --namespace default --output "persistent://public/default/chatresult2" --tenant public

````

# To Install Python 3 Library

````

pip3 install --upgrade pip
pip3 install vaderSentiment
python3 pulsar-pychat-function/src/sentiment.py 

````
