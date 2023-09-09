from flask import Flask
from flask_cors import CORS

from ingestor.controller import ingestor_blueprint
from chatbot_response.controller import chatbot_blueprint
from instruments.controller import instruments_blueprint
from price_values.controller import price_values_blueprint
from funds.controller import funds_blueprint


app = Flask(__name__)
CORS(app)
app.register_blueprint(ingestor_blueprint, url_prefix='/ingest')
app.register_blueprint(chatbot_blueprint, url_prefix='/chatbot')
app.register_blueprint(instruments_blueprint, url_prefix='/instruments')
app.register_blueprint(funds_blueprint, url_prefix='/funds')
app.register_blueprint(price_values_blueprint, url_prefix='/price_values')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
