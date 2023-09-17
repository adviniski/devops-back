from urllib.parse import quote
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

SERVER=os.environ.get("DEVOPS_DATABASE_SERVER")
PACKAGE=os.environ.get("DEVOPS_DATABASE_PACKAGE")
DATABASE=os.environ.get("DEVOPS_DATABASE_NAME")
USER=os.environ.get("DEVOPS_DATABASE_USERNAME")
PASSWD=os.environ.get("DEVOPS_DATABASE_PASSWORD")
HOST=os.environ.get("DEVOPS_DATABASE_HOST")
PORT=os.environ.get("DEVOPS_DATABASE_PORT")

metadata = MetaData()
instance = f"{SERVER}+{PACKAGE}://{USER}:{quote(str(PASSWD))}@{HOST}:{PORT}/{DATABASE}"
db = SQLAlchemy(metadata=metadata)
