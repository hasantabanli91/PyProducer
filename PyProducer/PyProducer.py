import pika

print('Write -1 to Exit')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.17.0.2'))

channel = connection.channel()
channel.queue_declare(queue='demo-queue')

messagestr = ''
while messagestr != '-1':
    messagestr = input()
    channel.basic_publish(exchange='', routing_key='demo-queue', body=messagestr)

connection.close()