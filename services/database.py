from urllib.parse import quote
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

SERVER=os.environ.get("DEVOPS_SERVER")
PACKAGE=os.environ.get("DEVOPS_PACKAGE")
DATABASE=os.environ.get("DEVOPS_DATABASE")
USER=os.environ.get("DEVOPS_USERNAME")
PASSWD=os.environ.get("DEVOPS_PASSWORD")
HOST=os.environ.get("DEVOPS_HOST")
PORT=os.environ.get("DEVOPS_PORT")

metadata = MetaData()
instance = f"{SERVER}+{PACKAGE}://{USER}:{quote(str(PASSWD))}@{HOST}:{PORT}/{DATABASE}"
db = SQLAlchemy(metadata=metadata)
