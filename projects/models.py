from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class Project(models.Model):
	title = models.CharField(max_length=100, verbose_name='Título')
	link = models.CharField(max_length=255, verbose_name='Link')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Proyecto"
		verbose_name_plural = "Proyectos"

	def __str__(self):
		return self.title

class Image(models.Model):
	title = models.CharField(max_length=100, verbose_name='Título', blank=True)
	image = models.ImageField(upload_to='images', verbose_name='Nombre_imagen')
	project_image = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name = "Imagen"
		verbose_name_plural = "Imágenes"

	def image_tag(self):
		if self.image:
			return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
		else:
			return 'No Image Found'
	image_tag.short_description = 'Image'