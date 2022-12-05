from flask_frozen import Freezer
from david import app

FREEZER_DESTINATION='.'
freezer = Freezer(app)

if __name__ == '__main__':
        freezer.freeze()
