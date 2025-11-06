[app]
title = Caracterizador de Antenas
package.name = myapp
package.domain = org.test
source.dir = .

source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3==3.9,kivy==2.3.0,numpy==1.21.6,matplotlib==3.4.3,pillow,pyjnius,requests

p4a.fork = kivy
p4a.python_version = 3.9
p4a.local_recipes = ./recipes
p4a.branch = develop
p4a.bootstrap = sdl2

icon.filename = icone.png

orientation = portrait
fullscreen = 0

android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_SCAN,BLUETOOTH_CONNECT,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 24
android.ndk_api = 23
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a
p4a.extra_env_vars = CFLAGS=-std=c++17
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
