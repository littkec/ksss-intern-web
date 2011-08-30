# -*- coding: utf-8 -*-

from django.db import models


# class för att fordefiniera vissa typiska skador
class Damage(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

# class för segelbåtar

LOCATIONS = (
    (u'Långholmen', 'Långholmen'),
    (u'Lökholmen', 'Lökholmen'),
    (u'Klockis', 'Klockis'),
    (u'Saltis', 'Saltis'),
    (u'Djursholm', 'Djursholm'),
    (u'Annan plats', 'Annan plats'),
    )

BOAT_TYPES = (
    (u'Motorbåt', 'Motorbåt'),
    (u'If', 'If'),
    (u'Optimist', 'Optimist'),
    (u'Två-Krona', 'Två-Krona'),
    )

MOTORS = (
    (u'Yamaha', 'Yamaha'),
    (u'Honda', 'Honda'),
    )

class Boat(models.Model):
    boat_type = models.CharField(choices=BOAT_TYPES, max_length=20)
    name = models.CharField(max_length=30)
    motor = models.CharField(choices=MOTORS, max_length=30, blank=True)
    motor_hp = models.CharField(max_length=3, blank=True)
    bought = models.CharField(max_length=4, blank=True)
    service = models.CharField(max_length=4, blank=True)
    location = models.CharField(choices=LOCATIONS, max_length=20)
    def __unicode__(self):
        return self.name

class ReportedDamage(models.Model):
    boat = models.ForeignKey(Boat)
    damage = models.ForeignKey(Damage)
    description = models.TextField()
    
    def __unicode__(self):
        return u'%s - %s' % (self.damage, self.description)
