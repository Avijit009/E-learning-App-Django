from django import template
from instructor.models import QuizAnswer,Quiz


register = template.Library()

@register.filter
def range_filter(value):
    if len(value)<300:
        return value
    return value[0:300]+'   - - - - - - - - - - - -- - - - -'

@register.filter
def mark_count(user):
    return QuizAnswer.objects.filter(user=user).count()