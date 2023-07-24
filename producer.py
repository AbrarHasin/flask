import pika, json

params = pika.URLParameters('amqps://zllzhyav:jHi18yD9N5Rr8VsvY-bVxKiz5nKsBvNX@armadillo.rmq.cloudamqp.com/zllzhyav')

params.socket_timeout = 10 # Set the socket timeout higher (0.25 is default) needed more for Docker/Distributed system

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(content_type='application/json',
            content_encoding='utf-8',
            headers={'key': 'value'},
            delivery_mode = 1,
            )
    message = {'method': method, 'body': body}
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(message), properties=properties)