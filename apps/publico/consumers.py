import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GalleryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('gallery_group', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('gallery_group', self.channel_name)

    async def new_image(self, event):
        await self.send(text_data=json.dumps({
            'new_image': True
        }))