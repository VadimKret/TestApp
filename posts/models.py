import datetime
import os
from django.db import models
from django.core.validators import FileExtensionValidator 

# Create your models here.


class Posts(models.Model):
      def get_file_path(self, filename):
            ext = filename.split('.')[-1]
            filename = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.{ext}'
            return os.path.join('telegram/images/', filename)

      title = models.CharField(max_length=255)
      description = models.TextField()
      image = models.ImageField(    
            upload_to = get_file_path,
            validators = [FileExtensionValidator(
                  null = True,
                  blank = True,
                  allowed_extensions = ['jpg', 'jpeg', 'png', 'webp']
                  )],
            verbose_name = "Изображение"
      )
      created = models.DateField(
            auto_now_add = True,
            verbose_name = "Дата создания"
      )
      last_modifaed = models.DateField(
            auto_now = True,
            verbose_name = "Последнее обновление"
      )
      active = models.BooleanField(
            verbose_name = "Активна",
            default = True
      )