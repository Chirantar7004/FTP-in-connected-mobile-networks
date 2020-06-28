#!/usr/bin/python

"""
Setting the position of Nodes (only for Stations and Access Points).
"""

from mininet.net import Mininet
from mininet.node import Controller,OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def topology():

    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    ## The mobile node
    sta1 = net.addStation( 'sta1', wlans=2, mac='00:00:00:00:00:02', ip='10.0.0.2/24' )
    ## The long range, poor quality access point
    ap1 = net.addAccessPoint( 'ap1', ssid= 'ap1-ssid', mode= 'g', channel= '1', position='50,50,0', range=51 )
    ## The sort range, good quality access points
    ap2 = net.addAccessPoint( 'ap2', ssid= 'ap2-ssid', mode= 'g', channel= '4', position='10,10,0', range=30 )
    ap3 = net.addAccessPoint( 'ap3', ssid= 'ap3-ssid', mode= 'g', channel= '4', position='90,10,0', range=30 )
    ap4 = net.addAccessPoint( 'ap4', ssid= 'fast-ssid', mode= 'g', channel= '4', position='50,80,0', range=10 )
    ## Controller for the APs (don't need to change this)
    c1 = net.addController( 'c1', controller=Controller )
    ## The host, will run the HTTP server in this example
    h1 = net.addHost ( 'h1', ip='10.0.0.3/24' )

    print "*** Configuring wifi nodes"
    net.configureWifiNodes()

    ## (ap2--ap3--ap4)
    print "*** Creating links"
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)

    ## Poor quality link ap1---h1
    net.addLink(ap1, h1, bw=2, delay='10ms', max_queue_size=1000)
    ## Good quality link ap2---h1 (note that ap2--ap3--ap4)
    net.addLink(ap2, h1)

    ## Just to make sure the interfaces are correctly set
    net.addLink(ap1, sta1) 
    net.addLink(ap2, sta1)

    print "*** Starting network"
    net.build()
    c1.start()
    ap1.start( [c1] )
    ap2.start( [c1] )
    ap3.start( [c1] )
    ap4.start( [c1] )

    ## Manually set a second IP for h1 and sta1
    sta1.setIP('10.1.0.2/24', intf='sta1-wlan1')
    h1.setIP('10.1.0.3/24', intf='h1-eth1')

    ## Run a simple HTTP server on h1
    print "*** Starting HTTP server on H1"
    h1.cmdPrint('python -m SimpleHTTPServer 80 &')

    """association control"""
    net.associationControl('ssf')

    """Plot graph"""
    net.plotGraph(max_x=100, max_y=100)

    """Seed"""
    net.seed(20) 

    "*** Available models: RandomWalk, TruncatedLevyWalk, RandomDirection, RandomWayPoint, GaussMarkov, ReferencePoint, TimeVariantCommunity ***"
    net.startMobility(startTime=0, model='RandomWayPoint', max_x=100, max_y=100, min_v=0.5, max_v=0.8)

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

