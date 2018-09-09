import paho.mqtt.client as paho

def on_publish(client,userdata,result):             
    print("data published \n")
    pass
client1= paho.Client("control1")                          
client1.on_publish = on_publish                         
client1.connect("test.mosquitto.org","1883")                                
ret= client1.publish("patidar","hey i am nil") 
