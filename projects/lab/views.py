#coding=utf-8 
import time
import datetime
from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from lab.models import Student,Manufactor,Device,LabAdmin,AdminRecord,Admincheck,StudentRecord,DeviceinRecord
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt 
def updateStu(request):
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	name=request.POST.get("name")
	age=request.POST.get("age")
	gender=request.POST.get("gender")
	sclass=request.POST.get("class")
	student.uName=name
	student.uage=age
	student.gender=gender
	student.sclass=sclass
	student.save()
	request.session['name']=name
	return redirect('/personal_info_stu/')

@csrf_exempt 
def updateAdmin(request):
	uid=request.session['user']
	admin=LabAdmin.objects.get(uid=uid)
	name=request.POST.get("name")
	age=request.POST.get("age")
	gender=request.POST.get("gender")
	admin.uName=name
	admin.uage=age
	admin.gender=gender
	admin.save()
	request.session['name']=name
	return redirect('/personal_info/')

def charts(request):
	devicenum=Device.objects.count()
	usernum=Student.objects.count()
	freeDevicesnum=Device.objects.filter(state="空闲").count()
	abDevicesnum=Device.objects.filter(state="报废").count()
	fixDevicesnum=Device.objects.filter(state="维修").count()
	loanDevicesnum=Device.objects.filter(state="借出").count()
	checkDevicesnum=Device.objects.filter(state="审核").count()
	return render(request,'charts.html',{'freeDevicesnum':freeDevicesnum,
		'abDevicesnum':abDevicesnum,
		'fixDevicesnum':fixDevicesnum,
		'loanDevicesnum':loanDevicesnum,
		'checkDevicesnum':checkDevicesnum,
		'devicenum':devicenum,
		'usernum':usernum})

@csrf_exempt  
def logincheck(request):
	uid=request.POST.get("user")
	upwd=request.POST.get("password")
	role=request.POST.get("role")
	if role=="学生":
		try:
			student=Student.objects.filter(upwd=upwd).get(uid=uid)
		except:
			return render(request,'login.html',{'data':1})
		request.session['user']=uid
		request.session['name']=student.uName
		request.session['role']="学生"
		return redirect('/home_stu/')
	else:
		try:
			admin=LabAdmin.objects.filter(upwd=upwd).get(uid=uid)
		except:
			return render(request,'login.html',{'data':1})
		request.session['user']=uid
		request.session['name']=admin.uName
		request.session['role']="管理员"
		request.session['msg']=Admincheck.objects.filter(state="未处理").count()
		return redirect('/home/')

def checkResponse(request):
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	data=student.studentRecord.filter(Q(state="接受")|Q(state="拒绝"))
	return render(request,'checkResponse.html',{'data':data})

def waitcheck(request):
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	data=StudentRecord.objects.filter(student=student).filter(state="审核中")
	return render(request,'waitcheck.html',{'data':data})

def sturecord(request):
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	data=StudentRecord.objects.filter(student=student)
	return render(request,'sturecord.html',{'data':data})

def device_stu(request):
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	data=student.device_set.all()
	return render(request,'device_stu.html')
def checkout(request):
	del request.session['user']
	del request.session['role']
	del request.session['name']
	return redirect('/login/')
def checkhistory(request):
	data=Admincheck.objects.filter(state="已处理")
	return render(request,'checkhistory.html',{'data':data})

def manufactor_stu(request):
	return render(request,'manufactor_stu.html')
def home_stu(request):
	devicenum=Device.objects.count()
	usernum=Student.objects.count()
	return render(request,'index_stu.html',{'devicenum':devicenum,'usernum':usernum})
def deviceloan(request):
	return render(request,'deviceloan.html')
def fixrecord(request):
	data=AdminRecord.objects.filter(rtype="报修")
	return render(request,'fixrecord.html',{'data': data})
def personal_info_stu(request):
	uid=request.session['user']
	user=Student.objects.get(uid=uid)
	return render(request,'personal_info_stu.html',{'stu':user})
def imrecord(request):
	data=DeviceinRecord.objects.filter(rtype="引入")
	return render(request,'imrecord.html',{'data': data})

def abrecord(request):
	data=AdminRecord.objects.filter(rtype="报废")
	return render(request,'abrecord.html',{'data': data})

def loanrecord(request):
	return render(request,'loanrecord.html')
def rtrecord(request):
	return render(request,'rtrecord.html')

def devicein(request):
	data=Manufactor.objects.all()
	return render(request,'devicein.html',{'data': data})


def device(request):
	data=Manufactor.objects.all()
	return render(request,'device.html',{'data': data})

def deviceab(request):
	data=Manufactor.objects.all()
	return render(request,'deviceab.html')

def devicefix(request):
	return render(request,'devicefix.html')
def login(request):
   return render(request,'login.html')

def register(request):
    return render(request,'lab/regist.html')

def student(request):
    return render(request,"student.html")
def manufactor(request):
	return render(request,"manufactor.html")
def home(request):
	devicenum=Device.objects.count()
	usernum=Student.objects.count()
	return render(request,"index.html",{'devicenum':devicenum,'usernum':usernum})

def personal_info(request):
	uid=request.session['user']
	admin=LabAdmin.objects.get(uid=uid)
	return render(request,"personal_info.html",{'admin':admin})

def signup(request):
	return render(request,"signup.html")
def template(request):
    return render(request,'base.html')
def allDevice(request):
    pass

def DeviceDetail(request):
    pass
def gocheck(request):
	data=Admincheck.objects.filter(state="未处理")
	return render(request,'gocheck.html',{'data': data})
def addaccount(request):
    pass
def device_stu_own(request):
	return render(request,'device_stu_own.html')
@csrf_exempt    
def queryOwnerDevice(request):
	page = request.POST.get('page')
	rows = request.POST.get('limit')
	name = request.POST.get('name')
	i = (int(page) - 1) * int(rows)
	j = (int(page) - 1) * int(rows) + int(rows)
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	if name:
		devices=student.device_set.filter(name__contains=name)
	else:
		devices=student.device_set.all()
	total = devices.count()
	devices = devices[i:j]
	resultdict = {}
	dict = []
	for s in devices:
		dic = {}
		dic['modelid']=s.modelid
		dic['id']=s.id
		dic['name']=s.name
		dic['manufactorId'] = s.manufactor.id
		dic['manufactorName'] = s.manufactor.name
		dic['typeName'] = s.typeName
		dic['price'] = s.price
		dic['buyDate']=s.buyDate
		dic['inDate'] = s.inDate
		dic['use'] = s.use
		dic['state'] = s.state
		dict.append(dic)
	resultdict['code'] = 0
	resultdict['msg'] = ""
	resultdict['count'] = total
	resultdict['data'] = dict
	return JsonResponse(resultdict, safe=False)

@csrf_exempt
def fixDevice(request):
	id=request.POST.get('id')
	device=Device.objects.get(id=id)
	des="闲置设备检测维修"
	device.state="维修"
	device.save()
	# 写条维修
	admin=LabAdmin.objects.get(id=1)
	rtype="报修"
	AdminRecord.objects.create(des=des,admin=admin,rtype=rtype,device=device,state="维修中")
	return JsonResponse({'message': 1}, safe=False)

@csrf_exempt    
def abDevice(request):
	id=request.POST.get('id')
	device=Device.objects.get(id=id)
	des="闲置设备直接报废"
	device.state="报废"
	device.save()
	uid=request.session['user']
	admin=LabAdmin.objects.get(uid=uid)
	rtype="报废"
	AdminRecord.objects.create(des=des,admin=admin,rtype=rtype,device=device)
	return JsonResponse({'message': 1}, safe=False) 

@csrf_exempt 
def responseCheck(request):
	cid =request.POST.get('cid')
	state =request.POST.get('state')
	msg =request.POST.get('msg')
	admincheck=Admincheck.objects.get(id=cid)
	uid=request.session['user']
	admin=LabAdmin.objects.get(uid=uid)
	rtype=admincheck.studentRecord.rtype
	if rtype=="借用":
		if state=="接受":
			student=admincheck.studentRecord.student
			device=admincheck.studentRecord.device
			device.owner=student
			device.state="借出"
			device.use+=1
			device.save()
		else:
			pass
	else:
		if state=="接受":
			student=admincheck.studentRecord.student
			device=admincheck.studentRecord.device
			device.owner=None
			device.state="空闲"
			device.save()
		else:
			pass
	admincheck.msg=msg
	studentRecord=admincheck.studentRecord
	studentRecord.state=state
	studentRecord.save()
	admincheck.admin=admin
	Admincheck.des=msg
	admincheck.state="已处理"
	admincheck.save()
	request.session['msg']=Admincheck.objects.filter(state="未处理").count()
	return JsonResponse({'message': 1}, safe=False)

@csrf_exempt    
def abfixDevice(request):
	id=request.POST.get('id')
	device=Device.objects.get(id=id)
	fixrecord=AdminRecord.objects.get(device=device)
	des="维修设备转报废"
	device.state="报废"
	device.save()
	admin=LabAdmin.objects.get(id=1)
	rtype="报废"
	print(fixrecord.state)
	fixrecord.fixtime= datetime.datetime.now()
	fixrecord.state="报废"
	fixrecord.save()
	AdminRecord.objects.create(des=des,admin=admin,rtype=rtype,device=device)
	return JsonResponse({'message': 1}, safe=False)

@csrf_exempt    
def fixinDevice(request):
	id=request.POST.get('id')
	device=Device.objects.get(id=id)
	fixrecord=AdminRecord.objects.get(device=device)
	device.state="空闲"
	device.save()
	print(fixrecord.state)
	fixrecord.fixtime= datetime.datetime.now()
	fixrecord.state="修完入库"
	fixrecord.save()
	return JsonResponse({'message': 1}, safe=False)
	
@csrf_exempt
def queryfreeDevice(request):
	page = request.POST.get('page')
	rows = request.POST.get('limit')
	name = request.POST.get('key[name]')
	i = (int(page) - 1) * int(rows)
	j = (int(page) - 1) * int(rows) + int(rows)
	if name:
		devices=Device.objects.filter(state="空闲").filter(name__contains=name)
	else:
		devices=Device.objects.filter(state="空闲")
	total = devices.count()
	devices = devices[i:j]
	resultdict = {}
	dict = []
	for s in devices:
	  dic = {}
	  dic['modelid']=s.modelid
	  dic['id']=s.id
	  dic['name']=s.name
	  dic['manufactorId'] = s.manufactor.id
	  dic['manufactorName'] = s.manufactor.name
	  dic['typeName'] = s.typeName
	  dic['price'] = s.price
	  dic['buyDate']=s.buyDate
	  dic['inDate'] = s.inDate
	  dic['use'] = s.use
	  dic['state'] = s.state
	  dict.append(dic)
	resultdict['code'] = 0
	resultdict['msg'] = ""
	resultdict['count'] = total
	resultdict['data'] = dict
	return JsonResponse(resultdict, safe=False)

@csrf_exempt
def queryStudent(request):
	page = request.POST.get('page')
	rows = request.POST.get('limit')
	name = request.POST.get('key[name]')
	i = (int(page) - 1) * int(rows)
	j = (int(page) - 1) * int(rows) + int(rows)
	if name:
		students=Student.objects.filter(uName__contains=name)
	else:	
		students=Student.objects.all()
	total = students.count()
	students = students[i:j]
	resultdict = {}
	dict = []
	for s in students:
	  dic = {}
	  dic['id']=s.id
	  dic['uName'] = s.uName
	  dic['uid'] = s.uid
	  dic['upwd'] = s.upwd
	  dic['uage'] = s.uage
	  dic['gender'] = s.gender
	  dic['sclass'] = s.sclass
	  dict.append(dic)
	resultdict['code'] = 0
	resultdict['msg'] = ""
	resultdict['count'] = total
	resultdict['data'] = dict
	return JsonResponse(resultdict, safe=False)

# 编辑学生
@csrf_exempt
def editStudent(request):
    id =request.POST.get('id')
    uid = request.POST.get('uid')
    uName = request.POST.get('uName')
    upwd = request.POST.get('upwd')
    uage = request.POST.get('uage')
    gender = request.POST.get('gender')
    sclass = request.POST.get('sclass')
    student = Student.objects.get(id=id)
    student.uid = uid
    student.uName = uName
    student.upwd = upwd
    student.uage = uage
    student.gender = gender
    student.sclass = sclass
    student.save()
    return JsonResponse({'message': 1}, safe=False)


# 新增学生
@csrf_exempt
def addStudent(request):
    uid = request.POST.get('uid')
    uName = request.POST.get('uName')
    upwd = request.POST.get('upwd')
    uage = request.POST.get('uage')
    gender = request.POST.get('gender')
    sclass = request.POST.get('sclass')
    print(uid,uName,upwd,upwd,gender,sclass)
    student = Student.objects.create(uid=uid,uName=uName,upwd=upwd,uage=uage,gender=gender,sclass=sclass)
    student.save()
    return JsonResponse({'message': 1}, safe=False)

# 删除学生
@csrf_exempt
def delStudent(request):
	id = request.POST.get('id')
	Student.objects.filter(id=id).delete()
	return JsonResponse({'message': 1}, safe=False)


# 查询管理员
@csrf_exempt
def queryAdmin(request):
	page = request.POST.get('page')
	rows = request.POST.get('limit')

	i = (int(page) - 1) * int(rows)
	j = (int(page) - 1) * int(rows) + int(rows)
	if name:
		students=Student.objects.filter(uName__contains=name)
	else:	
		students=Student.objects.all()
	total = students.count()
	students = students[i:j]
	resultdict = {}
	dict = []
	for s in students:
	  dic = {}
	  dic['id']=s.id
	  dic['uName'] = s.uName
	  dic['uid'] = s.uid
	  dic['upwd'] = s.upwd
	  dic['uage'] = s.uage
	  dic['gender'] = s.gender
	  dic['sclass'] = s.sclass
	  dict.append(dic)
	resultdict['code'] = 0
	resultdict['msg'] = ""
	resultdict['count'] = total
	resultdict['data'] = dict
	return JsonResponse(resultdict, safe=False)

# 编辑管理员
@csrf_exempt
def editAdmin(request):
    id =request.POST.get('id')
    uid = request.POST.get('uid')
    uName = request.POST.get('uName')
    upwd = request.POST.get('upwd')
    uage = request.POST.get('uage')
    gender = request.POST.get('gender')
    sclass = request.POST.get('sclass')
    student = Student.objects.get(id=id)
    student.uid = uid
    student.uName = uName
    student.upwd = upwd
    student.uage = uage
    student.gender = gender
    student.sclass = sclass
    student.save()
    return JsonResponse({'message': 1}, safe=False)


# 添加管理员
@csrf_exempt
def addAdmin(request):
    uid = request.POST.get('uid')
    uName = request.POST.get('uName')
    upwd = request.POST.get('upwd')
    uage = request.POST.get('uage')
    gender = request.POST.get('gender')
    sclass = request.POST.get('sclass')
    print(uid,uName,upwd,upwd,gender,sclass)
    student = Student.objects.create(uid=uid,uName=uName,upwd=upwd,uage=uage,gender=gender,sclass=sclass)
    student.save()
    return JsonResponse({'message': 1}, safe=False)

# 删除管理员
@csrf_exempt
def delAdmin(request):
	id = request.POST.get('id')
	Student.objects.filter(id=id).delete()
	return JsonResponse({'message': 1}, safe=False)

# 查询设备
@csrf_exempt
def queryDevice(request):
	name=request.POST.get('key[name]')

	page = request.POST.get('page')
	rows = request.POST.get('limit')

	i = (int(page) - 1) * int(rows)
	j = (int(page) - 1) * int(rows) + int(rows)
	if name:
		devices=Device.objects.filter(Q(name__contains=name))
	else:
		devices=Device.objects.all()
	total = devices.count()
	devices = devices[i:j]
	resultdict = {}
	dict = []
	for s in devices:
	  dic = {}
	  dic['modelid']=s.modelid
	  dic['id']=s.id
	  dic['name']=s.name
	  dic['manufactorId'] = s.manufactor.id
	  dic['manufactorName'] = s.manufactor.name
	  dic['typeName'] = s.typeName
	  dic['price'] = s.price
	  dic['buyDate']=s.buyDate
	  dic['inDate'] = s.inDate
	  dic['use'] = s.use
	  dic['state'] = s.state
	  dict.append(dic)
	resultdict['code'] = 0
	resultdict['msg'] = ""
	resultdict['count'] = total
	resultdict['data'] = dict
	return JsonResponse(resultdict, safe=False)


@csrf_exempt
def queryfixDevice(request):
	name=request.POST.get('key[name]')
	page = request.POST.get('page')
	print(page)
	rows = request.POST.get('limit')
	print(rows)

	i = (int(page) - 1) * int(rows)
	j = (int(page) - 1) * int(rows) + int(rows)

	if name:
		devices=Device.objects.filter(name__contains=name).filter(state="维修")
	else:	
		devices=Device.objects.filter(state="维修")
	total = devices.count()
	devices = devices[i:j]
	resultdict = {}
	dict = []
	for s in devices:
	  dic = {}
	  dic['modelid']=s.modelid
	  dic['id']=s.id
	  dic['name']=s.name
	  dic['manufactorId'] = s.manufactor.id
	  dic['manufactorName'] = s.manufactor.name
	  dic['typeName'] = s.typeName
	  dic['price'] = s.price
	  dic['buyDate']=s.buyDate
	  dic['inDate'] = s.inDate
	  dic['use'] = s.use
	  dic['state'] = s.state
	  dict.append(dic)
	resultdict['code'] = 0
	resultdict['msg'] = ""
	resultdict['count'] = total
	resultdict['data'] = dict
	return JsonResponse(resultdict, safe=False)

# 编辑设备
@csrf_exempt
def editDevice(request):
    id =request.POST.get('id')
    name =request.POST.get('name')
    manufactorName = request.POST.get('manufactorName')
    manufactor=Manufactor.objects.get(name=manufactorName)
    modelid=request.POST.get('modelid')
    typeName = request.POST.get('typeName')
    price = request.POST.get('price')
    inDate = request.POST.get('inDate')
    use = request.POST.get('use')
    state = request.POST.get('state')
    buyDate = request.POST.get('buyDate')
    device = Device.objects.get(id=id)
    device.name=name;
    device.manufactor = manufactor
    device.typeName = typeName
    device.price = price
    device.inDate = inDate
    device.use = use
    device.state = state
    device.buyDate=buyDate
    device.save()
    return JsonResponse({'message': 1}, safe=False)


# 新增设备
@csrf_exempt
def addDevice(request):
    manufactorName = request.POST.get('manufactorName')
    name =request.POST.get('name')
    manufactor=Manufactor.objects.get(name=manufactorName)
    modelid=request.POST.get('modelid')
    typeName = request.POST.get('typeName')
    price = request.POST.get('price')
    inDate = request.POST.get('inDate')
    use = 0
    state = "空闲"
    buyDate = request.POST.get('buyDate')
    device = Device.objects.create(modelid=modelid,name=name,buyDate=buyDate,manufactor=manufactor,typeName=typeName,price=price,inDate=inDate,use=use,state=state)
    device.save()
    return JsonResponse({'message': 1}, safe=False)

# 删除设备
@csrf_exempt
def delDevice(request):
	id = request.POST.get('id')
	Device.objects.filter(id=id).delete()
	return JsonResponse({'message': 1}, safe=False)

# 查询制造商
@csrf_exempt
def queryManufactor(request):
	page = request.POST.get('page')
	rows = request.POST.get('limit')
	name = request.POST.get('key[name]')
	i = (int(page) - 1) * int(rows)
	j = (int(page) - 1) * int(rows) + int(rows)
	if name:
		manufactors=Manufactor.objects.filter(Q(name__contains=name))
	else:
		manufactors=Manufactor.objects.all()
	total = manufactors.count()
	manufactors = manufactors[i:j]
	resultdict = {}
	dict = []
	for s in manufactors:
	  dic = {}
	  dic['id']=s.id
	  dic['name'] = s.name
	  dic['telephone'] = s.telephone
	  dic['description'] = s.description
	  dict.append(dic)
	resultdict['code'] = 0
	resultdict['msg'] = ""
	resultdict['count'] = total
	resultdict['data'] = dict
	return JsonResponse(resultdict, safe=False)

# 编辑制造商
@csrf_exempt
def editManufactor(request):
    id =request.POST.get('id')
    name = request.POST.get('name')
    telephone = request.POST.get('telephone')
    description = request.POST.get('description')
    manufactor = Manufactor.objects.get(id=id)
    manufactor.name = name
    manufactor.telephone = telephone
    manufactor.description = description
    manufactor.save()
    return JsonResponse({'message': 1}, safe=False)


# 新增制造商
@csrf_exempt
def addManufactor(request):
    name = request.POST.get('name')
    telephone = request.POST.get('telephone')
    description = request.POST.get('description')
    manufactor = Manufactor.objects.create(name=name,telephone=telephone,description=description)
    manufactor.save()
    return JsonResponse({'message': 1}, safe=False)

# 删除制造商
@csrf_exempt
def delManufactor(request):
	id = request.POST.get('id')
	Manufactor.objects.filter(id=id).delete()
	return JsonResponse({'message': 1}, safe=False)

@csrf_exempt
def loanDevice(request):
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	id = request.POST.get('id')
	device=Device.objects.get(id=id)
	device.state="审核"
	device.save()
	rtype="借用"
	state="审核中"
	des="借用设备"
	studentRecord=StudentRecord.objects.create(student=student,device=device,rtype=rtype,state=state)
	Admincheck.objects.create(studentRecord=studentRecord,des="",state="未处理")
	return JsonResponse({'message': 1}, safe=False)

@csrf_exempt
def rtDevice(request):
	uid=request.session['user']
	student=Student.objects.get(uid=uid)
	id = request.POST.get('id')
	device=Device.objects.get(id=id)
	device.state="审核"
	device.owner=None
	device.save()
	rtype="归还"
	state="审核中"
	des="归还设备"
	studentRecord=StudentRecord.objects.create(student=student,device=device,rtype=rtype,state=state)
	Admincheck.objects.create(studentRecord=studentRecord,des="",state="未处理")
	return JsonResponse({'message': 1}, safe=False)

@csrf_exempt
def addinrecord(request):
	modelid=request.POST.get('modelid')
	des=request.POST.get('des')
	admin=LabAdmin.objects.get(id=1)
	num = request.POST.get('num')
	price=request.POST.get('price')
	buyDate=request.POST.get('buyDate')
	totalprice=int(num)*float(price)
	DeviceinRecord.objects.create(modelid=modelid,price=price,rtype="引入",des=des,admin=admin,num=num,totalprice=totalprice,buyDate=buyDate)
	return JsonResponse({'message': 1}, safe=False)

def loanrecord_admin(request):
	data=StudentRecord.objects.filter(state="接受").filter(rtype="借用")
	return render(request,"loanrecord_admin.html",{'data':data})

def rtrecord_admin(request):
	data=StudentRecord.objects.filter(state="接受").filter(rtype="归还")
	return render(request,"rtrecord_admin.html",{'data':data})

def  fixdeal(request):
	return render(request,"fixdeal.html")