from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/",views.login,name='login'),
    path("register/",views.register,name='register'),
    path("template/",views.template,name='template'),
    path("signup/",views.signup,name='signup'),
    path("personal_info/",views.personal_info,name='personal_info'),
    path("gocheck/",views.gocheck,name="gocheck"),
    path("checkhistory/",views.checkhistory,name="checkhistory"),
    path("charts/",views.charts,name="charts"),
    path("responseCheck/",views.responseCheck,name="responseCheck"),
    path("logincheck/",views.logincheck,name="logincheck"),
    path("checkout/",views.checkout,name="checkout"),
    # 学生
    path("student/",views.student,name='student'),
    path("queryStudent/",views.queryStudent,name='queryStudent'),
    path("addStudent/",views.addStudent,name='addStudent'),
    path("delStudent/",views.delStudent,name='delStudent'),
    path("editStudent/",views.editStudent,name='editStudent'),
    # 制造商
    path("manufactor/",views.manufactor,name='manufactor'),
 	path("queryManufactor/",views.queryManufactor,name='queryManufactor'),
    path("addManufactor/",views.addManufactor,name='addManufactor'),
    path("delManufactor/",views.delManufactor,name='delManufactor'),
    path("editManufactor/",views.editManufactor,name='editManufactor'),
    # 设备
    path("device/",views.device,name='device'),
 	path("queryDevice/",views.queryDevice,name='queryDevice'),
    path("addDevice/",views.addDevice,name='addDevice'),
    path("delDevice/",views.delDevice,name='delDevice'),
    path("editDevice/",views.editDevice,name='editDevice'),

    #设备管理
    path("devicefix/",views.devicefix,name='devicefix'),
    path("deviceab/",views.deviceab,name='deviceab'),
    path("devicein/",views.devicein,name='devicein'),
    path("queryfreeDevice/",views.queryfreeDevice,name='queryfreeDevice'),
    path("fixDevice/",views.fixDevice,name='fixDevice'),
    path("deviceab/",views.deviceab,name='deviceab'),
    path("fixdeal/",views.fixdeal,name="fixdeal"),
    path("queryfixDevice/",views.queryfixDevice,name="queryfixDevice"),
    #记录信息
    path("fixrecord/",views.fixrecord,name='fixrecord'),
    path("abrecord/",views.abrecord,name='abrecord'),
    path("loanrecord/",views.loanrecord,name='loanrecord'),
    path("rtrecord/",views.rtrecord,name='rtrecord'),
    path("imrecord/",views.imrecord,name='imrecord'),

    path("addinrecord/",views.addinrecord,name="addinrecord"),
    path("abDevice/",views.abDevice,name="abDevice"),
    path("loanrecord_admin/",views.loanrecord_admin,name="loanrecord_admin"),
    path("rtrecord_admin/",views.rtrecord_admin,name="rtrecord_admin"),

    path("abfixDevice/",views.abfixDevice,name="abfixDevice"),
    path("fixinDevice/",views.fixinDevice,name="fixinDevice"),
    # 学生端链接
    path("home_stu/",views.home_stu,name="home_stu"),
    path("deviceloan/",views.deviceloan,name="deviceloan"),
    path("device_stu/",views.device_stu,name="device_stu"),
    path("manufactor_stu/",views.manufactor_stu,name="manufactor_stu"),
    path("personal_info_stu/",views.personal_info_stu,name="personal_info_stu"),
    path("checkResponse/",views.checkResponse,name="checkResponse"),
    path("waitcheck/",views.waitcheck,name="waitcheck"),
    path("sturecord/",views.sturecord,name="sturecord"),

    path("queryOwnerDevice/",views.queryOwnerDevice,name="queryOwnerDevice"),
    path("device_stu_own/",views.device_stu_own,name="device_stu_own"),
    path("loanDevice/",views.loanDevice,name="loanDevice"),
    path("rtDevice/",views.rtDevice,name="rtDevice"),
    path("updateStu/",views.updateStu,name="updateStu"),
    path("updateAdmin/",views.updateAdmin,name="updateAdmin")
    

]