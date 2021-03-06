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


class BedTypes(models.TextChoices):
    UTIA = "UTIA", "UTI Adulto"
    UTIP = "UTIP", "UTI Pediátrica"
    UTIN = "UTIN", "UTI Neonatal"
    CA = "CA", "Clínico Adulto"
    CP = "CP", "Clínico Pediátrico"
    CN = "CN", "Clínico Neonatal"
    VM = "VM", "Leito Símples com Ventilador Mecânico"


class Hospital(models.Model):
    name = models.CharField("Nome", blank=False, max_length=254)
    city = models.CharField("Cidade", blank=False, max_length=254)
    phonenumber = models.CharField("Telefone", blank=False, max_length=16)
    email = models.EmailField("E-mail", blank=False, max_length=254)


class HospitalBed(models.Model):
    hospital = models.ForeignKey(Hospital, verbose_name="Hospital", on_delete=models.CASCADE)
    beds = models.CharField("Tipo do Leito", blank=False, choices=BedTypes.choices, default=BedTypes.UTIA, max_length=38)


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


class PatientBed(models.Model):
    patient = models.ForeignKey(Patient, verbose_name="Paciente", on_delete=models.CASCADE)
    bed = models.CharField("Tipo do Leito", blank=False, choices=BedTypes.choices, default=BedTypes.UTIA, max_length=38)
    admission_date = models.DateField("Data de Admissão neste Leito", blank=False, auto_now=False, auto_now_add=False)
    waiting_uti = models.BooleanField("Aguardando UTI", blank=False, default=False)


class Report(models.Model):
    hospital = models.ForeignKey(Hospital, verbose_name="Hospital", on_delete=models.CASCADE)

    report_date = models.DateTimeField("Data do Relatório", blank=False, auto_now=False, auto_now_add=True)
    informant_name = models.CharField("Nome do Informante", blank=False, max_length=256)
    informant_function = models.CharField("Função do Informante", blank=False, max_length=256)


class Occupation(models.Model):
    report = models.ForeignKey(Report, verbose_name="Relatório", on_delete=models.CASCADE)

    beds = models.CharField("Tipo do Leito", blank=False, choices=BedTypes.choices, default=BedTypes.UTIA, max_length=38)
    total = models.IntegerField("Quantidade total de leitos", blank=False, default=0)
    total_covid = models.IntegerField("Quantidade de leitos para Covid-19", blank=False, default=0)
    occupation = models.IntegerField("Quantidade de leitos ocupados", blank=False, default=0)
    occupation_covid = models.IntegerField("Quantidade de leitos ocupados por Covid-19", blank=False, default=0)
    total_waiting_uti = models.IntegerField("Aguardando UTI", blank=False, default=0)
