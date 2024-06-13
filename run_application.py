from backend.app import app
import os
import json

if __name__ == '__main__':
    # Load configuration from config.json
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Set Flask app configuration
    app.config['DATABASE_HOST'] = config['database']['host']
    app.config['DATABASE_PORT'] = config['database']['port']
    app.config['DATABASE_USERNAME'] = config['database']['username']
    app.config['DATABASE_PASSWORD'] = config['database']['password']
    app.config['DATABASE_NAME'] = config['database']['database']

    # Run Flask app
    app.run(host=config['server']['host'], port=config['server']['port'])
