from django import template
from account.models import RoleUser

register = template.Library()

@register.filter
def get_user_role_id(role_users, user):

    ru = role_users.filter(user=user).first()
    return ru.role.id if ru else ''

@register.filter
def get_user_role_name(role_users, user):
    ru = role_users.filter(user=user).first()
    return ru.role.role if ru else ''