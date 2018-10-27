# Generated by Django 2.1.2 on 2018-10-27 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('subcategory', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('coords', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_num', models.CharField(max_length=255)),
                ('contact_email', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=4095)),
                ('tags', models.CharField(max_length=4095)),
                ('accessbility', models.CharField(max_length=4095)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Saved_Searches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('search', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.CharField(max_length=6000)),
                ('loc_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Locations')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('dob', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Warnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning', models.CharField(max_length=255)),
                ('loc_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Locations')),
            ],
        ),
        migrations.AddField(
            model_name='suggestions',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Users'),
        ),
        migrations.AddField(
            model_name='saved_searches',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Users'),
        ),
        migrations.AddField(
            model_name='locations',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Users'),
        ),
        migrations.AddField(
            model_name='favourites',
            name='favourite_loc_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Locations'),
        ),
        migrations.AddField(
            model_name='favourites',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Users'),
        ),
    ]