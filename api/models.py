from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=255, default='')
    health = models.IntegerField(blank=True, null=True) #cached

    next_step_updated_timestamp = models.DateTimeField(blank=True, null=True)

    is_closed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'Fish'
        verbose_name_plural = 'Fishes'
        app_label = "api"

class Event(models.Model):
    coc_location = models.CharField(max_length=255, default='')
    event_type = models.CharField(max_length=255, default='') #logged note, grabbed a bed, asked for help, was referred
    client_id = models.CharField(max_length=255, default='')
    details = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        app_label = "api"

class Client(models.Model):
    name = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=255, default='')
    ssn = models.CharField(max_length=255, default='')
    dob = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=255, default='')
    pregnant = models.BooleanField(default=False)
    race = models.CharField(max_length=255, default='')
    marital_status = models.CharField(max_length=255, default='')
    number_of_children = models.IntegerField(blank=True, null=True, default=0)
    veteran = models.BooleanField(default=False)
    occupation = models.CharField(max_length=255, default='')
    education = models.CharField(max_length=255, default='')
    sex_offender = models.BooleanField(default=False)


    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        app_label = "api"

class Coc(models.Model):
    name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    latitude = models.CharField(max_length=255, default='')
    longitude = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=255, default='')
    coc_type = models.CharField(max_length=255, default='')
    # requirements = models.CharField(max_length=255, default='') # female-only, pregnant, male-only


    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = 'Coc'
        verbose_name_plural = 'Cocs'
        app_label = "api"