import matplotlib.pyplot as plt
import pandas as pd
from os import listdir

def generateDatabase():
    filepaths = [("indego_data/" + f) for f in listdir("indego_data/") if f.endswith('.csv')]
    return pd.concat(map(pd.read_csv, filepaths), sort=False)
def sanitizeData(df):
    #replaces Day Pass with One Day Pass from before there was Two Day Pass
    df['passholder_type'] = df['passholder_type'].replace(to_replace={'^Day Pass': 'One Day Pass'}, regex=True)
    #drops incomplete ride data, does not drop it if bike type is na because early data did not have this since only regular bikes
    df = df.dropna(subset=['trip_id', 'duration', 'start_time', 'end_time', 'plan_duration', 'passholder_type', 'start_station', 'start_lat', 'start_lon', 'end_station', 'end_lat', 'end_lon', 'bike_id', 'trip_route_category'])
    #removes trips that start or end at a Virtual Station (station id is 3000) b/c these are usually anomalous
    df = df[(df['start_station'] != 3000)]
    df = df[(df['end_station'] != 3000)]
    #duration should be capped at 24 hr per Indego documentation but is not always done
    df = df[(df['duration'] < (24*60))]
    return df
def dropUnusedColumns(df):
    return df.drop(['trip_id', 'start_station', 'start_lat', 'start_lon', 'end_station', 'end_lat', 'end_lon', 'bike_id', 'trip_route_category', 'bike_type'], axis=1)
def generatePassholderTripLengthPlot(df):
    df = df.drop(['end_time', 'plan_duration'], axis=1)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df = df[df['start_time'] > pd.Timestamp(2017, 4, 1)] #removes data from before 2017 Q2 because technical issues causes duration to be inaccurate
    df.boxplot(by=['passholder_type'], showfliers=False)
    plt.ylabel('Trip Length (minutes)')
    plt.xlabel('Passholder Type')
    plt.xticks(rotation=30)
    plt.title('Passholder Type vs Trip Length')
    plt.savefig('Passholder_Type_vs_Trip_Length.png')
def generatePassholderSumPlot(df):
    df = df.drop(['start_time', 'end_time', 'plan_duration'], axis=1)
    df = df.groupby('passholder_type').count()
    df.plot.pie(x='passholder_type', y='duration')
    plt.ylabel('')
    plt.savefig('Rides_Per_Passholder_Type.png')
def generateWeekdayTimeTrips(df):
    df = df.drop(['passholder_type', 'end_time', 'plan_duration', 'duration'], axis=1)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['start_hour_min'] = df['start_time'].dt.time
    df = df[df['start_time'].dt.dayofweek < 5]
    df = df.groupby('start_hour_min').count()
    df.plot.line()
    plt.xticks(rotation=30)
    plt.title('Weekday Trips')
    plt.ylabel('Total number of trips')
    plt.savefig('weekday_trips_by_time.png')
def generateWeekendTimeTrips(df):
    df = df.drop(['passholder_type', 'end_time', 'plan_duration', 'duration'], axis=1)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['start_hour_min'] = df['start_time'].dt.time
    df = df[df['start_time'].dt.dayofweek > 4]
    df = df.groupby('start_hour_min').count()
    df.plot.line()
    plt.xticks(rotation=30)
    plt.title('Weekend Trips')
    plt.ylabel('Total number of trips')
    plt.savefig('weekend_trips_by_time.png')
def generateRideOverTime(df):
    df = df.drop(['passholder_type', 'end_time', 'plan_duration', 'duration'], axis=1)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['start_day'] = df['start_time'].dt.date
    df = df.groupby('start_day').count()
    df.plot.line()
    plt.xticks(rotation=30)
    plt.title('Daily Trips')
    plt.ylabel('Total number of trips')
    plt.savefig('daily_trips.png')
def generateDurationOverTimeUnadjusted(df):
    df = df.drop(['passholder_type', 'end_time', 'plan_duration'], axis=1)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['start_day'] = df['start_time'].dt.date
    df = df.groupby('start_day').mean()
    df.plot.line()
    plt.xticks(rotation=30)
    plt.title('Average Duration per Day')
    plt.ylabel('Average Duration of trips')
    plt.savefig('duration_of_daily_trips_unadjusted.png')
def generateDurationOverTime(df):
    df = df.drop(['passholder_type', 'end_time', 'plan_duration'], axis=1)
    df['start_time'] = pd.to_datetime(df['start_time'])
    df = df[df['start_time'] > pd.Timestamp(2017, 4, 1)] #removes data from before 2017 Q2 because technical issues causes duration to be inaccurate
    df['start_day'] = df['start_time'].dt.date
    df = df.groupby('start_day').mean()
    df.plot.line()
    plt.xticks(rotation=30)
    plt.title('Average Duration per Day')
    plt.ylabel('Average Duration of trips')
    plt.savefig('duration_of_daily_trips.png')


db = generateDatabase()
db = sanitizeData(db)
db = dropUnusedColumns(db)
generatePassholderTripLengthPlot(db)
generatePassholderSumPlot(db)
generateWeekdayTimeTrips(db)
generateWeekendTimeTrips(db)
generateRideOverTime(db)
generateDurationOverTimeUnadjusted(db)
generateDurationOverTime(db)
