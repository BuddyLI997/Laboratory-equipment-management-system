from django.db import models
    
# 账户：
# 姓名，id，密码，年龄，性别
class LabAdmin(models.Model):
    uName = models.CharField(max_length=20)
    uid = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)
    uage = models.IntegerField()
    gender = models.CharField(max_length=2)

#学生 班级
class Student(models.Model):
    uName = models.CharField(max_length=20)
    uid = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)
    uage = models.IntegerField()
    gender = models.CharField(max_length=2)
    sclass = models.CharField(max_length=20)

# 制造商 姓名，电话，描述
class Manufactor(models.Model):
    name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    

# 设备 类型，价格，购买日期，各种状态
class Device(models.Model):
    modelid = models.CharField(max_length=20) #型号
    name = models.CharField(max_length=20)   #设备名
    manufactor = models.ForeignKey(Manufactor, on_delete=models.CASCADE) # 
    typeName   = models.CharField(max_length=20)
    price  = models.FloatField()
    inDate= models.DateField(auto_now_add=True)
    buyDate=models.DateField()
    use = models.IntegerField()
    state =models.CharField(max_length=20) #空闲，借出，审核，维护，报废
    owner = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)

class StudentRecord(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    rtype = models.CharField(max_length=20) #借用/归还
    Datetime=models.DateTimeField(auto_now_add=True)
    state =models.CharField(max_length=5) # 成功/拒绝/审核
    student =models.ForeignKey(Student,on_delete=models.CASCADE,related_name = "studentRecord")
    des =models.CharField(max_length=200)



class AdminRecord(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    rtype = models.CharField(max_length=20) #报修，报废
    Datetime=models.DateTimeField(auto_now_add=True)
    state =models.CharField(max_length=5,null=True) # 修成/未修成
    admin =models.ForeignKey(LabAdmin,on_delete=models.CASCADE)
    des =models.CharField(max_length=200)
    fixtime=models.DateTimeField(null=True)

class Admincheck(models.Model):
    studentRecord = models.OneToOneField(StudentRecord,on_delete=models.CASCADE,related_name="adminCheck")
    Datetime=models.DateTimeField(auto_now_add=True)
    state =models.CharField(max_length=5) # 处理/未处理
    dealtime=models.DateTimeField(auto_now=True)
    admin =models.ForeignKey(LabAdmin,on_delete=models.CASCADE,null=True)
    des =models.CharField(max_length=200)
    

class DeviceinRecord(models.Model):
    modelid = models.CharField(max_length=20)
    rtype = models.CharField(max_length=20) #报修，报废
    Datetime=models.DateTimeField(auto_now_add=True)
    state =models.CharField(max_length=5,null=True) # 修成/未修成
    admin =models.ForeignKey(LabAdmin,on_delete=models.CASCADE)
    des =models.CharField(max_length=200)
    num=models.IntegerField(null=True)
    buyDate=models.DateField(null=True)
    price=models.FloatField(null=True)
    totalprice=models.FloatField(null=True)