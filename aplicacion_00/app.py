import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()