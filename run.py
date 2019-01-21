from app import initialise_app

app = initialise_app()


if __name__=='__main__':
    app.config["DEBUG"] = True
    app.run()