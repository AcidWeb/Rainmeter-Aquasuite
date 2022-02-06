import time
import mmap
import winreg
import xml.etree.ElementTree as ET

SHM_HANDLE = 'Rainmeter'
REFRESH_DELAY = 1

rootkey = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, 'Software')
appkey = winreg.CreateKey(rootkey, 'RainmeterAquasuite')
winreg.CloseKey(appkey)
winreg.CloseKey(rootkey)
regkey = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, 'Software\RainmeterAquasuite', 0, winreg.KEY_SET_VALUE)

while True:
    with mmap.mmap(-1, 4096, SHM_HANDLE, mmap.ACCESS_READ) as shm:
        payload = shm.read().decode('utf-8-sig').rstrip('\x00')
        if len(payload) > 0:
            try:
                document = ET.fromstring(payload)
            except ET.ParseError:
                continue
            for dataset in document.findall('Logdata/LogDataSet'):
                if dataset[1].text == 'NaN':
                    break
                label = str(dataset[2].text)
                unit = str(dataset[3].text).replace('°', '')
                value = round(float(dataset[1].text))
                winreg.SetValueEx(regkey, f'{label} {unit}', 0, winreg.REG_SZ, str(value))
    time.sleep(REFRESH_DELAY)