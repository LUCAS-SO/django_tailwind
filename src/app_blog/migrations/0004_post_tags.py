# Generated by Django 5.2.3 on 2025-06-29 19:08

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_categoria_post_categoria'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
