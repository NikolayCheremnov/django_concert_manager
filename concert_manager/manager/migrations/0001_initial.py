# Generated by Django 3.2 on 2021-04-29 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LiveSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NonProgrammableConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_sample', models.CharField(max_length=200)),
                ('sub_sample', models.CharField(max_length=200)),
                ('left_sample', models.CharField(max_length=200)),
                ('split', models.CharField(max_length=200)),
                ('octave_upper', models.IntegerField()),
                ('octave_lower', models.IntegerField()),
                ('transpose', models.IntegerField()),
                ('other', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammableConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('non_programmable_configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.nonprogrammableconfiguration')),
                ('programmable_configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.programmableconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='SongSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_in_set', models.IntegerField(unique=True)),
                ('live_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.liveset')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.song')),
            ],
        ),
        migrations.CreateModel(
            name='ConcertLiveSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_in_concert', models.IntegerField(unique=True)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.concert')),
                ('live_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.liveset')),
            ],
        ),
    ]
