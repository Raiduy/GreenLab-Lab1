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

# AndroidRunner how does it work? (15 min)
* Files
    * config files
        * `run_stopping_condition`
        * `usb_handler` + caveats (RasPI 4B)
    * script files
    * interaction files
    * output files
    * `--progress` flag
* Profilers
    * BatteryManager (with companion)
    * Read the [BatteryManager README](https://github.com/S2-group/android-runner/tree/master/AndroidRunner/Plugins/batterymanager#readme)
    * Troubleshooting BatteryManager

# AndroidRunner demo (15 min)
* FORK [AndroidRunner](https://github.com/S2-group/android-runner)
* Install AndroidRunner
* [Before experiment checklist](./resources/android_exeriment_checklist.md)

# ExperimentRunner demo (15 min)
* FORK [ExperimentRunner](https://github.com/S2-group/experiment-runner)
* Install ExperimentRunner
* Install [PowerJoular](https://gitlab.com/joular/powerjoular) (will provide you energy data)
* Read the PowerJoular README in ExperimentRunner ([here](https://github.com/S2-group/experiment-runner/tree/master/examples/linux-powerjoular-profiling))



# Useful links
## AndroidRunner
- developer options: https://developer.android.com/studio/debug/dev-options
- adb: https://developer.android.com/studio/command-line/adb
- adb logcat: https://developer.android.com/studio/command-line/logcat
- wireless connection: https://developer.android.com/tools/adb#wireless
- AndroidRunner: https://github.com/S2-group/android-runner
- apks: https://apkpure.com/
- BatteryManager-companion: https://github.com/S2-group/batterymanager-companion
- BatteryManager-companion apk: https://github.com/S2-group/batterymanager-companion/releases/tag/v1.0.0
- monkeyrunner: https://android.googlesource.com/platform/sdk/+/ics-mr0/monkeyrunner?autodive=0%2F%2F

## ExperimentRunner

