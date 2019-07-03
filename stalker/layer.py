from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import OutgoingAckProtocolEntity
from yowsup.layers.protocol_presence.protocolentities import *
from yowsup.layers.protocol_contacts.protocolentities import GetSyncIqProtocolEntity, ResultSyncIqProtocolEntity
from yowsup.layers.protocol_iq.protocolentities import *
from yowsup.layers.protocol_chatstate.protocolentities import *
from yowsup.layers.protocol_ib.protocolentities.clean_iq import CleanIqProtocolEntity
from yowsup.common import YowConstants
from yowsup.common.tools import Jid

import time
from datetime import datetime
import logging

class StalkerLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("presence")
    def onPresenceChange(self, entity):
        number = (str)(entity._from.split('@')[0])
        if(entity.getType() == None):
            state = "online"
            online = "1"
            timestamp = (str)((int)(time.mktime(datetime.today().timetuple())))
        else:
            state = "offline"
            online = "0"
            if (entity.last == "deny" or entity.last == "none"):
                timestamp = (str)((int)(time.mktime(datetime.today().timetuple())))
            else:
                timestamp = (str)(entity.last)
        sql = "INSERT INTO logs (number_id, time, online) SELECT numbers.id, "+timestamp+", "+online+" FROM numbers WHERE number="+number
        self.dbHelper.doQuery(sql, False)
        logging.info(number + " is now " + state + "(" + time.strftime("%H:%M:%S", time.localtime()) + ")")
        print(number + " is now " + state + "(" + time.strftime("%H:%M:%S", time.localtime()) + ")")

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
        #outgoingMessageProtocolEntity = TextMessageProtocolEntity(
        #    "Your message was: " + messageProtocolEntity.getBody(),
        #    to = messageProtocolEntity.getFrom())
        #logging.info(messageProtocolEntity.getFrom() + ":" + messageProtocolEntity.getBody())
        #print(messageProtocolEntity.getFrom() + ":" + messageProtocolEntity.getBody())
        print("msg from: " + messageProtocolEntity.getFrom())
        self.toLower(receipt)
        #self.toLower(outgoingMessageProtocolEntity)
        self.toLower(SubscribePresenceProtocolEntity(messageProtocolEntity.getFrom()))
    
    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
        
    @ProtocolEntityCallback("success")
    def onSuccess(self, successProtocolEntity):
        self.startNumbers(self.contacts)
        self.dbHelper.doQuery("INSERT INTO script_starts (time) VALUES (" + (str)((int)(time.mktime(datetime.today().timetuple()))) + ")", False)
        self.toLower(CleanIqProtocolEntity("groups", YowConstants.DOMAIN))
        logging.info("Numbers started")
        print("Numbers started")
        
    def startNumbers(self, numbers):
        contactEntity = GetSyncIqProtocolEntity(numbers)
        self._sendIq(contactEntity, self.onGetSyncResult, self.onGetSyncError)
        time.sleep(0.5)
        self.toLower(AvailablePresenceProtocolEntity())
        time.sleep(2)
        self.doSubscribe(numbers);
    
    def doSubscribe(self, numbers):
        for number in numbers:
            self.toLower(SubscribePresenceProtocolEntity(Jid.normalize(number)))
            time.sleep(0.1) 

    def onGetSyncResult(self, resultSyncIqProtocolEntity, originalIqProtocolEntity):
        logging.info(resultSyncIqProtocolEntity)
        print(resultSyncIqProtocolEntity)

    def onGetSyncError(self, errorSyncIqProtocolEntity, originalIqProtocolEntity):
        logging.info(errorSyncIqProtocolEntity)
        print(errorSyncIqProtocolEntity)
                
    def sendMsg(self, content):
        self.toLower(AvailablePresenceProtocolEntity())
        time.sleep(1.5)
        self.toLower(OutgoingChatstateProtocolEntity(ChatstateProtocolEntity.STATE_TYPING, Jid.normalize("4915905347961")))
        outgoingMessage = TextMessageProtocolEntity(content.encode("utf-8"), to = Jid.normalize("4915905347961"))
        self.toLower(outgoingMessage)
        time.sleep(0.5)
        self.toLower(OutgoingChatstateProtocolEntity(ChatstateProtocolEntity.STATE_PAUSED, Jid.normalize("4915905347961")))