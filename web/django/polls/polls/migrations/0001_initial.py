# Generated by Django 4.1.4 on 2023-01-02 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='질문')),
                ('pub_date', models.DateTimeField(verbose_name='작성날짜')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0, verbose_name='투표')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question', verbose_name='연결된 질문')),
            ],
        ),
    ]
