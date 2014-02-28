from django import template

register = template.Library()

@register.filter
def get_wind_data_dates(value, i):
	return value