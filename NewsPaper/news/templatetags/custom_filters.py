from django import template


register = template.Library()



@register.filter()
def censor(message):

   bad_words = ['дурак','чмо','редиска','мат', 'бля', 'ху', 'пизд', 'пищи' ]  # непристойные выражения
   message_1 = message.lower()

   for i in bad_words:
      if i in message_1:
         message_1 = message_1.replace(i, "*" * len(i))

   message = message_1[0].title() + message_1[1:]

   return message


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()

