from django.shortcuts import render

from covid.models import VsRaw


# Create your views here.
def get_data_list(data):
    proteins_list = data.values("id_pdb__nm_protein").distinct("id_pdb__nm_protein")
    farmacos_list = data.values("nm_farmaco").distinct("nm_farmaco")
    return {
        "proteins_list": proteins_list,
        "farmacos_list": farmacos_list,
    }


def covidListPageView(request):
    # template_name = 'covid_list.html'

    context = {}
    data = VsRaw.objects.exclude(nm_farmaco="profluis", id_pdb="7K3G")

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

    context["protein"] = protein
    context["pdb"] = pdb
    context["farmaco"] = farmaco
    if protein:
        data.filter(id_pdb__nm_protein=protein)
    if pdb:
        data.filter(id_pdb=pdb)
    if farmaco:
        data.filter(nm_farmaco=farmaco)

    if protein or pdb or farmaco:
        context["complexes"] = data

    return render(request, "covid_list.html", context)


def covidDetailsPageView(request):
    context = {}
    return render(request, "covid_details.html", context)
