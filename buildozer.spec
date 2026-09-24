[app]

title = Reader
package.name = reader
package.domain = org.maxim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3==3.11.0,kivy,pyjnius,gtts

orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.2

android.ndk = 25b
android.ndk_api = 21

android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Жестко указываем стабильную версию Python для сборки
p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
