from django.db import models


# مخطط بيانات للمكان التاريخي
from django.db.models import DO_NOTHING


class Place(models.Model):
    name = models.CharField(max_length=256)  # هذا الحقل يحفظ اسم المكان التاريخي
    description = models.TextField()  # هذا الحقل يحفظ تفاصيل المكان التاريخي
    country = models.CharField(max_length=256)  # هذا الحقل يحفظ الدولة للمكان التاريخي
    image = models.ImageField(upload_to='places_images/')  # هذا الحقل يحفظ رابط الصورة للمكان التاريخي

    def __str__(self):
        return self.name


# مخطط بيانات لتقييمات المكان التاريخي
class Rate(models.Model):
    rate = models.IntegerField(default=0)  # يستخدم هذا الحقل لحفظ التقييم
    review = models.CharField(max_length=300)  # يستخدم هذا الحقل لحفظ التعليقات
    place = models.ForeignKey('Place', on_delete=DO_NOTHING)  # هذا الحقل يقوم بربط المكان التاريخي بالتعليق

    def __str__(self):
        return '{} - {}'.format(self.place, self.rate)
