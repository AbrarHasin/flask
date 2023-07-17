# import pika, json
# import os
# from app import Product, db

# params = pika.URLParameters('amqps://zllzhyav:jHi18yD9N5Rr8VsvY-bVxKiz5nKsBvNX@armadillo.rmq.cloudamqp.com/zllzhyav')
# # params = pika.URLParameters(os.getenv("RABBITMQ_URI"))


# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# channel.queue_declare(queue='main')


# def callback(ch, method, properties, body):
#     print('Received in main')
#     data = json.loads(body)
#     print(data)

#     if properties.content_type == 'product_created':
#         product = Product(id=data['id'], title=data['title'], image=data['image'])
#         db.session.add(product)
#         db.session.commit()
#         print('Product Created')

#     elif properties.content_type == 'product_updated':
#         product = Product.query.get(data['id'])
#         product.title = data['title']
#         product.image = data['image']
#         db.session.commit()
#         print('Product Updated')

#     elif properties.content_type == 'product_deleted':
#         product = Product.query.get(data)
#         db.session.delete(product)
#         db.session.commit()
#         print('Product Deleted')


# channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

# print('Started Consuming')

# channel.start_consuming()

# channel.close()

import pika, json

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
# django.setup()

# from products.models import Product

params = pika.URLParameters('amqps://zllzhyav:jHi18yD9N5Rr8VsvY-bVxKiz5nKsBvNX@armadillo.rmq.cloudamqp.com/zllzhyav')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)
    # id = json.loads(body)
    # print(id)
    # product = Product.objects.get(id=id)
    # product.likes = product.likes + 1
    # product.save()
    # print('Product likes increased!')

channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()