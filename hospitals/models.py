from django.db import models


class AirwaysTypes(models.TextChoices):
    VM = "VM", "Ventilação Mecânica"
    AA = "AA", "Ar Ambiente"
    VNI = "VNI", "Ventilação não Invasiva"


class StatusTypes(models.TextChoices):
    S = "S", "Suspeito"
    C = "C", "Confirmado"
    D = "D", "Descartado"


class DepartureTypes(models.TextChoices):
    A = "A", "Alta"
    O = "O", "Óbito"


class Hospital(models.Model):
    name = models.CharField("Nome", blank=False, max_length=254)
    city = models.CharField("Cidade", blank=False, max_length=254)
    phonenumber = models.CharField("Telefone", blank=False, max_length=16)
    email = models.EmailField("E-mail", blank=False, max_length=254)


class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, verbose_name="Hospital", on_delete=models.CASCADE)

    name = models.CharField("Nome", blank=False, max_length=254)
    birthday = models.DateField("Data de Nascimento", auto_now=False, auto_now_add=False)
    airways = models.CharField("Vias Aéreas", blank=False, choices=AirwaysTypes.choices, default=AirwaysTypes.AA, max_length=24)
    status = models.CharField("Status COVID", blank=False, choices=StatusTypes.choices, default=StatusTypes.S, max_length=10)

    hospitalization_date = models.DateField("Data de Internação", blank=False, auto_now=False, auto_now_add=False)
    departure_date = models.DateField("Data de Saída", blank=False, auto_now=False, auto_now_add=False)

    cns = models.CharField("Carteira Nacional do SUS", blank=True, default="", max_length=30)
    sisreg = models.CharField("Número no sistema Sisreg", blank=True, default="", max_length=30)
    departure_reason = models.CharField("Motivo da Saída", blank=True, choices=DepartureTypes.choices, default=DepartureTypes.A, max_length=5)
