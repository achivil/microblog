#! microblog/bin/python

from app import app
import logging
logging.basicConfig(filename='logger.txt', level=logging.DEBUG)
app.run(debug = True)
#app.run()
