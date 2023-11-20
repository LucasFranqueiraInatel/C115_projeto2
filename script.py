from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink


def custom_topology():
    "Create custom topology in Mininet."

    # Initialize the network
    net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)

    # Add a controller
    c0 = net.addController('c0')

    # Add hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5')
    h6 = net.addHost('h6')
    h7 = net.addHost('h7')
    h8 = net.addHost('h8')
    h9 = net.addHost('h9')

    # Add switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    # Add links between switches and hosts
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, s2)
    net.addLink(h3, s2)
    net.addLink(s2, s3)
    net.addLink(h4, s2)
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    net.addLink(s3, s4)
    net.addLink(h7, s4)
    net.addLink(h8, s4)
    net.addLink(s4, h9)

    # Start the network
    net.start()

    # Run CLI (Command Line Interface)
    CLI(net)

    # Stop the network
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    custom_topology()