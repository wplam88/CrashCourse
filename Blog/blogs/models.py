from django.db import models

# blog
class Blog(models.Model):
    """Reprsents an overall blog"""
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Returns a string representation of the model"""
        return self.name

# blog post
class BlogPost(models.Model):
    """Represents a blog post"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            """Returns a string representation of the model"""
            return self.name
