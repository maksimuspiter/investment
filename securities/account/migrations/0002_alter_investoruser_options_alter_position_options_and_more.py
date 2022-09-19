# Generated by Django 4.1.1 on 2022-09-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investoruser',
            options={'ordering': ['last_name'], 'verbose_name': 'Инвестор', 'verbose_name_plural': 'Инвесторы'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['investor'], 'verbose_name': 'Открытая позиция', 'verbose_name_plural': 'Открытые позиции'},
        ),
        migrations.RenameField(
            model_name='securities',
            old_name='title',
            new_name='type_securities',
        ),
        migrations.AlterField(
            model_name='position',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='открытая позиция'),
        ),
    ]