<<<<<<< HEAD
"""
Django settings for mall project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 让django找到apps包
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# print(sys.path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g_@n0syz8mas8p$9)_-clscb*06u3j4w=$fpi&2ewkimhfwn&3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# CORS
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    'www.meiduo.site:8080',
<<<<<<< HEAD
    '192.168.35.21:8080',

    '192.168.107.128:8080'
=======
    '192.168.35.30:8080'
>>>>>>> origin/returnes
)

CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

#允许哪些主机访问
# ALLOWED_HOSTS = ['*']
<<<<<<< HEAD

ALLOWED_HOSTS = ['127.0.0.1','api.meiduo.site','192.168.150.1','192.168.107.128']
=======
ALLOWED_HOSTS = ['127.0.0.1','api.meiduo.site','192.168.35.30']
>>>>>>> origin/returnes

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users',
    # 'users.apps.UsersConfig',
    # 'corsheaders',#解决后端跨域问题
    'oauth.apps.OauthConfig',
    'areas.apps.AreasConfig',
    'goods.apps.GoodsConfig',
    'contents.apps.ContentsConfig',
    'orders.apps.OrdersConfig',
    'pay.apps.PayConfig',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'django_crontab',  # 定时任务
    'haystack',# 搜索引擎接口
<<<<<<< HEAD
    # xadmin
    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',
=======
    #xadmin
    'xadmin',
    'crispy_forms',
    'reversion',
>>>>>>> origin/returnes

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
<<<<<<< HEAD
<<<<<<< HEAD
        'HOST': '127.0.0.1',  # 数据库主机
        # 'HOST': '192.168.35.21',  # 数据库主机
=======
        'HOST': '192.168.35.21',  # 数据库主机
>>>>>>> origin/returnes
        # 'HOST': '192.168.150.145',  # 数据库主机
=======
        'HOST': '192.168.35.21',  # 数据库主机
        # 'HOST': '127.0.0.1',  # 数据库主机
>>>>>>> origin/first
        'PORT': 3306,  # 数据库端口
        'USER': 'meiduo',  # 数据库用户名
        'PASSWORD': 'meiduo',  # 数据库用户密码
        'NAME': 'meiduo_mall'  # 数据库名字
    }
}

# redis 配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
<<<<<<< HEAD
        # "LOCATION": "redis://192.168.35.21:6379/0",
        "LOCATION": "redis://127.0.0.1:6379/0",
=======
        "LOCATION": "redis://192.168.35.21:6379/0",
        # "LOCATION": "redis://127.0.0.1:6379/0",
>>>>>>> origin/returnes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
<<<<<<< HEAD
        # "LOCATION": "redis://192.168.35.21:6379/1",
        "LOCATION": "redis://127.0.0.1:6379/1",
=======
        "LOCATION": "redis://192.168.35.21:6379/1",
        # "LOCATION": "redis://127.0.0.1:6379/1",
>>>>>>> origin/returnes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 图形验证码
    "code": {
        "BACKEND": "django_redis.cache.RedisCache",
<<<<<<< HEAD
        # "LOCATION": "redis://192.168.35.21:6379/2",
        "LOCATION": "redis://127.0.0.1:6379/2",
=======
        "LOCATION": "redis://192.168.35.21:6379/2",
        # "LOCATION": "redis://127.0.0.1:6379/2",
>>>>>>> origin/returnes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    #存放省市区信息
    "areas": {
        "BACKEND": "django_redis.cache.RedisCache",
<<<<<<< HEAD
        # "LOCATION": "redis://192.168.35.21:6379/3",
        "LOCATION": "redis://127.0.0.1:6379/3",
=======
        "LOCATION": "redis://192.168.35.21:6379/3",
        # "LOCATION": "redis://127.0.0.1:6379/3",
>>>>>>> origin/returnes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "history": {
        "BACKEND": "django_redis.cache.RedisCache",
<<<<<<< HEAD
        # "LOCATION": "redis://192.168.35.21:6379/4",
        "LOCATION": "redis://127.0.0.1:6379/4",
=======
        "LOCATION": "redis://192.168.35.21:6379/4",
        # "LOCATION": "redis://127.0.0.1:6379/4",
>>>>>>> origin/returnes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
<<<<<<< HEAD
        # "LOCATION": "redis://192.168.35.21:6379/5",
        "LOCATION": "redis://127.0.0.1:6379/5",
=======
        "LOCATION": "redis://192.168.35.21:6379/5",
        # "LOCATION": "redis://127.0.0.1:6379/5",
>>>>>>> origin/returnes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# DRF扩展,存储省市区信息
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'areas',
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    ),
    # 异常处理#,异常处理通用文件配置
    'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 分页配置类配置项
    'DEFAULT_PAGINATION_CLASS':'utils.pagination.StandardResultsSetPagination',
}

# 用户表继承django自带模型
AUTH_USER_MODEL = 'users.User'
import datetime

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),# 指明token有效期
    'JWT_RESPONSE_PAYLOAD_HANDLER':'utils.users.jwt_response_payload_handler',

}

# 默认认证后端
AUTHENTICATION_BACKENDS = [
   'utils.users.UsernameMobileAuthBackend',
]

# QQ登录参数
QQ_CLIENT_ID = '101474184'
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c'

# QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html'
<<<<<<< HEAD
QQ_REDIRECT_URI = 'http://192.168.107.128:8080/oauth_callback.html'

=======
QQ_REDIRECT_URI = 'http://192.168.35.30:8080/oauth_callback.html'
>>>>>>> origin/returnes

#邮箱认证配置信息
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = 'returnes@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = '520000000'
#收件人看到的发件人
EMAIL_FROM = '美多商城<returnes@163.com>'


# FastDFS
FDFS_URL = 'http://192.168.107.128:8888/'  # 访问图片的路径域名 ip地址修改为自己机器的ip地址
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/docker_fastdfs/client.conf')

# django文件存储
DEFAULT_FILE_STORAGE = 'utils.docker_fastdfs.storage_manage.FastDFSStorage'


# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''

# 生成的静态html文件保存目录
# GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(BASE_DIR), 'front')
GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(BASE_DIR), 'front')


# 定时任务
CRONJOBS = [
    # 每5分钟执行一次生成主页静态文件
    ('*/1 * * * *', 'contents.crons.generate_static_index_html', '>> /Users/yangjuan/Desktop/123/mall/logs/crontab.log')

]

# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'


# Haystack 搜索引擎接口
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.35.21:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# 支付宝
ALIPAY_APPID = "2016092300577627"
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"
ALIPAY_DEBUG = True
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/app_private_key.pem')
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/alipay_public_key.pem')


# 买家账号
# 买家账号ptpdem0491@sandbox.com
# 登录密码111111
# 支付密码111111

# ===========================日志配置=============================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/meiduo.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
        },
    }
}
=======
"""
Django settings for mall project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 让django找到apps包
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# print(sys.path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g_@n0syz8mas8p$9)_-clscb*06u3j4w=$fpi&2ewkimhfwn&3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# CORS
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    'www.meiduo.site:8080',
    '192.168.35.21:8080',
    '192.168.198.152:8080'
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

#允许哪些主机访问
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['127.0.0.1','api.meiduo.site','192.168.198.152']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'users',
    # 'users.apps.UsersConfig',
    'corsheaders',#解决后端跨域问题
    'oauth.apps.OauthConfig',
    'areas.apps.AreasConfig',
    'goods.apps.GoodsConfig',
    'contents.apps.ContentsConfig',
    'orders.apps.OrdersConfig',
    'pay.apps.PayConfig',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'django_crontab',  # 定时任务
    'haystack',# 搜索引擎接口
    #xadmin
    # 'xadmin',
    # 'crispy_forms',
    # 'reversion',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'HOST': '127.0.0.1',  # 数据库主机
        'HOST': '192.168.35.21',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'meiduo',  # 数据库用户名
        'PASSWORD': 'meiduo',  # 数据库用户密码
        'NAME': 'meiduo_mall'  # 数据库名字
    }
}
# redis 配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.35.21:6379/0",
        # "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.35.21:6379/1",
        # "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 图形验证码
    "code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.35.21:6379/2",
        # "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    #存放省市区信息
    "areas": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.35.21:6379/3",
        # "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "history": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.35.21:6379/4",
        # "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.35.21:6379/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# DRF扩展,存储省市区信息
REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'areas',
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    ),
    # 异常处理#,异常处理通用文件配置
    'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 分页配置类配置项
    'DEFAULT_PAGINATION_CLASS':'utils.pagination.StandardResultsSetPagination',
}

# 用户表继承django自带模型
AUTH_USER_MODEL = 'users.User'
import datetime

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),# 指明token有效期
    'JWT_RESPONSE_PAYLOAD_HANDLER':'utils.users.jwt_response_payload_handler',

}

# 默认认证后端
AUTHENTICATION_BACKENDS = [
   'utils.users.UsernameMobileAuthBackend',
]

# QQ登录参数
QQ_CLIENT_ID = '101474184'
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c'
# QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html'
# QQ_REDIRECT_URI = 'http://192.168.35.21:8080/oauth_callback.html'
QQ_REDIRECT_URI = 'http://192.168.198.152:8080/oauth_callback.html'

# 微博登录

WEIBO_Key = '3305669385'
WEIBO_Secret = '74c7bea69d5fc64f5c3b80c802325276'
WEIBO_REDIRECT_URI = 'http://www.meiduo.site:8080/sina_callback.html'



#邮箱认证配置信息
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = 'returnes@163.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = '520000000'
#收件人看到的发件人
EMAIL_FROM = '美多商城<returnes@163.com>'


# FastDFS
FDFS_URL = 'http://192.168.35.21:8888/'  # 访问图片的路径域名 ip地址修改为自己机器的ip地址
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/docker_fastdfs/client.conf')

# django文件存储
DEFAULT_FILE_STORAGE = 'utils.docker_fastdfs.storage_manage.FastDFSStorage'


# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''

# 生成的静态html文件保存目录
# GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(BASE_DIR), 'front')
GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(BASE_DIR), 'front')


# 定时任务
CRONJOBS = [
    # 每5分钟执行一次生成主页静态文件
    # ('*/5 * * * *', 'contents.crons.generate_static_index_html' ,'>> '+os.path.join(BASE_DIR,'logs\\')+'crontab.log')
    ('*/5 * * * *', 'contents.crons.generate_static_index_html', '>> /home/python/Desktop/p5/123/mall/logs/crontab.log')

]

# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'


# Haystack 搜索引擎接口
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.35.21:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# 支付宝
ALIPAY_APPID = "2016092300577627"
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"
ALIPAY_DEBUG = True
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/app_private_key.pem')
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'apps/pay/keys/alipay_public_key.pem')


# 买家账号
# 买家账号ptpdem0491@sandbox.com
# 登录密码111111
# 支付密码111111

# ===========================日志配置=============================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/meiduo.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
        },
    }
}
>>>>>>> origin/wen
