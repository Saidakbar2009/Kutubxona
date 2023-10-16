from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.PositiveSmallIntegerField()
    kitoblar_soni = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=10, choices=(("Erkak", "Erkak"), ("Ayol", "Ayol")))
    kitoblar_soni = models.PositiveSmallIntegerField()
    tugilgan_yil = models.DateField(blank=True, null=True)
    tirik = models.BooleanField(default=False)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
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
    olingan_sana = models.DateField(auto_now_add=True)
    qaytarish_sana = models.DateField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)
    def str(self):
        return f"{self.talaba.ism} - {self.kitob.nom}ni {self.olingan_sana}da oldi."
