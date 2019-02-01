import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('rjxy', '7uuh8baa')
sta_if.isconnected()
sta_if.ifconfig()