

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_item_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='goods_photos/no-photo.png', upload_to='goods_photos'),
        ),
    ]
