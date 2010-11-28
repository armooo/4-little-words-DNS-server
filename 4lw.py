#!/usr/bin/python
from twisted.names import dns
from twisted.names import common
from twisted.names import server

from twisted.internet import defer, reactor
from twisted.python import failure

import convert_4lw

class FourLittleWordsAuthority(common.ResolverBase):

    def __init__(self):
        common.ResolverBase.__init__(self)

    def _lookup(self, name, cls, type, timeout = None):
        
        if type != dns.A:
            return defer.fail(failure.Failure(dns.AuthoritativeDomainError(name)))

        try:
            address = convert_4lw.from_4lw(name)
        except convert_4lw.FourLittleWordsError:
            return defer.fail(failure.Failure(dns.AuthoritativeDomainError(name)))

        results = []
        rec = dns.Record_A(address)
        results.append(dns.RRHeader(name, dns.A, dns.IN, 60*60*24, rec, auth=True))

        return defer.succeed((results, [], []))

def main():
    dns_factory = server.DNSServerFactory(verbose=True, authorities=[FourLittleWordsAuthority()])
    dns_protocol = dns.DNSDatagramProtocol(dns_factory)
    reactor.listenUDP(53, dns_protocol)
    reactor.run()

if __name__ == '__main__':
    main()
