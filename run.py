from app import initialise_app

app = initialise_app()

if __name__ == '__main__':
    app.config.from_object('config.DevelopmentConfig')
    app.run()
