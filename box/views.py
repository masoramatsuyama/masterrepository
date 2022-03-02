from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from box.models import *

class TopView(TemplateView):
  template_name = "top.html"

class ArtistlistView(TemplateView):
  template_name = "artistlist.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    artist_list = Artist.objects.all()
    context["artist_list"] = artist_list
    return context

class ArtistDetailView(DetailView):
  model= Artist
  template_name = 'artistdetail.html'

class BuyView(DetailView):
  model= Artist
  template_name = "buy.html"

class ThankyouView(TemplateView):
  template_name = "thankyou.html"