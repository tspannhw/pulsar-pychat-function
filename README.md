## Pulsar Pychat

## With context

````
bin/pulsar-admin functions localrun --broker-service-url pulsar://pulsar-mini-proxy:6650/ --py /pulsar/pulsar-pychat-function/src/sentiment.py \
  --classname sentiment.Chat --inputs persistent://public/default/chat --output persistent://public/default/chatresult --tenant public --namespace default --name Chat
  
bin/pulsar-admin functions localrun --broker-service-url pulsar://pulsar-mini-proxy:6650/ --py /pulsar/pulsar-pychat-function/src/sentiment.py \
  --classname sentiment.Chat --inputs persistent://public/default/chat2 --output persistent://public/default/chatresult2 --tenant public --namespace default --name Chat
  
  
/pulsar/bin/pulsar-admin functions localrun \
--broker-service-url pulsar://broker_container:6650 \
--tenant user1 \
--namespace namespace1 \
--py /pulsar_functions/function1.py \
--name function_test \
--user-config '{"output_topic": "persistent://user1/namespace1/output_topic"}' \
--classname function1.Function1 \


bin/pulsar-admin functions create \
  --py reverse.py \
  --classname reverse \
  --inputs persistent://public/default/backwards \
  --output persistent://public/default/forwards \
  --tenant public \
  --namespace default \
  --name reverse
````

## correct syntax for localrun

## connect to k8 node and run from there localrun

````
kubectl exec -it -n pulsar pulsar-mini-toolset-0 -- /bin/bash

pip3 install --upgrade pip
pip3 install vaderSentiment
python3 pulsar-pychat-function/src/sentiment.py 

bin/pulsar-admin functions localrun --broker-service-url pulsar://pulsar-mini-proxy:6650/ --py /pulsar/pulsar-pychat-function/src/sentiment.py   --classname sentiment.Chat --inputs persistent://public/default/chat --output persistent://public/default/chatresult --tenant public --namespace default --name Chat
````

## create function and deploy

````
bin/pulsar-admin functions create --py /pulsar/pulsar-pychat-function/src/sentiment.py  --classname sentiment.Chat --tenant public --namespace default --name Chat --inputs persistent://public/default/chat --output persistent://public/default/chatresult 

````

## check function
````
bin/pulsar-admin functions get --tenant public --namespace default --name Chat
bin/pulsar-admin functions status --tenant public --namespace default --name Chat
bin/pulsar-admin functions stats --tenant public --namespace default --name Chat
````

## config file

````

bin/pulsar-admin functions create --py /pulsar/pulsar-pychat-function/src/sentiment.py  --classname sentiment.Chat --tenant public --namespace default --name Chat --inputs persistent://public/default/chat --output persistent://public/default/chatresult 
   
bin/pulsar-admin functions create --functionConfigFile ./chat.yaml
    
chat.yaml

name: Chat
tenant: public
namespace: default
py: /pulsar/pulsar-pychat-function/src/sentiment.py
className: sentiment.Chat
inputs: 
- persistent://public/default/chat
output: persistent://public/default/chatresult
brokerServiceUrl: pulsar://pulsar-mini-proxy:6650


bin/pulsar-admin functions list --tenant public --namespace default

bin/pulsar-admin functions trigger --tenant public --namespace default --name Chat --topic persistent://public/default/chat \
    --trigger-value "hello pulsar functions"

bin/pulsar-admin topics create persistent://public/default/chat
bin/pulsar-admin topics create persistent://public/default/chatresult
bin/pulsar-admin topics create persistent://public/default/chatlog
bin/pulsar-admin topics create persistent://public/default/chatdead
bin/pulsar-admin topics create persistent://public/default/chat2
bin/pulsar-admin topics create persistent://public/default/chatresult2

bin/pulsar-client consume "persistent://public/default/chat" -s "fnchatreader" -n 0
bin/pulsar-client consume "persistent://public/default/chatresult" -s "fnchatresultreader" -n 0
  
  
bin/pulsar-admin sink stop --name scyalla-test-sink --namespace default --tenant public

bin/pulsar-admin sinks delete --tenant public --namespace default --name scyalla-test-sink
````
