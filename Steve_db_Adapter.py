import sys
import os
import time as Time
import simplejson as json

import datetime
from datetime import timezone
from psycopg2 import sql
import psycopg2.extras

class Steve_db():
    def __init__(self, db='sensor_data', host='10.0.0.8', user='pi', password='321'):
        self.db = db
        self.host = host
        self.user = user
        self.password = password
        self.conn = str("host="+self.host +
                                     " dbname="+self.db +
                                     " user="+self.user +
                                     " password="+self.password
                                     )
                                    

    def validity_by_time(self):
        """
        checks to see what the oldest entry in the database is. if its too old then return Fasle
        """
        conn = psycopg2.connect(self.conn)
        permissable_maximum_age_secs = 600  # 600s = 10mins
        query = "SELECT time FROM steve_sense_sensor_logs ORDER BY time DESC LIMIT 1"
        cur = conn.cursor()
        cur.execute(query)
        queryResult = cur.fetchall()
        age_seconds = (datetime.datetime.now(
            timezone.utc) - queryResult[0][0]).seconds
        cur.close()
        conn.close()
        if age_seconds > permissable_maximum_age_secs:
            print("Check Sensor, last sample is "+str(age_seconds)+" old")
            return False
        else:
            return True

    def fetch_latest_sample(self, sensor_id):
        """
        Get the latest sample and make it an average if its a number
        """
        conn = psycopg2.connect(self.conn)
        query = "SELECT * FROM steve_sense_sensor_logs WHERE sensor_id = '{}' ORDER BY time DESC LIMIT 1".format(
                sensor_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        data = json.loads(json.dumps(
            cur.fetchall(), use_decimal=True, default=str))
        cur.close()
        conn.close()
        return data

    def fetch_param_item(self, field,sensor_id):
        conn = psycopg2.connect(self.conn)
        query = "SELECT {} from steve_sense_environmental_settings WHERE sensor_id = '{}'".format(
            field,sensor_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        data = json.loads(json.dumps(
            cur.fetchall(), use_decimal=True, default=str))
        cur.close()
        conn.close()
        for i, j in data[0].items():
            return i, j

    def fetch_params(self, space_id):
        """
        Get the latest sample and make it an average if its a number
        """
        conn = psycopg2.connect(self.conn)
        query = "SELECT * FROM steve_sense_environmental_settings WHERE space_id = '{}'".format(
                space_id)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        data = json.loads(json.dumps(
            cur.fetchall(), use_decimal=True, default=str))
        cur.close()
        conn.close()
        return data

    def insert(self, key, value):  # broke as fuck
        query = "UPDATE steve_sense_environmental_settings SET {} = {}".format(
            key, value)
        cur = self.conn.cursor()
        cur.execute(query, (key, value))
        self.conn.commit()
        cur.close()
        self.conn.close()
        return True

