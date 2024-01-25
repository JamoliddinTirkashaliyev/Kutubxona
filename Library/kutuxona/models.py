from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kitoblar_soni = models.PositiveSmallIntegerField(default=0)
    kurs = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism = models.CharField(max_length=50)
    jins = models.CharField(max_length=10)
    tugilgan_sana = models.DateField(null=True, blank=True)
    tirik = models.BooleanField()
    kitoblar_soni = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.CharField(max_length=30)
    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField(null=True, blank=True)
    qaytardi = models.BooleanField(default=False)