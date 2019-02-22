from django.db import models
from django.contrib.auth.models import User


def ToLowerCase(name):
    return name.lower()

class Smartphone(models.Model):
    name = models.CharField(max_length=100, validators=[ToLowerCase,])
    image = models.ImageField(blank='False', upload_to='media')
    performance_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    design_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    camera_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    sound_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    features_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    no_of_users = models.IntegerField(default=0)
    commented = models.IntegerField(default=0)
    written = models.IntegerField(default=0)
    total_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    recommend = models.IntegerField(default=0)
    not_recommend = models.IntegerField(default=0)
    overpriced = models.IntegerField(default=0)
    issues_with_the_product = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)
    smooth = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Rated(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Smartphone, on_delete=models.CASCADE)
    # user_rating = models.PositiveSmallIntegerField(default=0, blank=False)
    performance_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    design_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    camera_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    sound_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    features_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    total_ratings = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    recommend = models.IntegerField(default=0)
    not_recommend = models.IntegerField(default=0)
    overpriced = models.IntegerField(default=0)
    issues_with_the_product = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)
    smooth = models.IntegerField(default=0)
    has_commented = models.BooleanField(default=False)
    about = models.TextField(max_length=500, blank=True)
    has_written = models.BooleanField(default=False)
    comment_like = models.IntegerField(default=0)
    comment_dislike = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) + ',' + str(self.product)
