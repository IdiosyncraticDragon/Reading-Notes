#
#   The Shops server
#

from __future__ import print_function
import Pyro4
import shop

ns = Pyro4.naming.locateNS()
daemon = Pyro4.core.Daemon()

uri = daemon.register(shop.Shop())
ns.register("example.shop.Shop", uri)

print(list(ns.list(prefix="example.shop.").keys()))

# enter the service loop.

daemon.requestLoop()
