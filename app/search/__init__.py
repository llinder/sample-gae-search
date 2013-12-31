from flask import Flask
import settings


# create application
app = Flask('search')
app.config.from_object('search.settings')

# Views
import views
