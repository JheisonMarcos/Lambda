# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admetmesh(models.Model):
    smiles = models.CharField(blank=True, null=True)
    logs = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    logd = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    logp = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pgp_inh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pgp_sub = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    hia = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    f_20 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    f_30 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    caco_2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    mdck = models.CharField(max_length=30, blank=True, null=True)
    bbb = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ppb = models.FloatField(blank=True, null=True)
    vdss = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fu = models.FloatField(blank=True, null=True)
    cyp1a2_inh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp1a2_sub = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp2c19_inh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp2c19_sub = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp2c9_inh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp2c9_sub = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp2d6_inh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp2d6_sub = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp3a4_inh = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cyp3a4_sub = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    cl = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    t12 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    herg = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    h_ht = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    dili = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ames = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    roa = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fdamdd = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    skinsen = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    carcinogenicity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ec = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ei = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    respiratory = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    bcf = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    igc50 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    lc50 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    lc50dm = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nr_ar = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nr_ar_lbd = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nr_ahr = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nr_aromatase = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nr_er = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nr_er_lbd = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nr_ppar_gamma = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    sr_are = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    sr_atad5 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    sr_hse = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    sr_mmp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sr_p53 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    mw = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    vol = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    dense = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nha = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nhd = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    tpsa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nrot = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nring = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    maxring = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nhet = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fchar = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nrig = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    flex = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nstereo = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    toxicophores = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    acute_aquatic_toxicity = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ld50_oral = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nongenotoxic_carcinogenicity = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    skin_sensitization = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    surechembl = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    genotoxic_carcinogenicity_mutagenicity = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    nonbiodegradable = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    qed = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    synth = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fsp3 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    mce_18 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    natural_product_likeness = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    alarm_nmr = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    bms = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    chelating = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pains = models.IntegerField(blank=True, null=True)
    lipinski = models.CharField(max_length=8, blank=True, null=True)
    pfizer = models.CharField(max_length=8, blank=True, null=True)
    gsk = models.CharField(max_length=8, blank=True, null=True)
    goldentriangle = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admetmesh'
        db_table_comment = ' find . -maxdepth 2 -iname "*admetmesh*" -exec cat {} \\; | tr -s \',;\' \'\\t\' | tr -d \'\\r%\' | grep -v \'smiles\' > /tmp/admetmesh.tsv\n\n psql -h 127.0.0.1 -d vs -U efolador\n\n'


class ClasseFarmaco(models.Model):
    nm_protein = models.CharField(max_length=30, blank=True, null=True)
    vl_score = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classe_farmaco'


class Fpocket(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=30, blank=True, null=True)
    drug_score = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    volume = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    nb_asph = models.IntegerField(blank=True, null=True)
    inter_chain = models.IntegerField(blank=True, null=True)
    apol_asph_proportion = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    mean_asph_radius = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    as_density = models.CharField(max_length=10, blank=True, null=True)
    mean_asph_solv_acc = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    mean_loc_hyd_dens = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    flexnumeric = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    hydrophobicity_score = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    volume_score = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    charge_score = models.IntegerField(blank=True, null=True)
    polarity_score = models.IntegerField(blank=True, null=True)
    a0_apol = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    a0_pol = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    af_apol = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    af_pol = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    n_abpa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fpocket'
        db_table_comment = 'find . -maxdepth 2 -iname "fpoqcket.tsv" -exec cat {} \\; > /tmp/fpoqcket.tsv\n\npsql -h 127.0.0.1 -d vs -U efolador\ndelete from covid19.fpocket;\n\\copy covid19.fpocket from \'/tmp/fpoqcket.tsv\' with CSV DELIMITER E\'\\t\';\n'


class PlipHalogen(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
    don_angle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acc_angle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    don_idx = models.IntegerField(blank=True, null=True)
    donortype = models.CharField(max_length=5, blank=True, null=True)
    acc_idx = models.IntegerField(blank=True, null=True)
    acceptortype = models.CharField(max_length=5, blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'plip_halogen'
        db_table_comment = 'find . -maxdepth 2 -iname "HalogenBonds.csv" -exec cat {} \\;  > /tmp/HalogenBonds.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_halogen;\n\\copy covid19.plip_halogen from \'/tmp/HalogenBonds.csv\' with CSV DELIMITER E\'\\t\';'


class PlipHydrogen(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
    dist_ha = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dist_da = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    don_angle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
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
        db_table = 'plip_hydrogen'
        db_table_comment = 'find . -maxdepth 2 -iname "HydrogenBonds.csv" -exec cat {} \\;  > /tmp/HydrogenBonds.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_hydrogen;\n\\copy covid19.plip_hydrogen from \'/tmp/HydrogenBonds.csv\' with CSV DELIMITER E\'\\t\';'


class PlipHydrophobic(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
        db_table = 'plip_hydrophobic'
        db_table_comment = 'find . -maxdepth 2 -iname "HydrophobicInteractions.csv" -exec cat {} \\;  > /tmp/HydrophobicInteractions.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_hydrophobic;\n\\copy covid19.plip_hydrophobic from \'/tmp/HydrophobicInteractions.csv\' with CSV DELIMITER E\'\\t\';'


class PlipMetal(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
        db_table = 'plip_metal'


class PlipPication(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
    voffset = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    protcharged = models.BooleanField(blank=True, null=True)
    lig_group = models.CharField(max_length=30, blank=True, null=True)
    lig_idx_list = models.CharField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'plip_pication'
        db_table_comment = 'find . -maxdepth 2 -iname "pi-CationInteractions.csv" -exec cat {} \\;  > /tmp/pi-CationInteractions.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_pication;\n\\copy covid19.plip_pication from \'/tmp/pi-CationInteractions.csv\' with CSV DELIMITER E\'\\t\';'


class PlipPistacking(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
    centdist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    angle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    voffset = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vtype = models.CharField(max_length=1, blank=True, null=True)
    lig_idx_list = models.CharField(blank=True, null=True)
    ligcoo = models.CharField(max_length=50, blank=True, null=True)
    protcoo = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'plip_pistacking'
        db_table_comment = 'find . -maxdepth 2 -iname "pi-Stacking.csv" -exec cat {} \\;  > /tmp/pi-Stacking.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_pistacking;\n\\copy covid19.plip_pistacking from \'/tmp/pi-Stacking.csv\' with CSV DELIMITER E\'\\t\';'


class PlipSalt(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
        db_table = 'plip_salt'
        db_table_comment = 'find . -maxdepth 2 -iname "SaltBridges.csv" -exec cat {} \\;  > /tmp/SaltBridges.csv\npsql -h 192.168.0.1 -d vs -U efolador\ndelete from covid19.plip_salt;\n\\copy covid19.plip_salt from \'/tmp/SaltBridges.csv\' with CSV DELIMITER E\'\\t\';'


class PlipWater(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
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
        db_table = 'plip_water'


class ProteinClasses(models.Model):
    ds_protein = models.CharField(max_length=70, blank=True, null=True)
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
    nm_protein = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protein_classes'


class Proteins(models.Model):
    id_pdb = models.CharField(primary_key=True, max_length=4)
    nm_protein = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proteins'
        db_table_comment = 'CREATE TABLE proteins AS (SELECT DISTINCT id_pdb, nm_protein from protein_classes)'


class Smiles(models.Model):
    nm_analogo = models.CharField(max_length=30)
    ds_smiles = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smiles'
        db_table_comment = 'Gerar arquivo:\n- find . -maxdepth 3 -iname "*pubchem.txt" -exec cat {} \\;  >> /tmp/smiles.txt\n- find . -maxdepth 3 -iname "*zinc.txt" -exec cat {} \\;  | grep \'^ZINC\' > /tmp/smiles.txt\n\nCarregar no SGBD:\n- psql -h 192.168.0.1 -d vs -U efolador \n\n'


class VsRaw(models.Model):
    id_pdb = models.CharField(primary_key=True, max_length=4)  # The composite primary key (id_pdb, id_pocket, nm_farmaco, nm_analogo) found, that is not supported. The first column is selected.
    id_pocket = models.CharField(max_length=10)
    nm_farmaco = models.CharField(max_length=30)
    nm_analogo = models.CharField(max_length=60)
    vl_score = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vs_raw'
        unique_together = (('id_pdb', 'id_pocket', 'nm_farmaco', 'nm_analogo'),)
        db_table_comment = 'cd /data/covid19/executados\n\nfind . -maxdepth 2 -iname "*.tab" -exec cat {} \\; > /tmp/vs_tab_docking.tab\n\npsql -d vs -U efolador\n      vs=# \\copy covid19.vs_raw from \'./mdl28170.tsv\' with CSV DELIMITER E\'\\t\';  \n\npsql -d vs -c "copy covid19.vs_raw from \'/tmp/vs_tab_docking.tab\' with CSV DELIMITER E\'\\t\'"\nCOPY 1997759\n\npsql -h 127.0.0.1 -d vs -U efolador -c "copy covid19.vs_raw from \'/tmp/luis.tab\' with CSV DELIMITER E\'\\t\'"\nCOPY 110695\n\n psql -d vs -c "copy covid19.vs_raw from \'/tmp/cloroquina.tsv\' with CSV DELIMITER E\'\\t\'"\nCOPY 1.039.350\n'


class WekaOut(models.Model):
    id_pdb = models.CharField(max_length=4, blank=True, null=True)
    id_pocket = models.CharField(max_length=10, blank=True, null=True)
    nm_farmaco = models.CharField(max_length=30, blank=True, null=True)
    nm_analogo = models.CharField(max_length=60, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)
    predicted = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    error = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weka_out'
        db_table_comment = "-- Grave o output do Weke em formato .CSV\nweka_prediction.csv\n\n-- Gerar o arquivo de output weka para importar no SGBD\npaste weka.csv weka_prediction.csv | tr ',' '\\t' | cut -f 1-4,32,34-36 | head -n -1 > weka_out.tsv\n\n-- Importar no SGBD\npsql -h 192.168.0.1 -d vs -U efolador\n\\copy covid19.weka_out from './weka_out.tsv' with CSV HEADER DELIMITER E'\\t'  \n\n"
