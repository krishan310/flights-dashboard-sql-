import  mysql.connector
class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Krishna@123',
                database='flights'
            )
            self.mycursor = self.conn.cursor()
            print('Connection done')

        except :
            print('No Connection')


    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
        select distinct(Source) from flights.flights 
        union 
        select distinct(Destination) from flights.flights ; 
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self , source , destination):
        self.mycursor.execute(""" 
        SELECT Airline  Route , Dep_Time , Duration ,Price  FROM flights.flights 
        where Source = '{}' and Destination = '{}'
        """.format(source , destination))

        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []
        self.mycursor.execute(""" 
        select Airline , COUNT(*) FROM flights.flights 
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline , frequency

    def busy_airport(self):
        city = []
        frequency1 = []
        self.mycursor.execute("""
        select source , count(*) from (select source from flights 
            union all 
            select Destination from flights) t 
            group by t.source 
            order by count(*) desc
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency1.append(item[1])

        return city, frequency1

    def daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute("""
        select Date_of_journey , COUNT(*) from flights 
        group by Date_of_journey
     
           """)
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency

