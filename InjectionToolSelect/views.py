from django.shortcuts import render
from InjectionTool import models
from django.http import JsonResponse

def updatesystem(request):
    if request.method=="POST":
        pass
    else:
        try:
            dnsnamelist=models.density_material.objects.all().values("material_type").distinct()
            print(dnsnamelist)
        except Exception:
            return render(request,"updatesystem.html",{"login_err":"loaddnsnamefail"})
        return render(request,"updatesystem.html",{"dnsnamelist":dnsnamelist})


def getipaddr(request):
    if request.method == 'GET':
        seldnsname=request.GET.get('seldnsname')
        if seldnsname:
            data = list(models.density_material.objects.filter(material_type=seldnsname).values("density_max"))
            print(data)
            return JsonResponse(data, safe=False)
