from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import UserProfile
import uuid

class Command(BaseCommand):
    help = 'Fix missing student IDs and QR codes for existing users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--set-student-id',
            type=str,
            help='Set student ID for a specific username (format: username:student_id)',
        )

    def handle(self, *args, **options):
        if options['set_student_id']:
            # Set specific student ID
            try:
                username, student_id = options['set_student_id'].split(':')
                user = User.objects.get(username=username)
                user.profile.student_id = student_id
                user.profile.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Set student ID for {username}: {student_id}')
                )
            except ValueError:
                self.stdout.write(
                    self.style.ERROR('Format should be: --set-student-id username:student_id')
                )
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'User {username} not found')
                )
            return

        self.stdout.write("Checking user profiles...")
        
        # Get all users
        users = User.objects.all()
        fixed_count = 0
        
        for user in users:
            try:
                profile = user.profile
                
                # Set student_id to username if missing (default behavior)
                if not profile.student_id:
                    profile.student_id = user.username
                    profile.save()
                    self.stdout.write(
                        self.style.SUCCESS(f'Set student ID for {user.username}: {profile.student_id}')
                    )
                    fixed_count += 1
                
                # Show current status
                self.stdout.write(f'{user.username}: student_id={profile.student_id}, points={profile.total_points}')
                
            except UserProfile.DoesNotExist:
                # Create profile if it doesn't exist
                UserProfile.objects.create(
                    user=user,
                    student_id=user.username,  # Default to username
                    qr_code_data=f"SMC-USER-{user.username}-{str(uuid.uuid4())[:8]}"
                )
                self.stdout.write(
                    self.style.WARNING(f'Created profile for {user.username} with student_id: {user.username}')
                )
                fixed_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Fixed {fixed_count} users. Total users: {users.count()}')
        )
        
        self.stdout.write("\nTo set a specific student ID, use:")
        self.stdout.write("python manage.py fix_qr_codes --set-student-id username:student_id_number")
