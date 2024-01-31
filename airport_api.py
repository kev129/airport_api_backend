from flask import Flask
from flask_cors import CORS
import os
import airport


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    return 'Welcome to airport API'


@app.route('/get_flights', methods=['GET'])
def get_flights():
    return airport.response(), 200


@app.route('/process_input', methods=['POST'])
def process_input_route():
    return airport.process_input(), 200


if __name__ == '__main__':
    app.run(debug=False)

    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': f'0.0.0.0:{int(os.environ.get("PORT", 8080))}',
            }

        def load(self):
            return app

    FlaskApplication().run()

    # from gunicorn.app.base import Application

    # class FlaskApplication(Application):
    #     def init(self, parser, opts, args):
    #         return {
    #             "success": True,
    #         }

    # Gunicorn("airport_api:app", forwarded_allow_ips="*")
