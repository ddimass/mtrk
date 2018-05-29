from django.db import models



# Create your models here.

class Lm(models.Model):
  lm_types = (
    (0, 'Regresions'),
    (1, 'Classification'),
  )

  lm_libs = (
    (0, 'Scikit-learn'),
    (1, 'Tensorflow'),
    (2, 'Keras'),
  )
  name = models.CharField(max_length=200)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.FileField(upload_to='uploads/%Y/%m/%d/')
  lm_type = models.IntegerField(choices=lm_types)
  lm_lib = models.IntegerField(choices=lm_libs)
  def __str__(self):
    return self.name

