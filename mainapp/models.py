from django.db import models


class AgentName(models.Model):
    """
    Creates a Table "agentname" that contains the following data
    """
    name_id = models.IntegerField(primary_key=True, null=False)
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, default="")
    phone = models.CharField(max_length=13, null=False)
    pollingunit_uniqueid = models.IntegerField(null=False, unique=True)

    class Meta:
        db_table = "agentname"


class AnnouncedPollingUnit(models.Model):
    """
    Creates a Table "announced_pu_results" that contains the following data
    """
    result_id = models.IntegerField(null=False, primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50, null=False, unique=True)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateField(null=False)
    user_ip_address = models.GenericIPAddressField(max_length=50)

    class Meta:
        db_table = "announced_pu_results"


class AnnouncedStateResults(models.Model):
    """
    Creates a table "announced_state_results that contains the following data
    """
    result_id = models.IntegerField(primary_key=True, null=False)
    state_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateField(null=False)
    user_ip_address = models.GenericIPAddressField(max_length=50)

    class Meta:
        db_table = "announced_state_results"


class AnnouncedWardResults(models.Model):
    """
    Creates a table "announced_ward_results" that contains the following data
    """
    result_id = models.IntegerField(null=False, primary_key=True)
    ward_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateField(null=False)
    user_ip_address = models.GenericIPAddressField(max_length=50)

    class Meta:
        db_table = "announced_ward_results"


class Lga(models.Model):
    """
    Creates a table "lga" that contains the following data
    """
    uniqueid = models.IntegerField(primary_key=True, unique=True, null=False)
    lga_id = models.IntegerField(null=False)
    lga_name = models.CharField(max_length=50, null=False)
    state_id = models.IntegerField(null=False)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateField(null=False, auto_now_add=True)
    user_ip_address = models.GenericIPAddressField(max_length=50, null=False)

    class Meta:
        db_table = "lga"


class Party(models.Model):
    """
    Creates a table "party" with the following data
    """
    id = models.IntegerField(null=False, primary_key=True)
    partyid = models.CharField(max_length=11, null=False)
    partyname = models.CharField(max_length=11, null=False)

    class Meta:
        db_table = "party"


class PollingUnit(models.Model):
    """
    Creates a table "polling_unit" with the following data
    """
    uniqueid = models.IntegerField(null=False, primary_key=True)
    polling_unit_id = models.IntegerField(null=False)
    ward_id = models.IntegerField(null=False)
    lga_id = models.IntegerField(null=False)
    uniquewardid = models.IntegerField(default="")
    polling_unit_number = models.CharField(max_length=50, default="")
    polling_unit_name = models.CharField(max_length=50, default="")
    polling_unit_description = models.TextField()
    lat = models.CharField(default="", max_length=50)
    long = models.CharField(default="", max_length=50)
    entered_by_user = models.CharField(max_length=50, default="")
    date_entered = models.DateField(default="")
    user_ip_address = models.GenericIPAddressField(default="", max_length=50)

    class Meta:
        db_table = "polling_unit"


class States(models.Model):
    """
    Creates a table "states" with the following data
    """
    state_id = models.IntegerField(primary_key=True, null=False)
    state_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = "states"


class Wards(models.Model):
    """
    Creates a table "ward" with the following data
    """
    unique_id = models.IntegerField(null=False, primary_key=True)
    ward_id = models.IntegerField(null=False)
    ward_name = models.CharField(max_length=50, null=False)
    lga_id = models.IntegerField(null=False)
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateField(null=False)
    user_ip_address = models.GenericIPAddressField(max_length=50, null=False)

    class Meta:
        db_table = "ward"


class AnnouncedLgaResults(models.Model):
    """
    Creates a table "announced_lga_results" with the following data
    """
    result_id = models.IntegerField(null=False, primary_key=True)
    lga_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateField(null=False)
    user_ip_address = models.GenericIPAddressField(max_length=50, null=False)

    class Meta:
        db_table = "announced_lga_results"
