## Pulsar Pychat

## With context

````
bin/pulsar-admin functions localrun \
  --py src/sentiment.py \
  --classname Chat.process \
  --inputs persistent://public/default/chat \
  --output persistent://public/default/chatresult

````
