#coding: utf-8
from unittest import TestCase
from django.template import Template, Context
from chart_tools.templatetags.chart_tags import prepare_chart

CHART = "<img src='http://chart.apis.google.com/chart?chxr=0,0,160&chxt=y&chbh=a&chs=440x220&cht=bvs&chco=4D89F9&chds=0,160&chd=t:10,50,60,80,40,60,30&chtt=Horizontal+bar+chart' width='440' height='220' alt=''  />"

FIXTURES = {
'copy_paste': '''
http://chart.apis.google.com/chart
   ?chxr=0,0,160
   &chxt=y
   &chbh=a
   &chs=440x220
   &cht=bvs
   &chco=4D89F9
   &chds=0,160
   &chd=t:10,50,60,80,40,60,30
   &chtt=Horizontal+bar+chart
''',

'copy_paste_without_url': '''
   ?chxr=0,0,160
   &chxt=y
   &chbh=a
   &chs=440x220
   &cht=bvs
   &chco=4D89F9
   &chds=0,160
   &chd=t:10,50,60,80,40,60,30
   &chtt=Horizontal+bar+chart
''',

'formatted': '''
http://chart.apis.google.com/chart?
   chxr=0,0,160&
   chxt=y&
   chbh=a&
   chs=440x220&
   cht=bvs&
   chco=4D89F9&
   chds=0,160&
   chd=t:10,50,60,80,40,60,30&
   chtt=Horizontal+bar+chart
''',

'cleaned_up': '''
   chxr=0,0,160
   chxt=y
   chbh=a
   chs=440x220
   cht=bvs
   chco=4D89F9
   chds=0,160
   chd=t:10,50,60,80,40,60,30
   chtt=Horizontal+bar+chart
'''

}

class PrepareTest(TestCase):

    def assertCorrectChart(self, variant):
        self.assertEqual(prepare_chart(FIXTURES[variant]), CHART)

    def test_copy_paste(self):
        self.assertCorrectChart('copy_paste')

    def test_copy_paste2(self):
        self.assertCorrectChart('copy_paste_without_url')

    def test_formatted(self):
        self.assertCorrectChart('formatted')

    def test_cleaned_chart(self):
        self.assertCorrectChart('cleaned_up')


class RenderTest(TestCase):

    def assertChartRendered(self, variant):
        template = '{% load chart_tags %}{% chart %}'+FIXTURES[variant]+'{% endchart %}'
        rendered = Template(template).render(Context())
        assert rendered == CHART, "\n%s \n  VV \n%s \n != \n%s" % (template, rendered, CHART)

    def test_copy_paste(self):
        self.assertChartRendered('copy_paste')

    def test_copy_paste2(self):
        self.assertChartRendered('copy_paste_without_url')

    def test_formatted(self):
        self.assertChartRendered('formatted')

    def test_cleaned_chart(self):
        self.assertChartRendered('cleaned_up')

class RegressionTest(TestCase):

    def test_tab_as_whitespace(self):
        chart_input = FIXTURES['cleaned_up'].replace(" ", "\t")
        self.assertFalse(chart_input.find("\t") == -1)
        chart_img = prepare_chart(chart_input)
        self.assertTrue(chart_img.find("\t") == -1)

