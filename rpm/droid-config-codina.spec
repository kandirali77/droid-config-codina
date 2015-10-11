# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device codina
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Ace2 GT-I8160

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 1.5

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc
