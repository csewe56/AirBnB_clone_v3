#!/usr/bin/python3
"""Index page"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review

classes = [User, Place, Amenity, State, City, Review]


@app_views.route('/status', strict_slashes=False)
def index_status():
    """Index route"""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """Get status"""
    return jsonify(
        users=storage.count(User)
        places=storage.count(Place),
        amenities=storage.count(Amenity),
        states=storage.count(State),
        cities=storage.count(City),
        reviews=storage.count(Review),
            )
