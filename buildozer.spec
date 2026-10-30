[app]

title = Simple Flashlight
package.name = simpleflashlight
package.domain = org.akshai

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,plyer

orientation = portrait
fullscreen = 0

android.permissions = CAMERA,FLASHLIGHT

android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1