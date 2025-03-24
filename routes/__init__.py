from routes.error_routes import errors
from routes.user_routes import user
from routes.movie_routes import movie



def register_blueprints(app):
    app.register_blueprint(errors)
    app.register_blueprint(user)
    app.register_blueprint(movie)
