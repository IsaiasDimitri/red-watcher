import graphene
from graphene_django import DjangoObjectType

from .models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class Query(graphene.ObjectType):
    event = graphene.List(EventType)

    def resolve_event(self, info, **kwargs):
        return Event.objects.all()


class CreateEvent(graphene.Mutation):
    event = graphene.Field(EventType)

    class Arguments:
        locality_address = graphene.String()
        event_type = graphene.String()
        event_time = graphene.String()

    def mutate(self, info, locality_address, event_type, event_time):
        event = Event(
            locality_address=locality_address,
            event_type=event_type,
            event_time=event_time,
        )
        event.save()

        return CreateEvent(
            event=event
        )


class UpdateEvent(graphene.Mutation):
    event = graphene.Field(EventType)

    class Arguments:
        id = graphene.ID()
        eventStatus = graphene.String()
        teamConfirmation = graphene.Boolean()
        teamTime = graphene.String()
        team = graphene.String()

    # The class attributes define the response of the mutation

    def mutate(self, info, id, eventStatus, teamConfirmation, teamTime, team):
        event = Event.objects.get(pk=id)
        event.event_status = eventStatus
        event.team_confirmation = teamConfirmation
        event.team_time = teamTime
        event.team = team
        event.save()
        return UpdateEvent(event=event)


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
