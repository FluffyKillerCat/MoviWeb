from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
@errors.app_errorhandler(500)
@errors.app_errorhandler(400)
@errors.app_errorhandler(403)
@errors.app_errorhandler(405)
def handle_error(error):
    description = getattr(
        error, "description", "An unexpected error occurred."
    )
    return (
        render_template(
            "error.html", error=error, description=description
        ),  # noqa E501
        error.code,
    )