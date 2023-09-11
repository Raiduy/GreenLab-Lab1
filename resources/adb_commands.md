# Useful ADB Commands

View connected devices
```bash 
adb devices
```

View existing apps
```bash
adb shell pm list packages
```

Install an app
```bash
adb install <path_to_apk>
```

Run an app
```bash
adb shell monkey -p <package_name> -c android.intent.category.LAUNCHER 1
```

Uninstall an app
```bash
adb uninstall <package_name>
```

Logcat live view
```bash
adb logcat
```
Push a file to the device
```bash
adb push <path_to_file_on_host> <path_to_save_file_on_device>
```

Pull a file from the device
```bash
adb pull <path_to_file_on_device> <path_to_save_file_on_host>
```

Shell into the device
```bash
adb shell
```

Kill the server
```bash
adb kill-server
```


Wireless connection (device_ip can be found under WIFI in the device settings) (will not work on university network)
```bash
adb tcpip 5555
adb connect <device_ip>:5555

OR USE THE adb_connect_wifi.sh SCRIPT
```