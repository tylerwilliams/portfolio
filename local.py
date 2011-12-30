from main import *

app = web.application(urls, globals(), autoreload=True)

if __name__ == "__main__":
    app.run()