import os
import tornado.ioloop
import tornado.web

class StartHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class PlayHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("play.html")


def make_app():
    settings = dict(
        static_path=os.path.join(os.path.dirname(__file__), 'public'),
        template_path=os.path.join(os.path.dirname(__file__), 'public/html'),
        static_url_prefix='/public/'
    )
    return tornado.web.Application(
        handlers=[
            (r"/", StartHandler),
            (r"/play", PlayHandler),
        ],
        autoreload=True,
        **settings
    )

if __name__ == "__main__":
    app = make_app()
    port = int(os.environ.get("PORT", 8888))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
