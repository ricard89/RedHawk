from main_app.models import Notification, Tag

def send_push_notification(user):

    notifications = Notification.objects.filter(owner=user)
    tags = Tag.objects.filter(owner=user)

    for notification in notifications:
        first_operand = str(Tag.objects.filter(owner=user, name_ID=notification.first_operand)[0].value)
        operator = notification.operator
        second_operand = notification.second_operand

        if second_operand == "true" or second_operand == "TRUE":
            second_operand = "1"
        elif second_operand == "false" or second_operand == "FALSE":
            second_operand = "0"

        if eval(first_operand + operator + second_operand):
            if not notification.sended:
                print("TO: " + str(user) + " TITLE: " + notification.title + " MESSAGE: " + notification.message)
                Notification.objects.filter(id=notification.id, owner=user).update(sended=True)
        else:
            Notification.objects.filter(id=notification.id, owner=user).update(sended=False)
