import random
from itertools import product


class DB(object):

    def __init__(self):

        # TAROT
        self.majors = [ '0 - The Fool',
                        'I - The Magician',
                        'II - The High Priestess',
                        'III - The Empress',
                        'IV - The Emperor',
                        'V - The Hierophant',
                        'VI - The Lovers',
                        'VII - The Chariot',
                        'VIII - Justice',
                        'IX - The Hermit',
                        'X - Wheel of Fortune',
                        'XI - Strength',
                        'XII - Hanged Man',
                        'XIII - Death',
                        'XIV - Temperance',
                        'XV - The Devil',
                        'XVI - The Tower',
                        'XVII - The Star',
                        'XVIII - The Moon',
                        'XIX - The Sun',
                        'XX - Judgment',
                        'XXI - The World'
        ]
        self.ranks = [ 'Ace of ',
                       '2 of ',
                       '3 of ',
                       '4 of ',
                       '5 of ',
                       '6 of ',
                       '7 of ',
                       '8 of ',
                       '9 of ',
                       '10 of ',
                       'Page of ',
                       'Queen of ',
                       'King of ',
                       'Knight of '
        ]
        self.suits = [ 'Wands', 'Swords', 'Pentacles', 'Cups']
        self.deck = list(r + s for r, s in product(self.ranks, self.suits))
        self.deck.extend(self.majors)

        # RUNES
        self.runes = [ 'Fehu',
                       'Uruz',
                       'Thurisaz',
                       'Ansuz',
                       'Raidho',
                       'Kenaz',
                       'Gebo',
                       'Wunjo',
                       'Hagalaz',
                       'Nauthiz',
                       'Isa',
                       'Jera',
                       'Eihwaz',
                       'Perthro',
                       'Algiz',
                       'Sowilo',
                       'Tiwaz',
                       'Berkano',
                       'Ehwaz',
                       'Mannaz',
                       'Laguz',
                       'Ingwaz',
                       'Dagaz',
                       'Othala'
        ]

        # YIJING
        self.yijing = [ 'Hexagram 1 - Qian: The Creative',
                        'Hexagram 2 - K\'un: The Receptive',
                        'Hexagram 3 - Chun: Difficult Beginnings',
                        'Hexagram 4 - Meng: Youthful Folly',
                        'Hexagram 5 - Hsu: Nourished While Waiting',
                        'Hexagram 6 - Sung: Conflict',
                        'Hexagram 7 - Shih: Army',
                        'Hexagram 8 - Pi: Uniting',
                        'Hexagram 9 - Hsiao Ch\'u: Small Restraint',
                        'Hexagram 10 - Lu: Treading',
                        'Hexagram 11 - T\'ai: Peace',
                        'Hexagram 12 - P\'i: Standstill',
                        'Hexagram 13 - T\'ung Jen: Fellowship',
                        'Hexagram 14 - Ta Yu: Great Possessing',
                        'Hexagram 15 - Qian: Authenticity',
                        'Hexagram 16 - Yu: Enthusiasm',
                        'Hexagram 17 - Sui: Following',
                        'Hexagram 18 - Ku: Decay',
                        'Hexagram 19 - Lin: Approach',
                        'Hexagram 20 - Kuan: Contemplation',
                        'Hexagram 21 - Shi Ho: Biting Through',
                        'Hexagram 22 - Bi: Grace',
                        'Hexagram 23 - Po: Split Apart',
                        'Hexagram 24 - Fu: Return',
                        'Hexagram 25 - Wu: Wang Innocence',
                        'Hexagram 26 - Ta: Ch\',u Controlled Power',
                        'Hexagram 27 - Yi: Nourishing Vision',
                        'Hexagram 28 - Ta Kuo: Critical Mass',
                        'Hexagram 29 - Kan: Abyss',
                        'Hexagram 30 - Li: Clarity',
                        'Hexagram 31 - Hsien: Influence/Wooing',
                        'Hexagram 32 - Heng: Duration',
                        'Hexagram 33 - Tun: Retreat',
                        'Hexagram 34 - Da Zhuang: Great Power',
                        'Hexagram 35 - Chin: Progress',
                        'Hexagram 36 - Ming Yi: Brightness Hiding',
                        'Hexagram 37 - Chia Jen: Family',
                        'Hexagram 38 - K’uei: Opposition',
                        'Hexagram 39 - Jian: Obstruction',
                        'Hexagram 40 - Jie: Liberation',
                        'Hexagram 41 - Sun: Decrease',
                        'Hexagram 42 - Yi: Increase',
                        'Hexagram 43 - Guai: Determination',
                        'Hexagram 44 - Gou: Coming to Meet',
                        'Hexagram 45 - Cui: Gathering Together',
                        'Hexagram 46 - Sheng: Pushing Upward',
                        'Hexagram 47 - Kun: Oppression/Exhaustion',
                        'Hexagram 48 - Jing: The Well',
                        'Hexagram 49 - Ko: Molting/Revolution',
                        'Hexagram 50 - Ting: Cauldron',
                        'Hexagram 51 - Zhen: Shocking',
                        'Hexagram 52 - Ken: Keeping Still',
                        'Hexagram 53 - Ji\'an: Development',
                        'Hexagram 54 - Kui Mei: Propriety',
                        'Hexagram 55 - Feng: Abundance',
                        'Hexagram 56 - Lu: The Wanderer',
                        'Hexagram 57 - Xun: Penetration',
                        'Hexagram 58 - Tui: Joy',
                        'Hexagram 59 - Huan: Dispersion',
                        'Hexagram 60 - Jie: Limitation',
                        'Hexagram 61 - Zhong Fu: Inner Truth',
                        'Hexagram 62 - Xiao Guo: Small Exceeding',
                        'Hexagram 63 - Chi Chi: After Completion',
                        'Hexagram 64 - Wei Chi: Before Completion',
        ]

    def tarot(self):
        deck = []
        deck += self.deck
        for i in range(len(deck)):
            if random.randint(1, 100) >= 50:
                deck[i] += ' [REVERSED]'
            else:
                pass
        random.shuffle(deck)
        return deck
        del deck

    def get(self, **kwargs):
        deck = self.tarot()
        if kwargs['type'] == 'tarot':
            if kwargs['amt'] >= 2:
                return ' / '.join(random.sample(deck, kwargs['amt']))
            return random.choice(deck)
        elif kwargs['type'] == 'rune':
            if kwargs['amt'] >= 2:
                return ' / '.join(random.sample(self.runes, kwargs['amt']))
            return random.choice(self.runes)
        elif kwargs['type'] == 'yijing':
            return random.choice(self.yijing)

