# Generated by Django 3.2.9 on 2021-11-27 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211118_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentity',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_following', models.DateTimeField(auto_now_add=True)),
                ('following_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='users.userentity')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='users.userentity')),
            ],
            options={
                'unique_together': {('user_id', 'following_user_id')},
            },
        ),
    ]