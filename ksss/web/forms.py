# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from ksss.web.models import *

class AddDamage(ModelForm):
    class Meta:
        model = ReportedDamage

class AddBoat(ModelForm):
    class Meta:
        model = Boat

class EditBoat(ModelForm):
    class Meta:
        model = Boat

class News(ModelForm):
    class Meta:
        model = News

class Building(ModelForm):
    class Meta:
        model = Building

class Inventory(ModelForm):
    class Meta:
        model = Inventory
