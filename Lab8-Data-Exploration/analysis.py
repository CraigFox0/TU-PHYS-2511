import matplotlib.pyplot as plt
import pandas as pd
from os import listdir

#compare duration w/ time of day
#compare bike_type w/ plan_duration

#figure out why duration vs plan duration no work

#duration, start_time, end_time, plan_duration, passholder_type

#correlate weather/precipitation/sunlight/temp

def generateDatabase():
    filepaths = [("indego_data/" + f) for f in listdir("indego_data/") if f.endswith('.csv')]
    return pd.concat(map(pd.read_csv, filepaths), sort=False)
def sanitizeData(database):
    #replaces Day Pass with One Day Pass from before there was Two Day Pass
    database['passholder_type'] = database['passholder_type'].replace(to_replace={'^Day Pass': 'One Day Pass'}, regex=True)
    #drops incomplete ride data, does not drop it if bike type is na because early data did not have this since only regular bikes
    database = database.dropna(subset=['trip_id', 'duration', 'start_time', 'end_time', 'plan_duration', 'passholder_type', 'start_station', 'start_lat', 'start_lon', 'end_station', 'end_lat', 'end_lon', 'bike_id', 'trip_route_category'])
    #removes trips that start or end at a Virtual Station (station id is 3000) b/c these are usually anomalous
    database = database[(database['start_station'] != 3000)]
    database = database[(database['end_station'] != 3000)]
    #duration should be capped at 24 hr per Indego documentation but is not always done
    database = database[(database['duration'] < (24*60))]
    return database
def dropUnusedColumns(database):
    return database.drop(['trip_id', 'start_station', 'start_lat', 'start_lon', 'end_station', 'end_lat', 'end_lon', 'bike_id', 'trip_route_category', 'bike_type'], axis=1)
def generatePassholderTripLengthPlot(database):
    database = database.drop(['start_time', 'end_time', 'plan_duration'], axis=1)
    database.boxplot(by=['passholder_type'], showfliers=False)
    plt.ylabel('Trip Length (minutes)')
    plt.xlabel('Passholder Type')
    plt.xticks(rotation=30)
    plt.ylim(0, 24*60)
    plt.title('Passholder Type vs Trip Length')
    plt.savefig('Passholder_Type_vs_Trip_Length.png')
def generatePassholderSumPlot(database):
    database = database.drop(['start_time', 'end_time', 'plan_duration'], axis=1)
    database = database.groupby('passholder_type').count()
    database.plot.pie(x='passholder_type', y='duration')
    plt.ylabel('')
    plt.savefig('Rides_Per_Passholder_Type.png')


db = generateDatabase()
db = sanitizeData(db)
db = dropUnusedColumns(db)
generatePassholderTripLengthPlot(db)
generatePassholderSumPlot(db)
