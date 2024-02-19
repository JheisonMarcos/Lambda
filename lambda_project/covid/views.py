from django.shortcuts import render

from covid.models import *


# Create your views here.
def get_data_list(data):
    proteins_list = (
        data.select_related()
        .values_list("id_pdb__nm_protein", flat=True)
        .distinct("id_pdb__nm_protein")
    )
    pdb_list = (
        data.select_related()
        .values_list("id_pdb__id_pdb", flat=True)
        .distinct("id_pdb__id_pdb")
    )
    farmacos_list = (
        data.select_related()
        .values_list("nm_farmaco", flat=True)
        .distinct("nm_farmaco")
    )
    return {
        "proteins_list": proteins_list,
        "pdb_list": pdb_list,
        "farmacos_list": farmacos_list,
    }


def covidListPageView(request):
    # template_name = 'covid_list.html'

    context = {}
    data = VsRaw.objects.exclude(nm_farmaco="profluis")

    context.update(get_data_list(data))

    # TODO ta feio isso
    if request.method == "POST":
        protein = request.POST.get("protein")
        pdb = request.POST.get("pdb")
        farmaco = request.POST.get("farmaco")
    else:
        protein = request.GET.get("protein")
        pdb = request.GET.get("pdb")
        farmaco = request.GET.get("farmaco")

    if protein:
        context["protein"] = protein
        data = data.select_related().filter(id_pdb__nm_protein=protein)
    if pdb:
        context["pdb"] = pdb
        data = data.select_related().filter(id_pdb=pdb)
    if farmaco:
        context["farmaco"] = farmaco
        data = data.select_related().filter(nm_farmaco=farmaco)

    if protein or pdb or farmaco:
        context["complexes"] = data

    return render(request, "covid_list.html", context)


def filter_plip_tables(id_pdb, id_pocket, nm_farmaco, nm_analogo):
    """docstring for plip_tables_get"""
    table_list = [
        PlipSalt,
        PlipMetal,
        PlipWater,
        PlipHalogen,
        PlipHydrogen,
        PlipHydrophobic,
        PlipPistacking,
        PlipPication,
    ]
    interactions = {
        table._meta.model_name: table.objects.exclude(
            nm_farmaco="profluis", id_pdb="7K3G"
        ).filter(
            id_pdb=id_pdb,
            id_pocket=id_pocket,
            nm_farmaco=nm_farmaco,
            nm_analogo=nm_analogo,
        )
        for table in table_list
    }
    fields = {
        f"{table._meta.model_name}_fields": table._meta.get_fields
        for table in table_list
    }

    return interactions, fields


def covidDetailsPageView(request):
    context = {}

    if request.method == "GET":
        id_pdb = request.GET.get("id_pdb")
        id_pocket = request.GET.get("id_pocket")
        nm_farmaco = request.GET.get("nm_farmaco")
        nm_analogo = request.GET.get("nm_analogo")

        context["id_pdb"] = id_pdb
        context["id_pocket"] = id_pocket
        context["nm_farmaco"] = nm_farmaco
        context["nm_analogo"] = nm_analogo

        for x in filter_plip_tables(id_pdb, id_pocket, nm_farmaco, nm_analogo):
            context.update(x)

    return render(request, "covid_details.html", context)
