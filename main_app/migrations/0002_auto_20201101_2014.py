# Generated by Django 3.1.2 on 2020-11-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='lccn',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='unknown', max_length=13),
        ),
        migrations.AddField(
            model_name='book',
            name='word_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('AA', 'Action and Adventures'), ('CL', 'Classics'), ('GC', 'Graphic Novels/Comic Books'), ('DM', 'Detective/Mysteries'), ('FA', 'Fantasies'), ('HF', 'Historical Fiction'), ('HR', 'Horror'), ('LF', 'Literary Fiction'), ('RO', 'Romance'), ('SF', 'Science Fiction'), ('SS', 'Short Stories'), ('ST', 'Suspense/Thrillers'), ('AB', 'Autobiographies/Biographies'), ('CO', 'Cookbooks'), ('HI', 'History'), ('PO', 'Poetry'), ('SH', 'Self-Help'), ('TC', 'True Crime')], default='LF', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_published',
            field=models.IntegerField(),
        ),
    ]
