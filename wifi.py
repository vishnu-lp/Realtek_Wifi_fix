import os

a = 'sudo ip link set'
b = 'up'
os.system('iwconfig')
device = raw_input('enter your device designation\n')
os.chdir('rtlwifi_new')
os.system('make')
os.system('sudo make install')
os.system('sudo modprobe -rv rtl8723be')
os.system('sudo modprobe -v rtl8723be ant_sel=2')

os.system('%s %s %s' %(a, device, b))
os.system('echo "options rtl8723be ant_sel=2" | sudo tee /etc/modprobe.d/50-rtl8723be.conf')
