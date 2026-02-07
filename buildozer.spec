[app]
# (str) Title of your app
title = HelloCall

# (str) Package name (must be unique, lowercase, no spaces)
package.name = hellocall

# (str) Package domain (reverse DNS style, e.g., org.example)
package.domain = com.prioum

# (str) Source code file
source.include_exts = py,png,jpg,kv,atlas

# (str) The main Python file
source.main = hellocall_dialer.py

# (str) Version
version = 1.0.0

# (str) Orientation: portrait or landscape
orientation = portrait

# (list) Permissions your app needs
android.permissions = INTERNET,CALL_PHONE

# (list) Android API min/max
android.minapi = 21
android.sdk = 31
android.ndk = 24b

# (str) Package requirements
requirements = python3,kivy

# (str) Icon / splash (optional)
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
