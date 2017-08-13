@echo off
echo Re-install AUT:
echo ----------------------------------------------------------------------
echo Uninstall:
adb uninstall com.skysoft.kkbox.android
echo Install:
adb install "com.skysoft.kkbox.android.apk"
echo ----------------------------------------------------------------------
