from webshop.celery import app
from django.core.mail import send_mail
from orders.models import Order


@app.task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"VitaKing · Budaörs - Rendelésszám {order.id}"
    message = (
        f"Tisztelt {order.first_name},\n\n"
        f"Sikeresen leadott egy megrendelést."
        f"A megrendelés azonosítója {order.id}."
    )
    mail_sent = send_mail(subject, message, "shaba.keller@gmail.com", ["shaba.keller@gmail.com"])
    return mail_sent
