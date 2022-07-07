# coding=utf-8
import random

d = {
     "9102":"道路工程",
     "9103": "桥涵工程",
     "9104": "隧道工程",
     "9105": "管网工程",
     "9106": "水处理工程",
     }

s  = "INSERT INTO `oa_pm`.`pm_supplier_category`(`id`, `is_type`, `descrption`, `code`, `pid_code`, `name`, `initiator`, `is_delete`, `create_time`, `update_time`) VALUES ('12619375256077{}', 1, NULL, '{}', '91', '{}', NULL, 0, '2021-08-25 16:29:38', '2021-08-25 16:29:38');"

for i in d.keys():
     num = int(random.uniform(1,9)*1000)
     sql = s.format(num,i,d[i])
     print(sql)