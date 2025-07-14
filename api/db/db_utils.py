from . import db
from sqlalchemy.exc import SQLAlchemyError
from models import Ride  # ✅ اگر models.py db فولڈر میں ہو


def get_ride_status(ride_id):
    try:
        ride = db.session.get(Ride, ride_id)
        if ride:
            return (ride.status, ride.issue)
        else:
            return ("not_found", None)
    except SQLAlchemyError as e:
        print("❌ Error getting ride:", e)
        return ("error", None)
