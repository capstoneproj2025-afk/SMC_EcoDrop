# ======================================================================
# core/admin.py
# This file configures the Django admin interface for your models.
# ======================================================================

from django.contrib import admin
from .models import UserProfile, Entry, RewardItem, RedeemedPoints, Device, DeviceLog
import uuid

# Register your models here so they appear in the admin interface

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_points', 'qr_code_data')
    search_fields = ('user__username', 'user__email', 'qr_code_data')
    list_filter = ('total_points',)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'no_bottle', 'points', 'created_at')
    list_filter = ('created_at', 'points')
    search_fields = ('user_profile__user__username',)
    date_hierarchy = 'created_at'

@admin.register(RewardItem)
class RewardItemAdmin(admin.ModelAdmin):
    list_display = ('reward_name', 'points_required', 'icon')
    list_filter = ('points_required',)
    search_fields = ('reward_name',)

@admin.register(RedeemedPoints)
class RedeemedPointsAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'reward_item', 'redeemed_points', 'created_at')
    list_filter = ('created_at', 'reward_item')
    search_fields = ('user_profile__user__username', 'reward_item__reward_name')
    date_hierarchy = 'created_at'

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'device_id', 'location', 'status', 'total_bottles_processed', 'last_heartbeat')
    list_filter = ('status', 'created_at', 'last_heartbeat')
    search_fields = ('device_name', 'device_id', 'location')
    readonly_fields = ('api_key', 'total_bottles_processed', 'last_heartbeat', 'created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new device
            obj.api_key = str(uuid.uuid4())
        super().save_model(request, obj, form, change)

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ('device', 'log_type', 'sort_result', 'message', 'created_at')
    list_filter = ('log_type', 'sort_result', 'created_at', 'device')
    search_fields = ('device__device_name', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False  # Logs are created automatically, not manually
