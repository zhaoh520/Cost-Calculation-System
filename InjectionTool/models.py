from django.db import models

# Create your models here.
#海天注塑机参数
class InjectionMachineInfo(models.Model):
    machine_model = models.CharField(max_length=8, verbose_name='注塑机型号', blank=True, null=True)            #注塑机型号
    screw_type = models.CharField(max_length=1, verbose_name='螺杆类型', blank=True, null=True)                  #螺杆类型
    screw_diameter = models.IntegerField(verbose_name='螺杆直径', blank=True, null=True)                           #螺杆直径
    screw_LD_ratio = models.IntegerField(verbose_name='螺杆长径比', blank=True, null=True)                          #螺杆长径比
    shot_size_therotetical = models.IntegerField(verbose_name='理论容量', blank=True, null=True)                   #理论容量
    injection_weight_PS = models.IntegerField(verbose_name='射出量', blank=True, null=True)            #射出量
    injection_speed = models.FloatField(verbose_name='射出速度', blank=True, null=True)             #射出速度
    plasticizing_capacity = models.IntegerField(verbose_name='塑化能力', blank=True, null=True)           #塑化能力
    injection_pressure = models.IntegerField(verbose_name='射出压力', blank=True, null=True)           #射出压力
    screw_speed = models.IntegerField(verbose_name='螺杆转速', blank=True, null=True)           #螺杆转速
    clamping_force = models.IntegerField(verbose_name='锁模力', blank=True, null=True)            #锁模力
    clamping_stroke = models.IntegerField(verbose_name='锁模行程', blank=True, null=True)           #锁模行程
    space_between_tie_bars_x = models.IntegerField(verbose_name='拉杆间隔_x', blank=True, null=True)         # 拉杆间隔_x
    space_between_tie_bars_y = models.IntegerField(verbose_name='拉杆间隔_y', blank=True, null=True)          # 拉杆间隔_y
    max_mold_height = models.IntegerField(verbose_name='最大模厚', blank=True, null=True)           #最大模厚
    min_mold_height = models.IntegerField(verbose_name='最小模厚', blank=True, null=True)           #最小模厚
    toggle_stroke = models.IntegerField(verbose_name='开模行程', blank=True, null=True)           #开模行程
    ejector_tonnage = models.IntegerField(verbose_name='顶出力', blank=True, null=True)            #顶出力
    ejector_number = models.IntegerField(verbose_name='顶出杆根数', blank=True, null=True)          #顶出杆根数
    max_pump_pressure = models.FloatField(verbose_name='最大泵压力', blank=True, null=True)            # 最大泵压力
    pump_motor_power = models.IntegerField(verbose_name='马达输出功率', blank=True, null=True)         #马达输出功率
    heater_power = models.FloatField(verbose_name='加热器输出功率', blank=True, null=True)          #加热器输出功率
    machine_length = models.FloatField(verbose_name='机器外形长度', blank=True, null=True)           #机器外形长度
    machine_width = models.IntegerField(verbose_name='机器外形宽度', blank=True, null=True)         #机器外形宽度
    machine_height = models.FloatField(verbose_name='机器外形高度', blank=True, null=True)           #机器外形高度
    machine_weight = models.FloatField(verbose_name='机械重量', blank=True, null=True)             #机械重量
    container_capacity = models.IntegerField(verbose_name='贮料器容量', blank=True, null=True)          #贮料器容量
    hppper_capacity = models.IntegerField(verbose_name='料简体积', blank=True, null=True)           #料简体积
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        managed = True
        db_table = 'injection_machine_info'
        verbose_name = '注塑机参数'

    def __str__(self):
        """定义每个数据对象显示的信息"""
        return self.machine_model + self.screw_type

# 推荐模穴数
class NumberCaves(models.Model):
    """projection_area_min	projection_area_max	number_die_caves
                120000		                            1
                1200	        120000	                2
                0	            1200	                4
    """
    projection_area_min = models.IntegerField(verbose_name='零件投影面积min', blank=True, null=True)
    projection_area_max = models.IntegerField(verbose_name='零件投影面积max', blank=True, null=True)
    number_die_caves = models.IntegerField(verbose_name='模穴数', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'number_die_caves'
        verbose_name = '模穴数推荐'

# 模内压力
class pressure_in_mold(models.Model):
    """material_type	pressure_in_mold	factor_min_adding_glass_fiber	factor_max_adding_glass_fiber """
    material_type = models.CharField(max_length=20, verbose_name='材料类型', blank=True, null=True)
    pressure_in_mold = models.IntegerField(verbose_name='模内压力', blank=True, null=True)
    factor_min_adding_glass_fiber = models.FloatField(verbose_name='加玻纤系数min', blank=True, null=True)
    factor_max_adding_glass_fiber = models.FloatField(verbose_name='加玻纤系数max', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pressure_in_mold'
        verbose_name = '模内压力'

#     材料密度
class density_material(models.Model):
    """material_type	density_min	  density_max	 """
    material_type = models.CharField(max_length=20, verbose_name='材料类型', blank=True, null=True)
    density_min = models.FloatField(verbose_name='密度min', blank=True, null=True)
    density_max = models.FloatField(verbose_name='密度max', blank=True, null=True)
    pressure_in_mold = models.IntegerField(verbose_name='模内压力', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'density_material'
        verbose_name = '材料密度'


#     模具边距
class die_edge_distance(models.Model):
    """product_length_min	product_length_max	  die_edge_distance	 """
    product_length_min = models.IntegerField(verbose_name='零件长边_min', blank=True, null=True)
    product_length_max = models.IntegerField(verbose_name='零件长边_max', blank=True, null=True)
    die_edge_distance = models.IntegerField(verbose_name='模具边距', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'die_edge_distance'
        verbose_name = '模具边距'

#     材料利用率
class material_utilization_rate(models.Model):
    """product_net_weight_min	product_net_weight_max	material_utilization_rate"""
    product_net_weight_min = models.IntegerField(verbose_name='零件净重_min', blank=True, null=True)
    product_net_weight_max = models.IntegerField(verbose_name='零件净重_max', blank=True, null=True)
    material_utilization_rate = models.FloatField(verbose_name='材料利用率', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'material_utilization_rate'
        verbose_name = '材料利用率'