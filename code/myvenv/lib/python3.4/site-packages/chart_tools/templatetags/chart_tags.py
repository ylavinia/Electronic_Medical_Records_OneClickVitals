#coding: utf-8
import re
from django import template
from django.template import TemplateSyntaxError
register = template.Library()
API_URL = 'http://chart.apis.google.com/chart'


@register.inclusion_tag('chart_tools/bar_chart.html')
def bar_chart(values, captions, size='580x100', max_value=None):
    max_value = max_value or max(values)
    return {
        'values': [0 if not x else x for x in values], # Pass 0 to Google instead of Python falsiness
        'captions': captions,
        'size': size,
        'max_value': max_value,
    }

@register.tag
def chart(parser, token):
    params = token.split_contents()
    if len(params) == 2:
        attr = params[1]
    elif len(params) == 1:
        attr = ''
    else:
        raise TemplateSyntaxError('Invalid arguments')
    nodelist = parser.parse(('endchart',))
    parser.delete_first_token()
    return ChartNode(nodelist, attr)

class ChartNode(template.Node):
    def __init__(self, nodelist, attr):
        self.nodelist = nodelist
        self.attr = attr

    def render(self, context):
        input = self.nodelist.render(context)
        return prepare_chart(input, self.attr)

def prepare_chart(input, attr=''):
    # remove whitespaces
    input_lines = input.replace(' ', '').replace('\t', '').splitlines()

    # build url
    lines = []

    def clean_lines(line):
        if line.startswith(API_URL):
            return False
        if not line:
            return False
        return True

    for line in filter(clean_lines, input_lines):
        if line.startswith('&'):
            line = line[1:]
        if not line.endswith('&'):
            line = line + '&'
        lines.append(line)

    if not lines[0].startswith('?'):
        lines[0] = '?'+lines[0]
    lines[-1] = lines[-1].rstrip('&')

    output = ''.join(lines)

    # get the width and height from chart data for later use
    width = height = ''
    size = re.search("chs=(\d+)x(\d+)", output)
    if size:
        width = size.group(1)
        height = size.group(2)

    # prepend with API_URL
    if not output.startswith(API_URL):
        output = API_URL + output

    img = "<img src='%s' width='%s' height='%s' alt='' %s />" % (output, width, height, attr)
    return img
