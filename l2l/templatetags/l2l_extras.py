from django import template
from datetime import datetime

register = template.Library()

@register.filter
def l2l_dt(date):
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
    if isinstance(date, datetime):
        return date.strftime("%Y-%m-%d %H:%M:%S")
    raise Exception('Invalid type: Only accepts String or Datetime') 

