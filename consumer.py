import pika, json

params = pika.URLParameters('amqps://zllzhyav:jHi18yD9N5Rr8VsvY-bVxKiz5nKsBvNX@armadillo.rmq.cloudamqp.com/zllzhyav')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    message = json.loads(body)
    method = message['method']
    body = message['body']
    print(f"Method: {method}")
    print(f"Body: {body}")


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

channel.close()