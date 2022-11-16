import json
from random import randint
from time import sleep
from . models import Data
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.starin_data = await self.get_strain()
        await self.send(json.dumps({'value': self.starin_data}))
    
    @database_sync_to_async
    def get_strain(self):
        return Data.objects.all()[0].strain

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']
 
        await self.channel_layer.group_send(
              self.groupname,
              {
                  'type':'deprocessing',
                  'value': val
              }
        )   

        print('>>-->>', text_data)

    async def deprocessing(self, event):
        valOther =event['value']
        await self.send(text_data=json.dumps({'value':valOther}))

    async def disconnect(self, close_value):
        pass


# class GraphConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         self.starin_data = await self.get_strain()
#         await self.send(json.dumps({'value': self.starin_data}))

#         self.room_group_name = 'disp_room'
#         self.counter = await database_sync_to_async(self.get_counter)()

#         await (self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.accept()
    
#     @database_sync_to_async
#     def get_strain(self):

#         return Data.objects.all()[0].strain

#     async def receive(self, text_data):
#         datapoint = json.loads(text_data)
#         val =datapoint['value']
 
#         await self.channel_layer.group_send(
#               self.groupname,
#               {
#                   'type':'deprocessing',
#                   'value': val
#               }
#         )

#         print('>>-->>', text_data)
    
#     async def chat_message(self, event):
#         message_klik = event['klik']
#         message_klak = event['klak']
#         await self.send(text_data=json.dumps({
#             'klik': message_klik,
#             'klak': message_klak
#         }))
    
#     async def disconnect(self, close_code):
#         await (self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.close()

#     async def deprocessing(self, event):
#         valOther =event['value']
#         await self.send(text_data=json.dumps({'value':valOther}))

#     async def disconnect(self, close_value):
#         pass
