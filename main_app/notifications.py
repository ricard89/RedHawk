from accounts.models import User
from main_app.models import Notification, Tag

from push_notifications.apns import apns_send_message

def push_notification(user):

    notifications = Notification.objects.all()

    for notification in notifications:
        first_operand = str(Tag.objects.filter(name_ID=notification.first_operand)[0].value)
        operator = notification.operator
        second_operand = notification.second_operand
        user = notification.owner

        if second_operand == "true" or second_operand == "TRUE":
            second_operand = "1"
        elif second_operand == "false" or second_operand == "FALSE":
            second_operand = "0"

        if eval(first_operand + operator + second_operand):
            if not notification.sended:
                registration_id = user.apns_device_token
                message={"title" : notification.title, "body" : notification.message}
                apns_send_message(registration_id, message)

                Notification.objects.filter(id=notification.id, owner=user).update(sended=True)
        else:
            Notification.objects.filter(id=notification.id, owner=user).update(sended=False)
