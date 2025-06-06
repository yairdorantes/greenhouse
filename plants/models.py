from django.db import models
import os


class Plants(models.Model):
    name = models.CharField(verbose_name="Plant's name", max_length=200)
    last_water = models.DateTimeField()
    next_water = models.DateField()
    image = models.ImageField(upload_to="plant's_image/", null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check if the image is being replaced
        if self.pk:
            old = Plants.objects.get(pk=self.pk)
            if old.image and old.image != self.image:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image file when the model is deleted
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)


class PlantImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="plant_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Plant Image"
        verbose_name_plural = "Plant Images"

    def __str__(self):
        formatted_date = self.created_at.strftime("%b %d, %Y at %H:%M")
        return f"{self.title} - {self.plant.name} - {formatted_date}"

    def save(self, *args, **kwargs):
        # Check if the image is being replaced
        if self.pk:
            old = PlantImage.objects.get(pk=self.pk)
            if old.image and old.image != self.image:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image file when the model is deleted
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)


# addind a test comemnt here
