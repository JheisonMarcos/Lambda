# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Proteins(models.Model):
    id_pdb = models.CharField(primary_key=True, max_length=4)
    nm_protein = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "proteins"
        db_table_comment = "CREATE TABLE proteins AS (SELECT DISTINCT id_pdb, nm_protein from protein_classes)"


class VsRaw(models.Model):
    id_pdb = models.ForeignKey(
        Proteins, on_delete=models.DO_NOTHING, db_column="id_pdb"
    )
    nm_farmaco = models.CharField(max_length=30)
    id_pocket = models.CharField(max_length=10)
    nm_analogo = models.CharField(primary_key=True, max_length=60)
    vl_score = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "vs_raw"
        unique_together = (("id_pdb", "id_pocket", "nm_farmaco", "nm_analogo"),)
        db_table_comment = "cd /data/covid19/executados\n\nfind . -maxdepth 2 -iname \"*.tab\" -exec cat {} \\; > /tmp/vs_tab_docking.tab\n\npsql -d vs -U efolador\n      vs=# \\copy covid19.vs_raw from './mdl28170.tsv' with CSV DELIMITER E'\\t';  \n\npsql -d vs -c \"copy covid19.vs_raw from '/tmp/vs_tab_docking.tab' with CSV DELIMITER E'\\t'\"\nCOPY 1997759\n\npsql -h 127.0.0.1 -d vs -U efolador -c \"copy covid19.vs_raw from '/tmp/luis.tab' with CSV DELIMITER E'\\t'\"\nCOPY 110695\n\n psql -d vs -c \"copy covid19.vs_raw from '/tmp/cloroquina.tsv' with CSV DELIMITER E'\\t'\"\nCOPY 1.039.350\n"


class PlipHalogen(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    sidechain = models.BooleanField(blank=True, null=True)
    dist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    don_angle = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    acc_angle = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    don_idx = models.IntegerField(blank=True, null=True)
    donortype = models.CharField(max_length=5, blank=True, null=True)
    acc_idx = models.IntegerField(blank=True, null=True)
    acceptortype = models.CharField(max_length=5, blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_halogen"
        db_table_comment = "find . -maxdepth 2 -iname \"HalogenBonds.csv\" -exec cat {} \\;  > /tmp/HalogenBonds.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_halogen;\n\\copy covid19.plip_halogen from '/tmp/HalogenBonds.csv' with CSV DELIMITER E'\\t';"

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"


class PlipHydrogen(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    sidechain = models.BooleanField(blank=True, null=True)
    dist_ha = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    dist_da = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    don_angle = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    protisdon = models.BooleanField(blank=True, null=True)
    donoridx = models.IntegerField(blank=True, null=True)
    donortype = models.CharField(max_length=5, blank=True, null=True)
    acceptoridx = models.IntegerField(blank=True, null=True)
    acceptortype = models.CharField(max_length=5, blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_hydrogen"
        db_table_comment = "find . -maxdepth 2 -iname \"HydrogenBonds.csv\" -exec cat {} \\;  > /tmp/HydrogenBonds.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_hydrogen;\n\\copy covid19.plip_hydrogen from '/tmp/HydrogenBonds.csv' with CSV DELIMITER E'\\t';"

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"


class PlipHydrophobic(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    dist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ligcarbonidx = models.IntegerField(blank=True, null=True)
    protcarbonidx = models.IntegerField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_hydrophobic"
        db_table_comment = "find . -maxdepth 2 -iname \"HydrophobicInteractions.csv\" -exec cat {} \\;  > /tmp/HydrophobicInteractions.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_hydrophobic;\n\\copy covid19.plip_hydrophobic from '/tmp/HydrophobicInteractions.csv' with CSV DELIMITER E'\\t';"

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"


class PlipMetal(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    prot_idx_list = models.CharField(blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    dist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    protispos = models.BooleanField(blank=True, null=True)
    lig_group = models.CharField(max_length=20, blank=True, null=True)
    lig_idx_list = models.CharField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_metal"

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"


class PlipPication(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    prot_idx_list = models.CharField(max_length=50, blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    dist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    voffset = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    protcharged = models.BooleanField(blank=True, null=True)
    lig_group = models.CharField(max_length=30, blank=True, null=True)
    lig_idx_list = models.CharField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_pication"
        db_table_comment = "find . -maxdepth 2 -iname \"pi-CationInteractions.csv\" -exec cat {} \\;  > /tmp/pi-CationInteractions.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_pication;\n\\copy covid19.plip_pication from '/tmp/pi-CationInteractions.csv' with CSV DELIMITER E'\\t';"

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"


class PlipPistacking(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    prot_idx_list = models.CharField(blank=True, null=True)
    centdist = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    angle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    voffset = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    vtype = models.CharField(max_length=1, blank=True, null=True)
    lig_idx_list = models.CharField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_pistacking"
        db_table_comment = "find . -maxdepth 2 -iname \"pi-Stacking.csv\" -exec cat {} \\;  > /tmp/pi-Stacking.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_pistacking;\n\\copy covid19.plip_pistacking from '/tmp/pi-Stacking.csv' with CSV DELIMITER E'\\t';"

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"


class PlipSalt(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    prot_idx_list = models.CharField(blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    dist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    protispos = models.BooleanField(blank=True, null=True)
    lig_group = models.CharField(max_length=20, blank=True, null=True)
    lig_idx_list = models.CharField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_salt"
        # db_table_comment = 'find . -maxdepth 2 -iname "SaltBridges.csv" -exec cat {} \\;  > /tmp/SaltBridges.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_salt;\n\\copy covid19.plip_salt from \'/tmp/SaltBridges.csv\' with CSV DELIMITER E\'\\t\';'

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"


class PlipWater(models.Model):
    id_pdb = models.CharField(primary_key=True, blank=True, null=False)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    resnr = models.IntegerField(blank=True, null=True)
    restype = models.CharField(max_length=3, blank=True, null=True)
    reschain = models.CharField(max_length=1, blank=True, null=True)
    prot_idx_list = models.CharField(blank=True, null=True)
    resnr_lig = models.IntegerField(blank=True, null=True)
    restype_lig = models.CharField(max_length=3, blank=True, null=True)
    reschain_lig = models.CharField(max_length=3, blank=True, null=True)
    dist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    protispos = models.BooleanField(blank=True, null=True)
    lig_group = models.CharField(max_length=20, blank=True, null=True)
    lig_idx_list = models.CharField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = "plip_water"

    def __str__(self):
        return f"{self.id_pdb}-{self.id_pocket}"
