import graphene
from graphene_django import DjangoObjectType

from .models import Notification

class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification

class Query(graphene.ObjectType):
    notifications = graphene.List(NotificationType)

    def resolve_notifications(self, info):
        return Notification.objects.all()

class CreateNotification(graphene.Mutation):
    id = graphene.Int()
    location = graphene.String()
    phone_number = graphene.String()

    class Arguments:
        location = graphene.String()
        phone_number = graphene.String()

    def mutate(self, info, location, phone_number):
        notification = Notification(location=location, phone_number=phone_number)
        notification.save()

        return CreateNotification(
            id=notification.id,
            location=notification.location,
            phone_number=notification.phone_number,
        )

class DeleteNotification(graphene.Mutation):
    id = graphene.Int()
    location = graphene.String()
    phone_number = graphene.String()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        notification = Notification.objects.get(id=id)
        notification.delete()

        return DeleteNotification(
            id=notification.id,
            location=notification.location,
            phone_number=notification.phone_number,
        )

class Mutation(graphene.ObjectType):
    create_notification = CreateNotification.Field()
    delete_notification = DeleteNotification.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
