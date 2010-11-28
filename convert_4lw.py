#Old word
WORDS = [
    'A', 'AID', 'ANA', 'ARC', 'AT', 'AWN', 'BAR', 'BET', 'BOG', 'BUG', 'CAB',
    'COD', 'COY', 'DAD', 'DES', 'DOE', 'DUE', 'EGO', 'ETC', 'FAT', 'FIR',
    'FUM', 'GAP', 'GIL', 'GUY', 'HAP', 'HER', 'HIT', 'HOW', 'ICY', 'ION',
    'IVY', 'JET', 'JOY', 'KIM', 'LAM', 'LEN', 'LIT', 'LOW', 'MAN', 'MEL',
    'MOD', 'MUG', 'NAY', 'NIP', 'NOV', 'OAR', 'OIL', 'ORR', 'OWL', 'PAP',
    'PEP', 'PIT', 'PRO', 'RAG', 'RED', 'RIP', 'RUB', 'SAG', 'SEA', 'SIN', 'SO',
    'SPY', 'TAD', 'TEN', 'TO', 'TOY', 'UP', 'WAG', 'WET', 'WOW', 'YES', 'ACHE',
    'ADEN', 'AIDS', 'ALLY', 'AMES', 'ANNA', 'ARGO', 'AUNT', 'AWAY', 'BAIT',
    'BAND', 'BARN', 'BAWD', 'BEAU', 'BELT', 'BETA', 'BILL', 'BLED', 'BLUR',
    'BOHR', 'BONE', 'BORE', 'BOYD', 'BRIG', 'BULL', 'BURT', 'CAFE', 'CANE',
    'CASH', 'CHAD', 'CHIN', 'CLAD', 'CLUB', 'CODE', 'COLT', 'CORD', 'CRAG',
    'CUBE', 'CURL', 'DANG', 'DATE', 'DEAN', 'DEFY', 'DIET', 'DISH', 'DOME',
    'DOUR', 'DRUB', 'DUKE', 'EACH', 'EDDY', 'ELBA', 'EROS', 'FAIL', 'FAST',
    'FELL', 'FILE', 'FISH', 'FLAT', 'FLOW', 'FOLK', 'FORK', 'FRAY', 'FULL',
    'GAGE', 'GAME', 'GAVE', 'GIBE', 'GIST', 'GLOW', 'GOES', 'GORY', 'GREW',
    'GULF', 'HAAG', 'HALO', 'HARM', 'HAWK', 'HEED', 'HERE', 'HIKE', 'HOBO',
    'HONE', 'HOST', 'HUFF', 'HURD', 'IDEA', 'IOWA', 'JACK', 'JERK', 'JOBS',
    'JOVE', 'JUNE', 'KANE', 'KERN', 'KISS', 'KNOW', 'LACK', 'LAME', 'LATE',
    'LEAK', 'LENT', 'LICK', 'LILA', 'LINK', 'LOAM', 'LONG', 'LOST', 'LULU',
    'LYLE', 'MAIL', 'MANN', 'MASH', 'MEAD', 'MEMO', 'MILD', 'MINI', 'MOAN',
    'MONA', 'MORN', 'MUDD', 'MUTT', 'NASH', 'NEIL', 'NIBS', 'NOEL', 'NOUN',
    'ODIN', 'OLIN', 'ONUS', 'OUTS', 'QUOD', 'RAIN', 'RAYS', 'REEK', 'RICE',
    'RINK', 'ROCK', 'ROOM', 'ROVE', 'RULE', 'RUST', 'SALK', 'SAUL', 'SEAM',
    'SELF', 'SHAW', 'SHOW', 'SILK', 'SITE', 'SKIT', 'SLIM', 'SLUR', 'SOAK',
    'SOME', 'SOWN', 'STIR', 'SUMS', 'SWAN', 'TAKE', 'TEAL', 'TEND', 'THEE',
    'TICK', 'TIME', 'TOIL', 'TOOT', 'TRAM', 'TROT', 'TUNE', 'ULAN', 'VAIN',
    'VEIN', 'VINE', 'WAIL', 'WANE', 'WAST', 'WEAN', 'WENT', 'WHET', 'WINE',
    'WOLF', 'WORN', 'YARN'
]
WORDS_MAP = dict([(w.lower(), str(i)) for i, w in enumerate(WORDS)])

#New mad libs style
ADJECTIVE_LIST = [
    'able', 'academic', 'active', 'actual', 'additional', 'afraid', 'alone',
    'ancient', 'annual', 'apparent', 'attractive', 'available', 'average',
    'aware', 'bad', 'basic', 'beautiful', 'big', 'black', 'bloody', 'blue',
    'brief', 'bright', 'broad', 'busy', 'capable', 'careful', 'central',
    'certain', 'cheap', 'chief', 'civil', 'clean', 'clear', 'close', 'cold',
    'commercial', 'common', 'complete', 'complex', 'concerned', 'constant',
    'corporate', 'correct', 'criminal', 'critical', 'cultural', 'current',
    'dangerous', 'dark', 'dead', 'deep', 'democratic', 'detailed', 'different',
    'difficult', 'direct', 'domestic', 'double', 'dry', 'due', 'early', 'easy',
    'economic', 'effective', 'elderly', 'empty', 'entire', 'equal',
    'essential', 'excellent', 'existing', 'expensive', 'external', 'extra',
    'fair', 'familiar', 'famous', 'far', 'fast', 'female', 'final',
    'financial', 'fine', 'first', 'following', 'foreign', 'formal', 'free',
    'fresh', 'front', 'full', 'funny', 'future', 'general', 'good', 'great',
    'green', 'grey', 'growing', 'happy', 'hard', 'heavy', 'high', 'historical',
    'hot', 'huge', 'human', 'immediate', 'important', 'impossible',
    'increased', 'individual', 'industrial', 'initial', 'interested',
    'internal', 'joint', 'key', 'labor', 'large', 'last', 'late', 'leading',
    'left', 'legal', 'liberal', 'light', 'likely', 'limited', 'little',
    'living', 'local', 'long', 'lovely', 'low', 'main', 'major', 'male',
    'married', 'medical', 'mental', 'military', 'modern', 'narrow', 'national',
    'natural', 'necessary', 'new', 'nice', 'normal', 'northern', 'nuclear',
    'obvious', 'odd', 'official', 'old', 'only', 'open', 'ordinary',
    'original', 'other', 'overall', 'particular', 'perfect', 'permanent',
    'personal', 'physical', 'political', 'poor', 'popular', 'positive',
    'possible', 'potential', 'powerful', 'practical', 'present', 'previous',
    'primary', 'prime', 'private', 'proper', 'public', 'purple', 'quick',
    'quiet', 'rare', 'ready', 'real', 'recent', 'red', 'regional', 'regular',
    'relative', 'relevant', 'religious', 'rich', 'right', 'royal', 'rural',
    'safe', 'secondary', 'senior', 'separate', 'serious', 'severe', 'short',
    'similar', 'simple', 'sinful', 'single', 'slow', 'small', 'social', 'soft',
    'sorry', 'southern', 'special', 'specific', 'standard', 'strange',
    'strong', 'suitable', 'sure', 'tall', 'technical', 'terrible', 'thin',
    'tiny', 'top', 'total', 'true', 'typical', 'unable', 'united', 'unlikely',
    'upper', 'urban', 'used', 'useful', 'usual', 'various', 'vast', 'very',
    'vital', 'warm', 'weak', 'western', 'white', 'whole', 'wide', 'wild',
    'wonderful', 'working', 'wrong', 'young'
]

NOUN_LIST = [
    'acid', 'actor', 'adult', 'age', 'agent', 'aid', 'aim', 'air', 'area',
    'arm', 'army', 'art', 'asset', 'award', 'baby', 'back', 'bag', 'ball',
    'band', 'bank', 'bar', 'base', 'basis', 'bed', 'bill', 'bird', 'birth',
    'bit', 'block', 'blood', 'board', 'boat', 'body', 'bone', 'book', 'box',
    'boy', 'brain', 'bus', 'call', 'cape', 'car', 'card', 'case', 'cash',
    'cat', 'cause', 'cell', 'chain', 'city', 'club', 'coal', 'cod', 'code',
    'copy', 'couple', 'cup', 'dare', 'data', 'day', 'deal', 'debt', 'desk',
    'dog', 'door', 'drug', 'duty', 'ear', 'edge', 'eel', 'egg', 'end', 'eye',
    'face', 'fact', 'fall', 'farm', 'fear', 'fee', 'file', 'film', 'finger',
    'fire', 'firm', 'fish', 'flat', 'flow', 'food', 'foot', 'form', 'fuel',
    'fund', 'game', 'gas', 'gate', 'girl', 'goal', 'god', 'gold', 'good',
    'gun', 'hair', 'half', 'hall', 'hand', 'head', 'heat', 'hell', 'help',
    'hill', 'hole', 'home', 'hope', 'hour', 'idea', 'iron', 'item', 'job',
    'kid', 'kind', 'king', 'kit', 'knee', 'lack', 'lady', 'land', 'law',
    'lead', 'leaf', 'leg', 'life', 'line', 'link', 'lip', 'list', 'loan',
    'look', 'lord', 'loss', 'lot', 'love', 'man', 'map', 'mask', 'mass',
    'mate', 'meal', 'mile', 'milk', 'mind', 'mine', 'move', 'name', 'neck',
    'need', 'news', 'node', 'nose', 'oil', 'page', 'pain', 'pair', 'park',
    'part', 'past', 'path', 'pay', 'plan', 'play', 'pool', 'post', 'pub',
    'rabbit', 'race', 'rain', 'rate', 'rest', 'ring', 'rise', 'risk', 'road',
    'rock', 'role', 'roof', 'room', 'rule', 'run', 'sale', 'sea', 'seal',
    'seat', 'ship', 'shoe', 'shop', 'shot', 'show', 'side', 'sign', 'sin',
    'sir', 'site', 'size', 'skin', 'sky', 'soil', 'son', 'song', 'sort',
    'spot', 'star', 'step', 'sum', 'sun', 'table', 'tape', 'task', 'tax',
    'tea', 'team', 'tear', 'term', 'text', 'time', 'ton', 'tone', 'tool',
    'top', 'tour', 'town', 'tree', 'trip', 'turtle', 'type', 'unit', 'user',
    'vest', 'view', 'vote', 'wage', 'walk', 'wall', 'war', 'wave', 'way',
    'week', 'wife', 'wind', 'wine', 'wing', 'woman', 'wood', 'word', 'yard',
    'yarn', 'year', 'zebra'
]

VERB_LIST = [
    'accepts', 'acts', 'adds', 'admits', 'adopts', 'advises', 'affects',
    'affords', 'agrees', 'aims', 'allows', 'answers', 'appeals', 'appears',
    'applies', 'argues', 'arises', 'arrives', 'asks', 'assesses', 'assumes',
    'attaches', 'attacks', 'attends', 'avoids', 'awards', 'bases', 'bears',
    'beats', 'becomes', 'begins', 'belongs', 'bends', 'binds', 'blows',
    'breaks', 'brings', 'builds', 'burns', 'buys', 'calls', 'cares', 'carries',
    'catches', 'causes', 'changes', 'charges', 'checks', 'chooses', 'claims',
    'clears', 'climbs', 'closes', 'comes', 'commits', 'costs', 'counts',
    'covers', 'creates', 'cries', 'crosses', 'cuts', 'damages', 'dates',
    'deals', 'decides', 'defines', 'demands', 'denies', 'depends', 'derives',
    'designs', 'dies', 'directs', 'divides', 'does', 'draws', 'dresses',
    'drinks', 'drives', 'drops', 'earns', 'eats', 'emerges', 'employs',
    'enables', 'ends', 'enjoys', 'ensures', 'enters', 'exists', 'faces',
    'fails', 'falls', 'fears', 'feels', 'fights', 'fills', 'finds', 'fits',
    'fixes', 'flies', 'focuses', 'forces', 'forms', 'gains', 'gets', 'gives',
    'goes', 'grants', 'grows', 'hands', 'hangs', 'has', 'hates', 'heads',
    'hears', 'helps', 'hides', 'hits', 'holds', 'hopes', 'hurts', 'implies',
    'issues', 'joins', 'judges', 'jumps', 'keeps', 'kills', 'knows', 'lasts',
    'laughs', 'lays', 'leads', 'leans', 'learns', 'leaves', 'lets', 'lies',
    'lifts', 'likes', 'limits', 'links', 'lives', 'looks', 'loses', 'loves',
    'makes', 'marks', 'marries', 'matches', 'means', 'meets', 'minds',
    'misses', 'moves', 'nags', 'needs', 'nods', 'notes', 'occurs', 'offers',
    'opens', 'orders', 'owns', 'paints', 'passes', 'pays', 'picks', 'places',
    'plans', 'plays', 'points', 'presses', 'proves', 'pulls', 'pushes', 'puts',
    'raises', 'reaches', 'reads', 'refers', 'relies', 'replies', 'rests',
    'rides', 'rings', 'rises', 'rolls', 'runs', 'saves', 'says', 'scores',
    'seeks', 'seems', 'sees', 'sells', 'sends', 'serves', 'sets', 'shakes',
    'shares', 'shoots', 'shouts', 'shows', 'shut', 'signs', 'sings', 'sits',
    'sleeps', 'slips', 'smiles', 'sorts', 'sounds', 'speaks', 'spends',
    'stands', 'stars', 'starts', 'states', 'stays', 'steals', 'sticks',
    'stops', 'studies', 'takes', 'talks', 'teach', 'tells', 'tends', 'tests',
    'thanks', 'thinks', 'throws', 'touches', 'trains', 'treats', 'tries',
    'turns', 'uses', 'varies', 'visits', 'votes', 'waits', 'walks', 'wants',
    'warns', 'washes', 'watches', 'wears', 'wins', 'wishes', 'works',
    'worries', 'writes'
]

ADJECTIVES = dict([(w.lower(), str(i)) for i, w in enumerate(ADJECTIVE_LIST)])
ADJECTIVES_BACK = dict([(str(i), w.lower()) for i, w in enumerate(ADJECTIVE_LIST)])
NOUNS = dict([(w.lower(), str(i)) for i, w in enumerate(NOUN_LIST)])
NOUNS_BACK = dict([(str(i), w.lower()) for i, w in enumerate(NOUN_LIST)])
VERBS = dict([(w.lower(), str(i)) for i, w in enumerate(VERB_LIST)])
VERBS_BACK = dict([(str(i), w.lower()) for i, w in enumerate(VERB_LIST)])

class FourLittleWordsError(Exception):
    pass

def to_4lw(ip):
    result = []
    quads = ip.split('.')
    try:
        result.append(ADJECTIVES_BACK[str(int(quads[0]))])
        result.append(NOUNS_BACK[str(int(quads[1]))])
        result.append(VERBS_BACK[str(int(quads[2]))])
        result.append(NOUNS_BACK[str(int(quads[3]))])
    except (KeyError, ValueError):
        raise FourLittleWordsError()
    return '.'.join(result)

def from_4lw(name):
    words = name.lower().split('.')[:4]
    if len(words) != 4:
        raise FourLittleWordsError()
    if words[0] in WORDS_MAP:
        try:
            return '.'.join([WORDS_MAP[word] for word in words])
        except KeyError:
            raise FourLittleWordsError()
    elif words[0] in ADJECTIVES:
        address = []
        try:
            address.append(ADJECTIVES[words[0]])
            address.append(NOUNS[words[1]])
            address.append(VERBS[words[2]])
            address.append(NOUNS[words[3]])
        except KeyError:
            raise FourLittleWordsError()
        return '.'.join(address)
    else:
        raise FourLittleWordsError()
