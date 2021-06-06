from rest_framework import serializers
from .models import User, Archivement, Board, Bulletin, Memo, Recycle_tag, Clear_archivement



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'password',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'followers',
            'groups',
            'user_permissions',
        )
        model = User


class ArchivementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'archive_name',
            'archive_info',
            'archive_tier',
        )
        model = Archivement


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'board_name',
            'board_type',
        )
        model = Board


class BulletinSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'bulletin_title',
            'bulletin_contents',
            'bulletin_write_date',
            'bulletin_last_edit_date',
            'bulletin_recommend',
            'is_active',
            'is_notice',
            'board_id',
        )
        model = Bulletin


class RecycleTagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'tag_name_korean',
            'tag_name_english',
            'tag_info',
        )
        model = Recycle_tag


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'memo_contents',
            'memo_write_date',
            'memo_recommend',
            'memo_color',
            'bulletin',
            'user_id',
        )
        model = Memo


class ClearArchivementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'archive_date',
            'archive_id',
            'user_id',
        )
        model = Clear_archivement


