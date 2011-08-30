# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from ksss.web.models import ReportedDamage, Boat

class AddDamage(ModelForm):
    class Meta:
        model = ReportedDamage

class AddBoat(ModelForm):
    class Meta:
        model = Boat
