python3 ../manage.py shell -c 'from django.core.management import call_command; from django_extensions.management.commands.show_urls import Command; call_command(Command())' > all_urls.txt
