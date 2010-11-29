#!/usr/bin/python
import sys
import getopt

from twisted.names import dns
from twisted.names import common
from twisted.names import server
from twisted.names import authority

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

class AuthoritativeDomainErrorAsDomainError(common.ResolverBase):
    def __init__(self, resolver):
        common.ResolverBase.__init__(self)
        self.resolver = resolver

    def _check_for_empty(self, f, name):
        f.trap(dns.AuthoritativeDomainError)
        return failure.Failure(dns.DomainError(name))

    def _lookup(self, name, cls, type, timeout):
        q = dns.Query(name, type, cls)
        d = self.resolver.query(q, timeout)
        d = d.addErrback(self._check_for_empty, name)
        return d

def main(pyzones):

    authorities = []
    for pyzone in pyzones:
        a = authority.PySourceAuthority(pyzone)
        # We have 2 authorities for the same zone. The ResolverChain will stop
        # at the first AuthoritativeDomainError, because the authoritative
        # zone could not find the record. But we have 2 authoritative zones so
        # we need to trick it to keep going.
        a = AuthoritativeDomainErrorAsDomainError(a)
        authorities.append(a)
    authorities.append(FourLittleWordsAuthority())

    dns_factory = server.DNSServerFactory(authorities=authorities)
    dns_protocol = dns.DNSDatagramProtocol(dns_factory)
    reactor.listenUDP(53, dns_protocol)
    reactor.run()

def usage():
    print '4lw.py [-z <pyzone file>]'
    print 'The pyzone format can be seen at '\
    'http://twistedmatrix.com/documents/current/names/howto/names.html#auto1'

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hz:')
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    pyzones = []

    for o, a in opts:
        if o == '-h':
            usage()
            sys.exit(1)
        elif o == '-z':
            pyzones.append(a)

    main(pyzones)
