����ʹ�õĻ�����
1)����ϵͳ��Windows10רҵ��
2) Python�汾��Python 3.7
3) Django�汾��Django�汾 2.2.1
4) �������Chorme�����

���ʹ���˽����ļ�.sql ������������������
--------------
�������ݿ⡣
��������ִ�У�python manage.py makemigrations ����Ǩ���ļ���
Ȼ��ִ�У�python manage.py migrate �������ݿ���
��MySQL���ݿ⣬LabAdmin����ӳ�ʼ����Ա�˺š�
---------------
���ʹ���˽����ļ�.sql ������������������


��projects/settings.py���������ݿ⣺
��������Ĵ��롣
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # ���ݿ�����
        'NAME': 'lab2',         # ��Ҫ�洢���ݵĿ���������Ҫ����֮
        'USER': 'root',         # ���ݿ��û���
        'PASSWORD': '123456',     # ����
        'HOST': 'localhost',    # ����
        'PORT': '3306',         # ���ݿ�ʹ�õĶ˿�
    }
}

��Ҫ����������������ҳ�õ�������Դû���ڱ��أ���font-awesomeͼ��⣬�����������أ���������ʹ�á�

Ȼ�����У�python manage.py runserver�������С�
��½��ַ��http://localhost:8000/login/�������Ա���뼴�ɵ�½��
