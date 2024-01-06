

# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter
# from channels.auth import AuthMiddlewareStack
# from Home import routing 

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mark_analyse.settings')

# application = ProtocolTypeRouter({
#         "http":get_asgi_application(),
#         'websocket':AuthMiddlewareStack(
#             URLRouter(
#                 routing.websocket_urlpatterns
#             )
#         )

# })

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from Home import routing  # Make sure the correct path to your routing module is imported

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mark_analyse.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

