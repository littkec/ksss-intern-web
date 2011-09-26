# -*- coding: utf-8 -*-

from django.db import models


class Damage(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

class Camp(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40, blank=True)

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
    current_port = models.ForeignKey(Camp, related_name="current_port")
    home_port = models.ForeignKey(Camp, related_name="home_port")
    notes = models.TextField(blank=True)
    def __unicode__(self):
        return self.name

class ReportedDamage(models.Model):
    boat = models.ForeignKey(Boat)
    damage = models.ForeignKey(Damage)
    description = models.TextField()
    actions_taken = models.TextField(blank=True)
    actions_needed = models.TextField(blank=True)
    repaired = models.BooleanField()
    def __unicode__(self):
        return u'%s - %s' % (self.damage, self.description)

class News(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    posted = models.DateField()
    author = models.CharField(max_length=30)
    camp = models.ForeignKey(Camp)

    def __unicode__(self):
        return self.title

class InventoryType(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=30)
    camp = models.ForeignKey(Camp)

    def __unicode__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(InventoryType)
    amount = models.IntegerField(blank=True, null=True)
    current_amount = models.IntegerField(blank=True, null=True)
    buy_date = models.DateField(blank=True, null=True)
    seller = models.CharField(max_length=30, blank=True)
    bought_by = models.CharField(max_length=30, blank=True)
    guarantee = models.CharField(max_length=30, blank=True)
    manual = models.CharField(max_length=30, blank=True)
    camp = models.ForeignKey(Camp)
    storage_place = models.ForeignKey(Building, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
