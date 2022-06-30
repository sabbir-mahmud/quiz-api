# Generated by Django 4.0.5 on 2022-06-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_quiz_question_title_remove_quizzes_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_question',
            name='question',
        ),
        migrations.AddField(
            model_name='quiz_question',
            name='title',
            field=models.CharField(default='what is react', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
