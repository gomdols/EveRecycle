from post.serializers import UserSerializer, ArchivementSerializer, BoardSerializer, BulletinSerializer, RecycleTagSerializer, MemoSerializer, ClearArchivementSerializer
from post.models import User, Archivement, Board, Bulletin, Recycle_tag, Memo, Clear_archivement
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArchivementViewSet(viewsets.ModelViewSet):
    queryset = Archivement.objects.all()
    serializer_class = ArchivementSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BulletinViewSet(viewsets.ModelViewSet):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer


class RecycleTagViewSet(viewsets.ModelViewSet):
    queryset = Recycle_tag.objects.all()
    serializer_class = RecycleTagSerializer


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer


class ClearArchivementViewSet(viewsets.ModelViewSet):
    queryset = Clear_archivement.objects.all()
    serializer_class = ClearArchivementSerializer