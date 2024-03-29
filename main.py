# encoding: utf-8
import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.dirname(os.path.abspath( __file__ )))
import web
import random
from web.contrib.template import render_mako
from mako import exceptions as mako_exceptions
from enabled import active_pages


cwd = os.path.dirname(os.path.abspath( __file__ ))
urls = (
        '/(.*)', 'main'
        )

render = render_mako(
        directories=[os.path.join(cwd, 'templates')],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


random_images = [
    {
        'link':'/electricalily',
        'src':'/static/images/text_small.jpg',
    },
    {
        'link':'/electricalily',
        'src':'/static/images/board_small.jpg',
    },
    {
        'link':'/electricalily',
        'src':'/static/images/pwmcloseup_small.jpg',
    },
    {
        'link':'/stringer',
        'src':'/static/images/stringer_small.jpg'
    },
    {
        'link':'/turbine',
        'src':'/static/images/turbine_small.jpg'
    },
    {
        'link':'/visualizer',
        'src':'/static/images/visualized_small.jpg'
    },
    {
        'link':'/medea',
        'src':'/static/images/circuit_export.png'
    },
    {
        'link':'/medea',
        'src':'/static/images/circuit_brd.png'
    },
    {
        'link':'/echospot',
        'src':'/static/images/echospot_small.jpg'
    },
    {
        'link':'/misc',
        'src':'/static/images/fpbox.jpg'
    },
    {
        'link':'/misc',
        'src':'/static/images/wirewrap.jpg'
    },
    {
        'link':'/misc',
        'src':'/static/images/remix_small.jpg'
    },
    {
        'link':'/misc',
        'src':'/static/images/mega128_small.jpg'
    },
    {
        'link':'/0-scope',
        'src':'/static/images/scope.png'
    },
    {
        'link':'/0-scope',
        'src':'/static/images/finished_out.png'
    },    
]

def random_image():
    d = random.choice(random_images)
    blob = """<p style="text-align: center;">
                <a href="%(link)s">
                  <img src="%(src)s"/>
                </a>
              </p>
           """
    return blob % d


class main:
    def GET(self, page_name):
        # find the requested page, or redirect to /
        try:
            render_func = getattr(render, page_name, None)
        except mako_exceptions.TopLevelLookupException:
            render_func = render.index
        
        # if index page, find a random image
        if render_func == render.index:
            body_override = random_image()
        else:
            body_override = None
        
        # render
        return render_func(sidebar=active_pages, body_override=body_override)

application = web.application(urls, globals()).wsgifunc()