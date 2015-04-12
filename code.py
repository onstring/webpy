import web

db = web.database(dbn='sqlite', db='MovieSite.db')

urls = (
    '/', 'index'
)

render =  web.template.render('templates/')

class index:
    def GET(self):
        movies = db.select('movie')
        return render.index(movies)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
