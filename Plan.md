# Overview (5 minutes)
* Motivation (2 min)
    * Why do we need to test mobile apps?
    * Why do we need to test mobile apps on real devices?
* Tools (3 min)
    * Profilers explained
        * Monsoon (hardware)
        * BatteryManager-companion (software)
    * ADB Overview
        * install, run, uninstall, logcat, pull, push, shell among others
    * AndroidRunner Overview
        * What is AndroidRunner?

# ADB demo (15 min)
* Install ADB
* Set up device
* Connect to device
* Install an app
* Run an app
* Uninstall an app
* Logcat
* Pull
* Push
* Shell
* Wireless connection
* Troubleshooting

# AndroidRunner how does it work? (20 min)
* Files
    * config files
        * `run_stopping_condition`
        * `usb_handler` + caveats (RasPI 4B)
    * script files
    * interaction files
    * output files
    * `--progress` flag
* Profilers
    * BatteryManager-companion
    * [maybe others too?]

# AndroidRunner demo (45 min)
* FORK AndroidRunner
* Install AndroidRunner
* Before experiment checklist
    * Device:
        * Enable Developer options
        * Enable USB debugging
        * Stay awake (Dev options)
        * Minimum brightness (we're testing battery consumption, not screen consumption)
        * Disable/turn off notifications and updates for all services (i.e., Google Play Services, Google Play Store, etc.)
        * Disable app checking over adb (Dev options)
        * Turn off all useless settings (i.e., NFC, Bluetooth, location, etc.)
        * Turn off any apps running
        * Set up USB/WiFi connection
    * Computer:
        * add your device ID to the `devices.json`
        * Set up `config.json` file
        * activate virtual environment




## Useful links:
- developer options: https://developer.android.com/studio/debug/dev-options
- adb: https://developer.android.com/studio/command-line/adb
- adb logcat: https://developer.android.com/studio/command-line/logcat
- wireless connection: https://developer.android.com/tools/adb#wireless
- AndroidRunner: https://github.com/S2-group/android-runner
- apks: https://apkpure.com/
- BatteryManager-companion: https://github.com/S2-group/batterymanager-companion
- BatteryManager-companion apk: https://github.com/S2-group/batterymanager-companion/releases/tag/v1.0.0
- monkeyrunner: https://android.googlesource.com/platform/sdk/+/ics-mr0/monkeyrunner?autodive=0%2F%2F



