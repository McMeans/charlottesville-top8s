from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_graphic_form_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic',
            name='title',
            field=models.TextField(max_length=80),
        ),
    ]
