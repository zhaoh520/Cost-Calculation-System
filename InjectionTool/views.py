import pymysql
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from InjectionTool import models
from django.db.models import F,Q
from django.forms.models import model_to_dict
# def injectionTool(request):
#
#     return render(request, 'injectiontool.html')

# def injectionTool_db_get(request):
#     material_density_data = {}
#     db = pymysql.connect(host="127.0.0.1", user="root", port=3306, password="123456", database="cost_calculation_tool", charset='utf8')
#     cursor = db.cursor()
#     sql = 'select material_type, density_max from density_material'
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     print(list(results))
#     for i in list(results):
#         material_density_data[i[0]]=i[1]
#     print(material_density_data)
#     return render(request, "injectiontool.html", {'material_density_data': material_density_data})

claping_force_calc = 0
die_length = 0
die_width = 0

# 生成材料选择清单
def material_select(request):
    if request.method=="POST":
        pass
    else:
        try:
            material_name_list=models.density_material.objects.all().values("material_type").distinct()
            print(material_name_list)
        except Exception:
            return render(request,"injectiontool.html",{"material_list_err":"材料列表生成失败"})
        return render(request,"injectiontool.html",{"material_name_list":material_name_list})


# 获取选择材料的密度
def get_material_density(request):
    if request.method == 'GET':
        # select_material_type = 'PP-T30'
        select_material_type=request.GET.get('select_material_type')
        # select_material_type=HttpRequest.GET.get('select_material_type')
        print(select_material_type)
        if select_material_type:
            data_material_density = list(models.density_material.objects.filter(material_type=select_material_type).values("density_max"))
            print(data_material_density)
            return JsonResponse(data_material_density, safe=False)
        else:
            messages.error(request, '请选择材料')

# 计算零件的毛重
def gross_weight(request):
    if request.method == 'GET':
        product_net_weight = request.GET.get('product_net_weight')
        print(product_net_weight, type(product_net_weight))
        material_utilization_rate = \
            models.material_utilization_rate.objects\
                .filter(product_net_weight_min__lt=product_net_weight)\
                .filter(product_net_weight_max__gte=product_net_weight)\
                .values("material_utilization_rate")
        print(material_utilization_rate)
        if material_utilization_rate:
            for material_input_rate in material_utilization_rate:
                input_rate = material_input_rate['material_utilization_rate']
            product_gross_weight = int(float(product_net_weight) / float(input_rate))
            print(product_gross_weight)
            product_gross_weight_json = {"product_net_weight": product_gross_weight}
            return JsonResponse(product_gross_weight_json, safe=False)
        else:
            messages.error(request, '请输入正确的材料利用率')

# 计算模穴数量
def carve_count(request):
    if request.method == 'GET':
        part_length = request.GET.get('part_length')
        part_width = request.GET.get('part_width')
        part_projection_area = int(float(part_length) * float(part_width))
        number_die_caves = \
            models.NumberCaves.objects\
                .filter(projection_area_min__lt=part_projection_area)\
                .filter(projection_area_max__gte=part_projection_area)\
                .values("number_die_caves")
        print(number_die_caves)
        if number_die_caves:
            for cave in number_die_caves:
                number_caves = cave['number_die_caves']
                print(number_caves)
                number_die_caves_json = {"number_die_caves": number_caves}
                return JsonResponse(number_die_caves_json, safe=False)
        else:
            messages.error(request, '请输入正确的模穴数')




def recommend_machine_type(request):
    if request.method == 'GET':
        '''"part_length":$("#txtHP_PartLength").val(),
            "part_width":$("#txtHP_PartWidth").val(),
            "select_material_type":$("#txtHP_Material").val(),
            "select_material_density":$("#txtHP_Density").val(),
            "machine_injection_weight_min":$("#txtHP_MachineInjectionWeight").val(),
            "toggle_stroke":$("#txtHP_ToggleStroke").val(),
            "carve_count":$("txtHP_CarveCount").val(),
            "carve_row":$("txtHP_CarveRow").val(),
            "carve_column":$("txtHP_CarveColumn").val(),
        '''
        number_caves = request.GET.get('carve_count')
        # print(number_caves)
        product_length = request.GET.get('part_length')
        product_width = request.GET.get('part_width')
        material_selected = request.GET.get('select_material_type')
        density_selected = float(request.GET.get('select_material_density'))
        injection_weight = int(float(request.GET.get('machine_injection_weight_min')) * 1.09 / density_selected)
        toggle_distance = request.GET.get('toggle_stroke')
        carve_row_number = request.GET.get('carve_row')
        carve_column_number = request.GET.get('carve_column')
        pressure_selected_material = models.density_material.objects.filter(material_type=material_selected).values("pressure_in_mold")
        print(pressure_selected_material)
        # 根据零件短边尺寸来确定模具边距
        die_caves_distance = \
            models.die_edge_distance.objects\
                .filter(product_length_min__lt=product_width)\
                .filter(product_length_max__gte=product_width)\
                .values("die_edge_distance")

        # 计算锁模力
        if pressure_selected_material:
            for pressure_data in pressure_selected_material:
                pressure_selected = pressure_data['pressure_in_mold']
                print(pressure_selected)
                global claping_force_calc
                print(product_length, product_width, number_caves, pressure_selected)
                claping_force_calc = int(product_length) * int(product_width) * int(number_caves) * int(pressure_selected) / 10000
        # 计算模具尺寸
        if die_caves_distance:
            for distance_data in die_caves_distance:
                distance_selected = distance_data['die_edge_distance']
                global die_length, die_width
                print(product_length, product_width, carve_column_number, carve_row_number, distance_selected)
                die_length = int(product_width) * int(carve_column_number) + (int(carve_column_number)+1) * int(distance_selected)
                die_width = int(product_length) * int(carve_row_number) + (int(carve_row_number) + 1) * int(distance_selected)
        print(injection_weight, claping_force_calc, die_length, die_width, toggle_distance)
        clamping_force_recommend = \
            models.InjectionMachineInfo.objects\
                .filter(injection_weight_PS__gte=injection_weight)\
                .filter(clamping_force__gte=claping_force_calc) \
                .filter(space_between_tie_bars_x__gte=die_length) \
                .filter(space_between_tie_bars_y__gte=die_width) \
                .filter(toggle_stroke__gte=toggle_distance) \
                .values("clamping_force")
        print(clamping_force_recommend)
        if clamping_force_recommend:
            clamping_list = []
            for clamping_RF in clamping_force_recommend:
                clamping_cell = int(clamping_RF['clamping_force'])
                clamping_list.append(clamping_cell)
            print(clamping_list)
            clamping_force_recommend_json = {"clamping_force_RC": min(clamping_list) / 10,
                                             "space_bars": max(die_width, die_length),
                                             "clamping_force": claping_force_calc}
            return JsonResponse(clamping_force_recommend_json, safe=False)