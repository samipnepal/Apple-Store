# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comments',
        ),
    ]
