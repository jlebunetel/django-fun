#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the livre index.")

def node_detail(request, node_id):
    return HttpResponse("détail du noeud %s" % node_id)

def edge_detail(request, edge_id):
    return HttpResponse("détail de l'arc %s" % edge_id)
