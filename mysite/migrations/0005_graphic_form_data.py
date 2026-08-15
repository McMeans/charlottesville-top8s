from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_graphic_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphic',
            name='form_data',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
