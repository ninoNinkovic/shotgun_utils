import subprocess

sg_plugin = "./npShotgunIntegration.dll"
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

# Register SG Chrome plugin
subprocess.call(["regsvr32", "/s", sg_plugin])

# Run Chrome
subprocess.call([chrome_path])