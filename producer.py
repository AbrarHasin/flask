import pika, json

params = pika.URLParameters('amqps://sxhupzyl:6qwtiY5A6CJKv3PTVQY651zRzHAb5nib@armadillo.rmq.cloudamqp.com/sxhupzyl')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
