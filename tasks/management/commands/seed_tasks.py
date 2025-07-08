"""
Django management command to seed the database with sample tasks.
"""

from django.core.management.base import BaseCommand
from tasks.models import Task


class Command(BaseCommand):
    help = 'Seed the database with sample tasks'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing tasks before seeding',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing tasks...')
            Task.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared all existing tasks'))

        # Sample tasks to create
        sample_tasks = [
            {
                'title': 'Fix login button on mobile',
                'description': 'The login button does not work on mobile devices. Users are unable to authenticate.',
                'status': False
            },
            {
                'title': 'Add dark mode toggle',
                'description': 'Implement a dark mode feature that allows users to switch between light and dark themes.',
                'status': False
            },
            {
                'title': 'Optimize database queries',
                'description': 'Improve performance by optimizing slow database queries in the user dashboard.',
                'status': True
            },
            {
                'title': 'Create user documentation',
                'description': 'Write comprehensive documentation for end users explaining how to use the application.',
                'status': False
            },
            {
                'title': 'Fix memory leak in background worker',
                'description': 'Background worker process consumes increasing amounts of memory over time.',
                'status': False
            },
            {
                'title': 'Add export functionality',
                'description': 'Allow users to export their data in CSV and JSON formats.',
                'status': True
            }
        ]

        self.stdout.write('Creating sample tasks...')
        created_count = 0
        
        for task_data in sample_tasks:
            task, created = Task.objects.get_or_create(
                title=task_data['title'],
                defaults={
                    'description': task_data['description'],
                    'status': task_data['status']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(f'Created task: {task.title}')
            else:
                self.stdout.write(f'Task already exists: {task.title}')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new tasks')
        )
        self.stdout.write(f'Total tasks in database: {Task.objects.count()}')