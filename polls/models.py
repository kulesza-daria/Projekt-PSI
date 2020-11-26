from datetime import date
from django.db import models


class Zolnierz(models.Model):
    id_zolnierza = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    data_urodzenia = models.DateField()
    telefon = models.CharField(max_length=15)
    specjalnosc = models.CharField(max_length=90)
    stanowisko_etatowe = models.CharField(max_length=90)
    zameldowanie = models.TextField(null=False)


class Kontrakty(models.Model):
    id_kontraktu = models.AutoField(primary_key=True)
    zolnierz = models.OneToOneField(Zolnierz, on_delete=models.CASCADE)
    poczatek_kontraktu = models.DateField(default=date.today, null=False)
    koniec_kontraktu = models.DateField(null=False)
    wynagrodzenie = models.DecimalField(max_digits=9, decimal_places=2, default=3200)


class Ekwipunek(models.Model):
    id_ekwipunku = models.AutoField(primary_key=True)
    zolnierz = models.ManyToOneRel(Zolnierz, on_delete=models.CASCADE)
    umundurowanie = models.CharField(choices=['odzież ochronna', 'zasobnik', 'manierka', 'menażka', 'przybory do czyszczenia', 'przybory toaletowe'])
    uzbrojenie = models.CharField(choices=['broń krótka', 'broń długa', 'broń biała'])
    oporzadzenie_uzbrojenia = models.CharField(choices=['kamizelki kuloodporne', 'maski przeciwgazowe', 'hełmy', 'futerał do broni', 'ładownice'])


class Przepustki(models.Model):
    zolnierz = models.ForeignKey(Zolnierz, on_delete=models.CASCADE)
    poczatek_przepustki = models.DateField()
    koniec_przepustki = models.DateField()


class Wnioski(models.Model):
    id_wniosku = models.AutoField(primary_key=True)
    zolnierz = models.ManyToOneRel(Zolnierz, on_delete=models.CASCADE)
    rodzaj_wniosku = models.CharField(choices=['urlopowy', 'mieszkaniowy'])
    status = models.CharField(choices=['przyjęty', 'odrzucony'])
    data_zlozenia = models.CharField(default=date.today, null=False)


class Wyjazdy_sluzbowe(models.Model):
    id_wyjazdu = models.AutoField(primary_key=True)
    zolnierz = models.ManyToManyField(Zolnierz)
    miejsce_docelowe = models.CharField(null=False)
    cel = models.CharField(choices=['misja', 'poligon'])
    data_wyjazdu = models.DateField()
    data_przyjazdu = models.DateField()
