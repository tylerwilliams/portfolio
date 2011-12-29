# encoding: utf-8
import os
import web
import random
from web.contrib.template import render_mako
from mako import exceptions as mako_exceptions
from enabled import active_pages


cwd = os.path.dirname(os.path.abspath( __file__ ))
urls = (
        '/(.*)', 'main'
        )

app = web.application(urls, globals(), autoreload=True)

render = render_mako(
        directories=[os.path.join(cwd, 'templates')],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


random_images = [
    {
        'link':'/electricalily',
        'src':'http://fr.ac.tl/blog/wp-content/uploads/2011/04/text_small.jpg',
    },
    {
        'link':'/electricalily',
        'src':'http://fr.ac.tl/blog/wp-content/uploads/2011/04/board_small.jpg',
    },
    {
        'link':'/stringer',
        'src':'http://fr.ac.tl/blog/wp-content/uploads/2011/02/strings.jpg'
    },
    {
        'link':'/turbine',
        'src':'/static/images/turbine.png'
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

if __name__ == "__main__":
    app.run()