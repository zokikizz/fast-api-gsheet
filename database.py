from deta import Deta
import sys
import os


def create_db_connection():
    project_key = os.getenv("DETA_PROJECT_KEY", None)
    if project_key is None:
        print("PROBLEM: There is no project key")
        sys.stdout.flush()

    deta = Deta(project_key)
    return deta.Base('gsheet_db')



