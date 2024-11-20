# main script to interact with a product management system
import os
from waitress import serve
from .db.db_connection import DbConnection
from .db.migrate import migrate_db
from .db.adapters.product_adapter import ProductAdapter
from .webserver.api import api

DEBUG_SERVER = False


def main():
    is_docker = os.environ.get("DOCKER", False)

    if is_docker:
        backend_host = os.environ["BACKEND_HOST"]
        backend_port = os.environ["BACKEND_PORT"]
        user = os.environ["DB_USER"]
        password = os.environ["DB_PASSWORD"]
        host = os.environ["DB_HOST"]
    else:
        print("Not running in Docker environment")
        backend_host = "localhost"
        backend_port = 8080
        user = "root"
        password = "root"
        host = "localhost"

    # Setup the DB singleton
    db = DbConnection(user, password, host, "lager")
    migrate_db(db, "migrations/")

    if DEBUG_SERVER:
        api.run()
    else:
        serve(api, host=backend_host, port=backend_port)


if __name__ == "__main__":
    main()
