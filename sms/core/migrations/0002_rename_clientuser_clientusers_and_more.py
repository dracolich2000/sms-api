# Generated by Django 5.1.4 on 2024-12-10 06:51

import core.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientUser',
            new_name='ClientUsers',
        ),
        migrations.RenameField(
            model_name='clientusers',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='clientusers',
            old_name='deleted_at',
            new_name='deletedAt',
        ),
        migrations.RenameField(
            model_name='clientusers',
            old_name='updated_at',
            new_name='updatedAt',
        ),
        migrations.AddField(
            model_name='company',
            name='revenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[core.models.validate_email]),
        ),
        migrations.AlterField(
            model_name='company',
            name='employees',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(max_length=255),
        ),
    ]