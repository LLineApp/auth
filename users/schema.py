from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

import datetime
import hashlib
from django.conf import settings


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        cpf = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, cpf, password):
        user = get_user_model()(
            cpf=cpf,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.AbstractType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged!')
        return user


def userToken():
    user = get_user_model()
    today = datetime.date.today()
    key = settings.SECRET_KEY  + str(user.email) + str(today)
    return hashlib.md5(key.encode()).digest
