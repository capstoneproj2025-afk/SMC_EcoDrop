# ======================================================================
# core/models.py
# This file defines your database structure based on your ERD.
# I've added the suggested 'total_points' field to the UserProfile
# for better performance.
# ======================================================================

from django.db import models
from django.contrib.auth.models import User

# Extends Django's built-in User model to include points
class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    total_points = models.PositiveIntegerField(default=0)
    # This field will store the student ID number from their ID card
    student_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    # Keep the old field for backward compatibility
    qr_code_data = models.CharField(max_length=100, unique=True, blank=True, null=True)
    # User type field to distinguish between student, teacher, and admin
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')

    def __str__(self):
        return self.user.username

# A record of a bottle deposit transaction
class Entry(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    no_bottle = models.PositiveIntegerField(default=1)
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.points} points"

# A record of a reward that can be redeemed
class RewardItem(models.Model):
    reward_name = models.CharField(max_length=100)
    points_required = models.PositiveIntegerField()
    # You can add quantity or status if needed
    # quantity = models.PositiveIntegerField(default=100)
    # is_active = models.BooleanField(default=True)
    icon = models.CharField(max_length=10, default='🏆') # Added for visual flair

    def __str__(self):
        return self.reward_name

# A record of when a user redeems their points for a reward
class RedeemedPoints(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reward_item = models.ForeignKey(RewardItem, on_delete=models.CASCADE)
    redeemed_points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username} redeemed {self.reward_item.reward_name}"

# Physical device management
class Device(models.Model):
    DEVICE_STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('maintenance', 'Maintenance'),
        ('error', 'Error'),
    ]
    
    device_id = models.CharField(max_length=50, unique=True)
    device_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    api_key = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=DEVICE_STATUS_CHOICES, default='offline')
    last_heartbeat = models.DateTimeField(null=True, blank=True)
    total_bottles_processed = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_name} ({self.device_id})"

# Device activity logs
class DeviceLog(models.Model):
    LOG_TYPE_CHOICES = [
        ('bottle_detected', 'Bottle Detected'),
        ('bottle_sorted', 'Bottle Sorted'),
        ('error', 'Error'),
        ('maintenance', 'Maintenance'),
        ('heartbeat', 'Heartbeat'),
    ]
    
    SORT_RESULT_CHOICES = [
        ('plastic', 'Plastic (Valid)'),
        ('invalid', 'Invalid (Not Plastic)'),
        ('error', 'Error'),
    ]
    
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    log_type = models.CharField(max_length=20, choices=LOG_TYPE_CHOICES)
    sort_result = models.CharField(max_length=10, choices=SORT_RESULT_CHOICES, null=True, blank=True)
    sensor_data = models.JSONField(null=True, blank=True)  # Store IR/CAP sensor readings
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.device_name} - {self.log_type} at {self.created_at}"
