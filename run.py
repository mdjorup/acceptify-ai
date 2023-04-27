import logging

from firebase_admin import credentials, initialize_app

from app import app

if __name__ == "__main__":
    logging.basicConfig(filename='server.log', level=logging.INFO)
    logging.info("Starting server")

    #ENVIRONMENT VARIABLES


   
    # CONNECTIONS
    cred = credentials.Certificate(app.config["FIREBASE_ADMIN_SDK"])
    initialize_app(cred)
    


    # get all environment variables and add to app.config
    app.run()