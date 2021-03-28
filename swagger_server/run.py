import os

import connexion
from werkzeug.exceptions import BadRequest

from swagger_server import db
from swagger_server import encoder
from swagger_server.exceptions import EXCEPTION_PRODUCERS


def main():
    class RequestBodyValidator(connexion.decorators.validation.RequestBodyValidator):
        def validate_schema(self, data, url):
            exception_producer_key = url.split('8080/')[-1]
            if self.is_null_value_valid and connexion.utils.is_null(data):
                return None
            errors = list(self.validator.iter_errors(data))
            if errors:
                if exception_producer_key in EXCEPTION_PRODUCERS:
                    EXCEPTION_PRODUCERS[exception_producer_key](data, errors)
                else:
                    raise BadRequest(description=','.join([e.message for e in errors]))

    connex_app = connexion.FlaskApp(
        __name__,
        specification_dir='./swagger/'
    )
    connex_app.app.json_encoder = encoder.JSONEncoder

    connex_app.add_api(
        'swagger.yaml',
        arguments={'title': 'Candy Delivery App'},
        pythonic_params=True,
        validator_map={'body': RequestBodyValidator},
    )

    app = connex_app.app

    app.config['MONGODB_SETTINGS'] = {
        'db': os.getenv('MONGO_DATABASE', 'candy_app'),
        'host': os.getenv('MONGO_HOST', 'localhost'),
        'port': int(os.getenv('MONGO_PORT', '27017')),
    }

    db.init_app(app)

    from swagger_server.exceptions import EXCEPTION_HANDLERS
    for error, handler in EXCEPTION_HANDLERS.items():
        connex_app.add_error_handler(error, handler)

    connex_app.run(port=8080)


if __name__ == '__main__':
    main()
