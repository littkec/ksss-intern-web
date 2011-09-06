# -*- coding: utf-8 -*-

from django.db import models


class Damage(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Locations(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class BoatTypes(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Motors(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Boat(models.Model):
    name = models.CharField(max_length=30)
    boat_type = models.ForeignKey(BoatTypes)
    motor = models.ForeignKey(Motors)
    motor_hp = models.CharField(max_length=3, blank=True)
    bought = models.CharField(max_length=4, blank=True)
    service = models.CharField(max_length=4, blank=True)
    current_location = models.ForeignKey(Locations, related_name="current_location")
    home_port = models.ForeignKey(Locations, related_name="home_port")
    notes = models.TextField(blank=True)
    def __unicode__(self):
        return self.name

class ReportedDamage(models.Model):
    boat = models.ForeignKey(Boat)
    damage = models.ForeignKey(Damage)
    description = models.TextField()
    actions_taken = models.TextField(blank=True)
    actions_needed = models.TextField(blank=True)
    def __unicode__(self):
        return u'%s - %s' % (self.damage, self.description)

class News(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    posted = models.DateField()
    author = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title
