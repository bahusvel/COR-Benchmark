__author__ = 'denis'
from corburn import CorBurner
import cor.comm

table = {}
corburn = CorBurner(route_callback=cor.comm.static_router_factory(table))
table["BENCHMARK.MPS"] = corburn

#Manager(modules=[module("test.corburn")])
