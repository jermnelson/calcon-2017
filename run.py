from app import app
from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9017, debug=True)
