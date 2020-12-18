import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Link, Vote, Auth


class AuthFilter(django_filters.FilterSet):
    class Meta:
        model = Auth
        fields = ['cpf', 'password']


class AuthNode(DjangoObjectType):
    class Meta:
        model = Auth
        interfaces = (graphene.relay.Node, )


class RelayCreateAuth(graphene.relay.ClientIDMutation):
    link = graphene.Field(AuthNode)

    class Input:
        cpf = graphene.String()
        password = graphene.String()

    def mutate_and_get_payload(self, root, info, **input):
        auth = Auth(
            cpf=input.get('cpf'),
            password=input.get('password'),
            posted_by=cpf,
        )
        auth.save()

        return RelayCreateAuth(auth=auth)


    # ############################################################


class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ['url', 'description']


class LinkNode(DjangoObjectType):
    class Meta:
        model = Link

        interfaces = (graphene.relay.Node, )


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node,)


class RelayQuery(graphene.ObjectType):
    relay_link = graphene.relay.Node.Field(LinkNode)

    relay_links = DjangoFilterConnectionField(
        LinkNode, filterset_class=LinkFilter)

    relay_auth = graphene.relay.Node.Field(AuthNode)


class RelayCreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String()
        description = graphene.String()

    def mutate_and_get_payload(self, root, info, **input):
        user = info.context.user or None

        link = Link(
            url=input.get('url'),
            description=input.get('description'),
            posted_by=user,
        )
        link.save()

        return RelayCreateLink(link=link)


class RelayMutation(graphene.AbstractType):
    relay_create_link = RelayCreateLink.Field()
    relay_create_auth = RelayCreateAuth.Field()
