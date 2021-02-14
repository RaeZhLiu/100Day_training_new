from tornado import web,ioloop,httpserver


# 视图
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('此部分填写HTML要做的事')


# 路由系统
app = web.Application(
    [
        (r'/', MainPageHandler),   # 显示页面内容
    ],
)


if __name__ == "__main__":
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8002)
    ioloop.IOLoop.current().start()

