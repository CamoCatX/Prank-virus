import ctypes

MessageBox = ctypes.windll.user32.MessageBoxW

MessageBox(None, "Error Detected. Scan?", "Computer", 0x40 | 0x4)

MessageBox(None, "Error 204. Please contact Microsoft help.", "Error 204", 0x30 | 0x1)

MessageBox(None, "Harmful program has been detected. Do you want to delete?", "Windows Security", 0x30 | 0x3)

MessageBox(None, "Unable to delete", "Windows Security", 0x30 | 0x5)

MessageBox(None, "Virus is activated", "Windows Security", 0x30 | 0x0)

MessageBox(None, "Harmful program 'onyx.exe' has gained permissions to public and private network(s) firewalls. Remove permissions?", "Windows Firewall", 0x30 | 0x10)

MessageBox(None, "DELETING SYSTEM FILES", "0NYX", 0x40 | 0x1)

MessageBox(None, "000100010111110111110111110111011000000", "ONYX", 0x40 | 0x13)

MessageBox(None, "File Transfer completed", "File Explorer", 0x40 | 0x1)

MessageBox(None, "User not recognized, signing out", ".exe", 0x40 | 0x0)

MessageBox(None, "This was a prank, HA HA. You must be more careful what you click on though.", "PRANK!", 0x40 | 0x1)

import webbrowser

webbrowser.open("https://www.sonicwall.com/phishing-iq-test-landing/")
