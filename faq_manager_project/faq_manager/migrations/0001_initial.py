# Generated by Django 5.1.5 on 2025-02-02 00:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='Question in English')),
                ('answer', ckeditor.fields.RichTextField()),
                ('question_hi', models.TextField(blank=True, help_text='Hindi translation', null=True)),
                ('question_bn', models.TextField(blank=True, help_text='Bengali translation', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'ordering': ['-created_at'],
            },
        ),
    ]
