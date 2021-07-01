from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.CharField(max_length=30, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, upload_to='images/')

    file_title = models.TextField(default='')
    file = models.FileField(null=True, upload_to='files/')

    def __str__(self):
        return self.title
