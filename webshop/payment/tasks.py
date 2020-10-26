from io import BytesIO
from webshop.celery import app
import weasyprint

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@app.task
def payment_completed(order_id):

    """
    Task to send an e-mail notification when an order is successfully created.
    """

    order = Order.objects.get(id=order_id)

    # Create invoice e-mail
    subject = f"VitaKing · Budaörs - Rendelés {order_id}"
    message = (
        f"Tisztelt {order.first_name},\n\n"
        f"Csatolva küldjük a legutóbbi vásárlás számláját."
    )
    email = EmailMessage(subject, message, "shaba.keller@gmail.com", [order.email])

    # Generate PDF
    html = render_to_string("orders/order/pdf.html", {"order": order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + "css/pdf.css")]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # Attach PDF file
    email.attach(f"order_{order.id}.pdf", out.getvalue(), "application/pdf")

    # Send e-mail
    email.send()
