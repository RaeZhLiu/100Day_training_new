# 导入tornado库并新引入web,ioloop,httpserver模块
from tornado import web,ioloop,httpserver

# 视图——RequestHandler-输出响应函数
class MainPageHandler(web.RequestHandler):
    # request可以是get()或post()处理函数，如果想让子类支持其他的标准请求如GET/HEAD/POST等，可以在子类中覆盖这些方法
    def get(self, *args, **kwargs):
        # 接收值渲染——接收self.render()方法传值的变量或一个值
        self.render('AutomaticJump.html')

# 路由系统
# 当Web服务器启动时，Web服务器会自动创建一个application对象。application对象一旦创建，它将一直存在，直到Web服务器关闭。
app = web.Application(
    [
        (r'/', MainPageHandler),   # 显示页面内容
    ],
)

if __name__ == '__main__':
    # 前台 socket
    # http server用于解析静态页面的服务器
    http_server = httpserver.HTTPServer(app)
    # 使用Listen在服务器端进行监听端口
    # 避免端口被占用，设置端口号8002等
    http_server.listen(60035)
    # 返回当前线程的IOLoop。如果IOLoop当前正在运行或被标记为通过make_current 返回该实例。如果当前没有IOLoop，则返回IOLoop.instance()(即主线程的IOLoop)，如果没有，则需要创建一个实例。
    ioloop.IOLoop.current().start()
