from yowsup.stacks import YowStackBuilder
from layer import StalkerLayer
#from yowsup.layers.auth import AuthError
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from yowsup.env import YowsupEnv

from threading import Thread
import time
import mysql.connector
import os
import logging

UPDATE_NUMBERS = 15
UPDATE_STATUS = 0.1
keepRunning = True

login_data = ("4915217207145", "e0rhFLogZXPrcO3Y9Yp6Cyno0aw=")

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S',filename='info.log',level=logging.INFO)

class LayerThread(Thread):
    def __init__(self, t, credentials, contacts):
        Thread.__init__(self)
        stackBuilder = YowStackBuilder()
        self.stalker = StalkerLayer()
        self.stalker.contacts = contacts
        self.stalker.dbHelper = t
        
        self.stack = stackBuilder\
            .pushDefaultLayers()\
            .push(self.stalker)\
            .build()
            
        self.stack.setProfile('77055764880')
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        #self.stack.setCredentials(credentials)
    def run(self):
        logging.info("layer running")
        print("layer running")
        self.stack.loop()

class DbHelper (Thread):
    def __init__(self):
        Thread.__init__(self)
        self.cnx = mysql.connector.connect(user='wa_logger', password='toor', host='localhost', database='whats-spy')
        
    def run(self):
        logging.info("dbHelper running")
        print("dbHelper running")
        
    def doQuery(self, query, fetch):
        logging.debug(query)
        print(query)
        cursor = self.cnx.cursor(buffered=True)
        cursor.execute(query)
        self.cnx.commit()
        if(fetch):
            result = cursor.fetchall()
            cursor.close()
            return result
        cursor.close()
        
    def stop(self):
        self.cnx.close()
        
class Updater(Thread):
    def __init__(self, t_db, t_layer):
        Thread.__init__(self)
        self.dbHelper = t_db
        self.stalker = t_layer.stalker
    
    def run(self):
        logging.info("updater running")
        print("updater running")
        while(True):
            time.sleep(UPDATE_NUMBERS * 60)
            logging.debug("Numbers Updated!");
            print("Numbers Updated!");
            numbers = []
            for number in self.dbHelper.doQuery("SELECT number FROM numbers", True):
                numbers.append(number[0])
            if(numbers != self.stalker.contacts):
                for number in numbers:
                    if(number not in self.stalker.contacts):
                        self.stalker.contacts.append(number)
                        self.stalker.startNumbers([number])
            time.sleep(UPDATE_NUMBERS * 60)
                        
dbHelper = DbHelper()
dbHelper.start()

numbers = []
for number in dbHelper.doQuery("SELECT number FROM numbers", True):
    numbers.append(number[0])

layerThread = LayerThread(dbHelper, login_data, numbers)
layerThread.start()

updater = Updater(dbHelper, layerThread)
updater.start()

while(keepRunning):
    while(layerThread.isAlive()):
        time.sleep(UPDATE_STATUS * 60)
    time.sleep(UPDATE_STATUS * 60)
    if(not layerThread.isAlive()):
        keepRunning = False
    
logging.critical("Layer crashed!")
print("Layer crashed!")
dbHelper.stop()
dbHelper.join()
os._exit(1)