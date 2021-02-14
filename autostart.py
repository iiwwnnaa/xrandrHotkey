import os

##############################################################################################
################################ xrandrHotkey AUTOSTART ######################################
##############################################################################################
########## Add this ===> python <Location of xrandrHotkey folder>/autostart.py <=== ##########
############################ on .xinitrc(Xorg) or i3 config files. ###########################
###################### AND YOU MUST CHECK UNDER COMMENT ######################################
##############################################################################################
##############################################################################################

sudoPassword = '' # Write your sudo password for autostart, If password is incorrect it dosen't work
location = '' # Write xrandrHotkey folder location, e.g. /home/blahblah/xranderHotkey

# DONT TOUCH
os.popen(f"sudo -S python {location}/xrandrHotkey.py", 'w').write(sudoPassword)