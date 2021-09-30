import sys
import os
import time as Time
import simplejson as json

import datetime
from datetime import timezone
import psycopg2
from psycopg2 import sql
import psycopg2.extras

from Steve_Relay_Adapter import Relay
from Steve_db_Adapter import Steve_db

class Grow_Space():
    def __init__(self,space_id):
        self.parameters = []
        self.db_adapter = Steve_db()
        self.parameters.append(self.db_adapter.fetch_params(space_id))
        

        