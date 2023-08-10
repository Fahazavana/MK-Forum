from django.template import Library

register = Library()


@register.simple_tag
def comm_reaction_count_up(comment):
    return comment.reactioncomment_set.filter(up=1).count()


@register.simple_tag
def comm_reaction_count_down(comment):
    return comment.reactioncomment_set.filter(down=1).count()
