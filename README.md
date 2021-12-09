## Pulsar Pychat

## With context

````
bin/pulsar-admin functions localrun --broker-service-url pulsar://pulsar-mini-proxy:6650/--py pulsar-pychat-function/src/sentiment.py \
  --classname Chat.process \
  --inputs persistent://public/default/chat --output persistent://public/default/chatresult

````
