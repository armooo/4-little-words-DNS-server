#!/usr/bin/python
from twisted.names import dns
from twisted.names import common
from twisted.names import server

from twisted.internet import defer, reactor
from twisted.python import failure

class FourLittleWordsAuthority(common.ResolverBase):

    WORDS = [
        'A', 'AID', 'ANA', 'ARC', 'AT', 'AWN', 'BAR', 'BET', 'BOG', 'BUG',
        'CAB', 'COD', 'COY', 'DAD', 'DES', 'DOE', 'DUE', 'EGO', 'ETC', 'FAT',
        'FIR', 'FUM', 'GAP', 'GIL', 'GUY', 'HAP', 'HER', 'HIT', 'HOW', 'ICY',
        'ION', 'IVY', 'JET', 'JOY', 'KIM', 'LAM', 'LEN', 'LIT', 'LOW', 'MAN',
        'MEL', 'MOD', 'MUG', 'NAY', 'NIP', 'NOV', 'OAR', 'OIL', 'ORR', 'OWL',
        'PAP', 'PEP', 'PIT', 'PRO', 'RAG', 'RED', 'RIP', 'RUB', 'SAG', 'SEA',
        'SIN', 'SO', 'SPY', 'TAD', 'TEN', 'TO', 'TOY', 'UP', 'WAG', 'WET',
        'WOW', 'YES', 'ACHE', 'ADEN', 'AIDS', 'ALLY', 'AMES', 'ANNA', 'ARGO',
        'AUNT', 'AWAY', 'BAIT', 'BAND', 'BARN', 'BAWD', 'BEAU', 'BELT',
        'BETA', 'BILL', 'BLED', 'BLUR', 'BOHR', 'BONE', 'BORE', 'BOYD',
        'BRIG', 'BULL', 'BURT', 'CAFE', 'CANE', 'CASH', 'CHAD', 'CHIN', 'CLAD',
        'CLUB', 'CODE', 'COLT', 'CORD', 'CRAG', 'CUBE', 'CURL', 'DANG', 'DATE',
        'DEAN', 'DEFY', 'DIET', 'DISH', 'DOME', 'DOUR', 'DRUB', 'DUKE', 'EACH',
        'EDDY', 'ELBA', 'EROS', 'FAIL', 'FAST', 'FELL', 'FILE', 'FISH', 'FLAT',
        'FLOW', 'FOLK', 'FORK', 'FRAY', 'FULL', 'GAGE', 'GAME', 'GAVE', 'GIBE',
        'GIST', 'GLOW', 'GOES', 'GORY', 'GREW', 'GULF', 'HAAG', 'HALO', 'HARM',
        'HAWK', 'HEED', 'HERE', 'HIKE', 'HOBO', 'HONE', 'HOST', 'HUFF', 'HURD',
        'IDEA', 'IOWA', 'JACK', 'JERK', 'JOBS', 'JOVE', 'JUNE', 'KANE', 'KERN',
        'KISS', 'KNOW', 'LACK', 'LAME', 'LATE', 'LEAK', 'LENT', 'LICK', 'LILA',
        'LINK', 'LOAM', 'LONG', 'LOST', 'LULU', 'LYLE', 'MAIL', 'MANN', 'MASH',
        'MEAD', 'MEMO', 'MILD', 'MINI', 'MOAN', 'MONA', 'MORN', 'MUDD', 'MUTT',
        'NASH', 'NEIL', 'NIBS', 'NOEL', 'NOUN', 'ODIN', 'OLIN', 'ONUS', 'OUTS',
        'QUOD', 'RAIN', 'RAYS', 'REEK', 'RICE', 'RINK', 'ROCK', 'ROOM', 'ROVE',
        'RULE', 'RUST', 'SALK', 'SAUL', 'SEAM', 'SELF', 'SHAW', 'SHOW', 'SILK',
        'SITE', 'SKIT', 'SLIM', 'SLUR', 'SOAK', 'SOME', 'SOWN', 'STIR', 'SUMS',
        'SWAN', 'TAKE', 'TEAL', 'TEND', 'THEE', 'TICK', 'TIME', 'TOIL', 'TOOT',
        'TRAM', 'TROT', 'TUNE', 'ULAN', 'VAIN', 'VEIN', 'VINE', 'WAIL', 'WANE',
        'WAST', 'WEAN', 'WENT', 'WHET', 'WINE', 'WOLF', 'WORN', 'YARN'
    ]
    WORDS_MAP = dict([(w.lower(), str(i)) for i, w in enumerate(WORDS)])
    IP_MAP = dict([(i, w) for w, i in WORDS_MAP.items()])

    def __init__(self):
        common.ResolverBase.__init__(self)

    def _lookup(self, name, cls, type, timeout = None):
        name = name.lower()

        words = name.split('.')[:4]
        if len(words) != 4:
            return defer.fail(failure.Failure(dns.AuthoritativeDomainError(name)))
        if type != dns.A:
            return defer.fail(failure.Failure(dns.AuthoritativeDomainError(name)))

        try:
            address = '.'.join([self.WORDS_MAP[word] for word in words])
        except KeyError:
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
