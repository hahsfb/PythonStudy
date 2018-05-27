from django.db import models


class Person(models.Model):
    people_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    sex = models.CharField()

    class Meta:
        db_table = 'reko_people'


class Video(models.Model):
    video_id = models.IntegerField(primary_key=True)
    people_id = models.ForeignKey(Person, related_name='people_id', on_delete=models.CASCADE)
    size = models.IntegerField()

    class Meta:
        db_table = 'reko_video'
        # order_with_respect_to = 'people_id'
