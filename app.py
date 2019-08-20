# 1. import Flask
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Function to covert string to datetime 
def s_to_d(date_time): 
    format = '%Y-%m-%d' # The format 
    datetime_str = dt.datetime.strptime(str(date_time), format) 
   
    return datetime_str

def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)

    # adjust the query based on the incomming parameters
    
    if not start_date.strip() and not end_date.strip():
        #both are empty
        return
    elif start_date.strip() and not end_date.strip():
        #start_date has value
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    elif not start_date.strip() and end_date.strip():    
        #end_date has value
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date <= end_date).all()
        # return

    else:
        return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
        # return
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precp():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all Measurement
    # results = session.query(Measurement.date).all()
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    all_data = []
    for date, prcp in results:
        data_dict = {}
        data_dict["Date"] = date
        data_dict["Precipitation"] = prcp
        all_data.append(data_dict)

    return jsonify(all_data)


@app.route("/api/v1.0/stations")
def st():

    session = Session(engine)

    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_st = list(np.ravel(results))

    return jsonify(all_st)

@app.route("/api/v1.0/tobs")
def temp():
    session = Session(engine)

    # last_date = session.query(Measurement.date).order_by(desc(Measurement.date)).first()
    # one_year_ago = s_to_d(last_date) - dt.timedelta(days=365)
    # results = session.query(Measurement.tobs).filter(Subject.time > ten_weeks_ago).all()
    tobs_last_year_query = '''
                    select tobs
                    from measurement
                    where date >= (  select  DATE(max(date), '-12 MONTHS') 
                                    from measurement
                                )
                    order by 1
    '''
    tobs_12month = engine.execute(tobs_last_year_query).fetchall()
    tobs = [tobs_12month[0] for tobs_12month in tobs_12month[0:]]

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(tobs))

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def start_date(start):

    session = Session(engine)

    results = calc_temps(start, "")
    # results = session.query(Measurement.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)

    results = calc_temps(start, end)

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

if __name__ == "__main__":
    app.run(debug=True)
