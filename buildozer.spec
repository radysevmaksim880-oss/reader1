[app]

title = Reader
package.name = reader
package.domain = org.maxim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.sdk = 31
android.build_tools_version = 33.0.2

android.ndk = 25b
android.ndk_api = 21

android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
p4a.python_version = 3.10

[buildozer]
log_level = 2
warn_on_root = 1
