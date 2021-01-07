from rest_framework import routers

from .views import TodoView

router = routers.DefaultRouter()
router.register('todos', TodoView, 'todos')
# router.register('<The URL prefix>', <The viewset class>, '<The URL name>')

urlpatterns = router.urls