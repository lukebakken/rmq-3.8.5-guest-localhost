import pika

parameters = pika.ConnectionParameters(host='shostakovich')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.confirm_delivery()
channel.close()
connection.close()
