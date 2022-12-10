# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device ocean
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty G7 Power

# Community HW adaptations need this
%define community_adaptation 1

%define dcd_path ./

# Sailfish OS is considered to-scale, if in the App Grid you get 4-in-a-row icons,
# and 2-in-a-row or 3-in-a-row app covers in the Home Screen, depending on
# how many apps are open.
# For 4-5.5" device screen sizes of 16:9 ratio, use this formula (hold portrait):
# pixel_ratio = 4.5/DiagonalDisplaySizeInches * HorizontalDisplayResolution/540
# Other screen sizes and ratios will require more trial-and-error.
%define pixel_ratio 1.75

 We assume most devices will
%define have_modem 1

# For building 17.1
%define android_version_major 10

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-ocean.inc
%include patterns/patterns-sailfish-device-configuration-ocean.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

