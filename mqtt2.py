import paho.mqtt.client as paho
#pip3 install paho-mqtt
global mqttclient;
global broker;
global port;


broker = "0.0.0.0";
port = 1883;

client_uniq = "pubclient_123"

mqttclient = paho.Client(client_uniq, True) 

def test(client, userdata, message):
  print("client:"+ str(client))
  print("userdata:"+ userdata)
  
  print("message:"+ message.payload)
  payload=float(message.payload)
  conn =pymysql.connect(database="Iotdatap",user="user2",password="Pass1234",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
  cur=conn.cursor()
#Create a dictonary containing the fields, name, age and place
  data={'topic':'IOT/test','value':message.payload}
#Execute the SQL to write data to the database
  cur.execute("INSERT INTO 'Sensordata'('Topic', 'Sensorvalue') VALUES(%(topic)s,%(value)s);",data)
#Close the cursor
  #cur.close()
#Commit the data to the database
  conn.commit()
def _on_message(client, userdata, msg):
#       print("Received: Topic: %s Body: %s", msg.topic, msg.payload)
        print(msg.topic+" "+str(msg.payload))

#Subscribed Topics 
def _on_connect(mqttclient, userdata, flags, rc):
#       print("New Client: "+str(mqttclient)+ " connected")
#       print(rc)
        mqttclient.subscribe("IOT/#", qos=0)    
  
mqttclient.message_callback_add("IOT/test", test)

mqttclient.connect(broker, port, keepalive=1, bind_address="")
  
mqttclient.on_connect = _on_connect

mqttclient.loop_forever()
conn.close()
