import json
import os

import pika
import time

import ssl
import smtplib


def send_mail(mail, text):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "kokatestmailk8@gmail.com"
    sender_password = "ASDasd123."
    receiver_email = mail
    message = text
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        return {"Message": "Mail has been sent."}
    except Exception as e:
        print(e)
        return {"Message": "Error occurred while sending mail."}
    finally:
        server.quit()


sleepTime = 5
print(' [*] Sleeping for ', sleepTime, ' seconds.')
time.sleep(sleepTime)

print(' [*] Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('RABBIT_MQ_HOST', 'localhost')))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print(' [*] Waiting for messages.')


def callback(ch, method, properties, body):
    print(" [x] Received %s" % body)
    cmd = body.decode()
    cmd = json.loads(cmd)
    send_mail(cmd['mail'], cmd['text'])
    print(" [x] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
