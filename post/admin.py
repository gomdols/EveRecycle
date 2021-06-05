from django.contrib import admin
from .models import Archivement, Board, Bulletin, Clear_archivement, Memo, Recycle_tag, User

admin.site.register(User)
admin.site.register(Board)
admin.site.register(Bulletin)
admin.site.register(Archivement)
admin.site.register(Clear_archivement)
admin.site.register(Recycle_tag)
admin.site.register(Memo)