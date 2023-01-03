from stock_objects import StockObjList,StockObject
global StockObjList





class SOBJMagicLockpick(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicLockpick"
        self.pName = "Magical Lockpicks"
        self.loop = 0
        self.pBaseView = 52550
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 257
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 1
        self.pWeight = 1

        self.bases.append("BKey")
        self.pLockValue = 0
        self.pUnlockValue = 0
        self.pSkeletonLock = 0
        self.pSkeletonUnlock = 0

        self.bases.append("BDescribed")

class SOBJRobeOfDefense(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RobeOfDefense"
        self.pName = "Mage's Robe"
        self.loop = 0
        self.pBaseView = 11500
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 98
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 11

        self.bases.append("BWearable")
        self.pLayer = 50
        self.pAreaWorn = 2
        self.pMask = -19203

        self.bases.append("BDescribed")

class SOBJMagicChainPants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicChainPants"
        self.pName = "Enchanted Chain Pants"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 170

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMagicChainTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicChainTunic"
        self.pName = "Enchanted Chain Tunic"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 180

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJMagicChainCowl(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicChainCowl"
        self.pName = "Enchanted Chain Cowl"
        self.loop = 0
        self.pBaseView = 13500
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 40

        self.bases.append("BWearable")
        self.pLayer = 70
        self.pAreaWorn = 3
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJEnchantedBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "EnchantedBoots"
        self.pName = "Enchanted High Boots"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 99
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BWearable")
        self.pLayer = 20
        self.pAreaWorn = 7
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJEnchantedShield(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "EnchantedShield"
        self.pName = "Enchanted Shield"
        self.loop = 0
        self.pBaseView = 16800
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 64
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 150

        self.bases.append("BWearable")
        self.pLayer = 5
        self.pAreaWorn = 17
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMagicPlatePants(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicPlatePants"
        self.pName = "Enchanted Plate Pants"
        self.loop = 0
        self.pBaseView = 13700
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 270

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 6
        self.pMask = -1

        self.bases.append("BDescribed")

class SOBJMagicPlateTunic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "MagicPlateTunic"
        self.pName = "Enchanted Plate Tunic"
        self.loop = 0
        self.pBaseView = 13600
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 63
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 300

        self.bases.append("BWearable")
        self.pLayer = 10
        self.pAreaWorn = 1
        self.pMask = -16385

        self.bases.append("BDescribed")

class SOBJOrbOfHealing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OrbOfHealing"
        self.pName = "Orb"
        self.pIDName = "Orb of Healing (defunct)"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJOrbOfInvisibility(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OrbOfInvisibility"
        self.pName = "Orb"
        self.pIDName = "Orb of Invisibility (defunct)"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJOrbOfLightning(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OrbOfLightning"
        self.pName = "Orb"
        self.pIDName = "Orb of Lightning (defunct)"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJOrbOfMana(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OrbOfMana"
        self.pName = "Orb"
        self.pIDName = "Orb of Mana (defunct)"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 72


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BUse")
        self.pVerb = 0
        self.pSpell = -1
        self.pTheurgism = 0

class SOBJSkillbook(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Skillbook"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbBasketWeaving(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbBasketWeaving"
        self.pName = "The Basics of Basketweaving"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

class SOBJskbPsychology(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbPsychology"
        self.pName = "Psychology of a Realm Player"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

class SOBJskbFriends(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbFriends"
        self.pName = "Making Friends and Being Polite in the Realm"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

class SOBJskbShortSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShortSword"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShortSwordI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShortSwordI"
        self.pName = "Familiarity with Short Swords"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShortSwordII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShortSwordII"
        self.pName = "Short Sword Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShortSwordIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShortSwordIII"
        self.pName = "Short Sword Expertise"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShortSwordIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShortSwordIV"
        self.pName = "The Master's Book of Short Swords"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShortSwordV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShortSwordV"
        self.pName = "Short Sword Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLongSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLongSword"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLongSwordI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLongSwordI"
        self.pName = "Familiarity with Long Swords"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLongSwordII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLongSwordII"
        self.pName = "Long Sword Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLongSwordIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLongSwordIII"
        self.pName = "Expertise with Long Swords"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLongSwordIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLongSwordIV"
        self.pName = "Long Sword Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLongSwordV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLongSwordV"
        self.pName = "Long Sword Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTwoHandedSword(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTwoHandedSword"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTwoHandedSwordI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTwoHandedSwordI"
        self.pName = "Familiarity with Two-Handed Swords"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTwoHandedSwordII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTwoHandedSwordII"
        self.pName = "Two-Handed Sword Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTwoHandedSwordIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTwoHandedSwordIII"
        self.pName = "Expertise with Two-Handed Swords"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTwoHandedSwordIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTwoHandedSwordIV"
        self.pName = "Two-Handed Sword Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTwoHandedSwordV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTwoHandedSwordV"
        self.pName = "Two-Handed Sword Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbDagger"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbDaggerI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbDaggerI"
        self.pName = "Familiarity with Daggers"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbDaggerII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbDaggerII"
        self.pName = "Dagger Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbDaggerIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbDaggerIII"
        self.pName = "Expertise with Daggers"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbDaggerIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbDaggerIV"
        self.pName = "Dagger Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbDaggerV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbDaggerV"
        self.pName = "Dagger Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAxe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAxe"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAxeI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAxeI"
        self.pName = "Familiarity with Axes"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAxeII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAxeII"
        self.pName = "Axe Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAxeIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAxeIII"
        self.pName = "Expertise with Axes"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAxeIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAxeIV"
        self.pName = "Axe Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAxeV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAxeV"
        self.pName = "Axe Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbClub(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbClub"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbClubI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbClubI"
        self.pName = "Familiarity with Clubs"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbClubII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbClubII"
        self.pName = "Club Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbClubIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbClubIII"
        self.pName = "Expertise with Clubs"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbClubIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbClubIV"
        self.pName = "Club Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbClubV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbClubV"
        self.pName = "Club Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMace(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMace"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaceI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaceI"
        self.pName = "Familiarity with Maces"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaceII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaceII"
        self.pName = "Mace Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaceIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaceIII"
        self.pName = "Expertise with Maces"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaceIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaceIV"
        self.pName = "Mace Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaceV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaceV"
        self.pName = "Mace Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbUnarmedCombat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbUnarmedCombat"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbUnarmedCombatI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbUnarmedCombatI"
        self.pName = "Familiarity with Unarmed Combat"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbUnarmedCombatII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbUnarmedCombatII"
        self.pName = "Unarmed Combat Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbUnarmedCombatIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbUnarmedCombatIII"
        self.pName = "Expertise with Unarmed Combat"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbUnarmedCombatIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbUnarmedCombatIV"
        self.pName = "Unarmed Combat Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbUnarmedCombatV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbUnarmedCombatV"
        self.pName = "Unarmed Combat Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThrowingWeapon(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThrowingWeapon"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThrowingWeaponI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThrowingWeaponI"
        self.pName = "Familiarity with Throwing Weapons"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThrowingWeaponII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThrowingWeaponII"
        self.pName = "Throwing Weapon Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThrowingWeaponIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThrowingWeaponIII"
        self.pName = "Expertise with Throwing Weapons"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThrowingWeaponIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThrowingWeaponIV"
        self.pName = "Throwing Weapon Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThrowingWeaponV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThrowingWeaponV"
        self.pName = "Throwing Weapon Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAcrobatic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAcrobatic"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAcrobaticI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAcrobaticI"
        self.pName = "Familiarity with Acrobatics"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAcrobaticII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAcrobaticII"
        self.pName = "Acrobatic Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAcrobaticIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAcrobaticIII"
        self.pName = "Expertise with Acrobatics"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAcrobaticIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAcrobaticIV"
        self.pName = "Acrobatic Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAcrobaticV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAcrobaticV"
        self.pName = "Acrobatic Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaul"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaulI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaulI"
        self.pName = "Familiarity with Mauls"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaulII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaulII"
        self.pName = "Maul Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaulIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaulIII"
        self.pName = "Expertise with Mauls"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaulIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaulIV"
        self.pName = "Maul Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMaulV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMaulV"
        self.pName = "Maul Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbSorcery(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbSorcery"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbSorceryI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbSorceryI"
        self.pName = "Familiar Sorceries"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbSorceryII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbSorceryII"
        self.pName = "Sorcery Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbSorceryIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbSorceryIII"
        self.pName = "Expert Sorceries"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbSorceryIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbSorceryIV"
        self.pName = "Sorcery Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbSorceryV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbSorceryV"
        self.pName = "Sorcery Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbElementalism(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbElementalism"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbElementalismI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbElementalismI"
        self.pName = "Familiar Elemental Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbElementalismII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbElementalismII"
        self.pName = "Elementalism Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbElementalismIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbElementalismIII"
        self.pName = "Expert Elemental Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbElementalismIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbElementalismIV"
        self.pName = "Elementalism Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbElementalismV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbElementalismV"
        self.pName = "Elementalism Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMysticism(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMysticism"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMysticismI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMysticismI"
        self.pName = "Familiar Mystic Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMysticismII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMysticismII"
        self.pName = "Mysticism Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMysticismIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMysticismIII"
        self.pName = "Expert Mystic Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMysticismIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMysticismIV"
        self.pName = "Mysticism Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMysticismV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMysticismV"
        self.pName = "Mysticism Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThaumaturgy(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThaumaturgy"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThaumaturgyI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThaumaturgyI"
        self.pName = "Familiar Thaumaturgical Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThaumaturgyII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThaumaturgyII"
        self.pName = "Thaumaturgy Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThaumaturgyIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThaumaturgyIII"
        self.pName = "Expert Thaumaturgical Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThaumaturgyIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThaumaturgyIV"
        self.pName = "Thaumaturgy Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbThaumaturgyV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbThaumaturgyV"
        self.pName = "Thaumaturgy Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbNecromancy(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbNecromancy"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbNecromancyI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbNecromancyI"
        self.pName = "Familiar Necromancy Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbNecromancyII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbNecromancyII"
        self.pName = "Necromancy Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbNecromancyIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbNecromancyIII"
        self.pName = "Expert Necromancy Spells"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbNecromancyIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbNecromancyIV"
        self.pName = "Necromancy Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbNecromancyV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbNecromancyV"
        self.pName = "Necromancy Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTheurgism(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTheurgism"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTheurgismI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTheurgismI"
        self.pName = "Familiar Theurgism"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTheurgismII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTheurgismII"
        self.pName = "Theurgism Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTheurgismIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTheurgismIII"
        self.pName = "Theurgism Expertise"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTheurgismIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTheurgismIV"
        self.pName = "Theurgism Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTheurgismV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTheurgismV"
        self.pName = "Theurgism Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAlchemy(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAlchemy"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAlchemyI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAlchemyI"
        self.pName = "Familiar Alchemy"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAlchemyII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAlchemyII"
        self.pName = "Alchemy Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAlchemyIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAlchemyIII"
        self.pName = "Alchemy Expertise"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAlchemyIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAlchemyIV"
        self.pName = "Alchemy Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbAlchemyV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbAlchemyV"
        self.pName = "Alchemy Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbWeaponsmithing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbWeaponsmithing"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbWeaponsmithingI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbWeaponsmithingI"
        self.pName = "Familiar Weaponsmithing"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbWeaponsmithingII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbWeaponsmithingII"
        self.pName = "Weaponsmithing Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbWeaponsmithingIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbWeaponsmithingIII"
        self.pName = "Expert Weaponsmithing"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbWeaponsmithingIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbWeaponsmithingIV"
        self.pName = "Weaponsmithing Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbWeaponsmithingV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbWeaponsmithingV"
        self.pName = "Weaponsmithing Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbArmorcrafting(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbArmorcrafting"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbArmorcraftingI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbArmorcraftingI"
        self.pName = "Familiar Armorcrafting"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbArmorcraftingII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbArmorcraftingII"
        self.pName = "Armorcrafting Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbArmorcraftingIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbArmorcraftingIII"
        self.pName = "Expert Armorcrafting"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbArmorcraftingIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbArmorcraftingIV"
        self.pName = "Armorcrafting Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbArmorcraftingV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbArmorcraftingV"
        self.pName = "Armorcrafting Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTracking(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTracking"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrackingI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrackingI"
        self.pName = "Familiar Tracking"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrackingII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrackingII"
        self.pName = "Tracking Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrackingIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrackingIII"
        self.pName = "Tracking Expertise"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrackingIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrackingIV"
        self.pName = "Tracking Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrackingV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrackingV"
        self.pName = "Tracking Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbHealing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbHealing"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbHealingI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbHealingI"
        self.pName = "Familiar Healing"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbHealingII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbHealingII"
        self.pName = "Healing Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbHealingIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbHealingIII"
        self.pName = "Healing Expertise"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbHealingIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbHealingIV"
        self.pName = "Healing Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbHealingV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbHealingV"
        self.pName = "Healing Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbPickpocketing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbPickpocketing"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbPickpocketingI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbPickpocketingI"
        self.pName = "Familiar Pickpocketing"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbPickpocketingII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbPickpocketingII"
        self.pName = "Pickpocketing Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbPickpocketingIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbPickpocketingIII"
        self.pName = "Pickpocketing Expertise"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbPickpocketingIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbPickpocketingIV"
        self.pName = "Pickpocketing Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbPickpocketingV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbPickpocketingV"
        self.pName = "Pickpocketing Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTraps(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTraps"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrapsI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrapsI"
        self.pName = "Basics of Trap Detection and Disarming"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrapsII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrapsII"
        self.pName = "Proficient Trap Manipulation"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrapsIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrapsIII"
        self.pName = "Expert Discourse on Traps"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrapsIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrapsIV"
        self.pName = "Mastery of Traps"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbTrapsV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbTrapsV"
        self.pName = "Disarming Traps = A Grand-Master Treatment"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLockpicking(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLockpicking"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLockpickingI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLockpickingI"
        self.pName = "Basics of Lockpicking"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLockpickingII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLockpickingII"
        self.pName = "Lockpicking Proficiency"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLockpickingIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLockpickingIII"
        self.pName = "Expert Lockpicking"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLockpickingIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLockpickingIV"
        self.pName = "Picking Masterful Locks"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbLockpickingV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbLockpickingV"
        self.pName = "Lockpicking Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMeditation(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMeditation"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMeditationI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMeditationI"
        self.pName = "The Basics of Meditation"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMeditationII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMeditationII"
        self.pName = "Becoming Proficient in Meditation"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMeditationIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMeditationIII"
        self.pName = "Meditation = Revelations of an Expert"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMeditationIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMeditationIV"
        self.pName = "Mastering Meditation"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbMeditationV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbMeditationV"
        self.pName = "Meditation Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbCriticalStriking(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbCriticalStriking"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbCriticalStrikingI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbCriticalStrikingI"
        self.pName = "The Basics of Critical Striking"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbCriticalStrikingII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbCriticalStrikingII"
        self.pName = "Critical Striking Proficiencies"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbCriticalStrikingIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbCriticalStrikingIII"
        self.pName = "Critical Striking = An Expert Discourse"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbCriticalStrikingIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbCriticalStrikingIV"
        self.pName = "Mastery of Critical Striking"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbCriticalStrikingV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbCriticalStrikingV"
        self.pName = "Critical Striking Grand-Mastery"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShieldUse(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShieldUse"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShieldUseI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShieldUseI"
        self.pName = "The Basics of Shield Usage"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShieldUseII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShieldUseII"
        self.pName = "Proficiencies in Shield Usage"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShieldUseIII(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShieldUseIII"
        self.pName = "Using Your Shield = An Expert Discourse"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShieldUseIV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShieldUseIV"
        self.pName = "Mastering the Shield"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJskbShieldUseV(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "skbShieldUseV"
        self.pName = "Shields = Defense by a Grand-Master"
        self.loop = 0
        self.pBaseView = 51150
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJSpellbook(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Spellbook"
        self.pName = "Book"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbBlank(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbBlank"
        self.pName = "Blank Spellbook"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

class SOBJspbHome(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbHome"
        self.pName = "Spellbook of Home"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbKillStar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbKillStar"
        self.pName = "Spellbook of Killstar"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbUnlock(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbUnlock"
        self.pName = "Spellbook of Unlock"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbDispelMagic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbDispelMagic"
        self.pName = "Spellbook of Dispel Magic"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbEngrave(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbEngrave"
        self.pName = "Spellbook of Engrave"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbMultiBlade(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbMultiBlade"
        self.pName = "Spellbook of Multi-Blade"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbGatherTheFellowship(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbGatherTheFellowship"
        self.pName = "Spellbook of Gather the Fellowship"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbCornucopia(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbCornucopia"
        self.pName = "Spellbook of Cornucopia"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbCloudOfFog(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbCloudOfFog"
        self.pName = "Spellbook of Grounding"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbImproveArmor(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbImproveArmor"
        self.pName = "Spellbook of Improve Armor"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbTeleport(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbTeleport"
        self.pName = "Spellbook of Teleport"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbExtension(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbExtension"
        self.pName = "Spellbook of Extension"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbSeeInvisibility(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbSeeInvisibility"
        self.pName = "Spellbook of See Invisibility"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbShift(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbShift"
        self.pName = "Spellbook of Shift"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbInvisibility(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbInvisibility"
        self.pName = "Spellbook of Invisibility"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbCombatTeleport(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbCombatTeleport"
        self.pName = "Spellbook of Combat Teleport"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbTeleportGroup(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbTeleportGroup"
        self.pName = "Spellbook of Teleport Group"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbPermanency(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbPermanency"
        self.pName = "Spellbook of Permanency"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbRust(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbRust"
        self.pName = "Spellbook of Rust"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbWraithform(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbWraithform"
        self.pName = "Spellbook of Defenselessness"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbImprovedInvisibility(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbImprovedInvisibility"
        self.pName = "Spellbook of Improved Invisibility"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbEnchantItem(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbEnchantItem"
        self.pName = "Spellbook of Enchant Item"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbMassRust(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbMassRust"
        self.pName = "Spellbook of Mass Rust"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbElphamesJustice(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbElphamesJustice"
        self.pName = "Spellbook of Elphame's Justice"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbGreaterIdentify(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbGreaterIdentify"
        self.pName = "Spellbook of Greater Identify"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbFireGrasp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbFireGrasp"
        self.pName = "Spellbook of Fire Grasp"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbFlameOrb(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbFlameOrb"
        self.pName = "Spellbook of Flame Orb"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbArticGrasp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbArticGrasp"
        self.pName = "Spellbook of Arctic Grasp"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbIceOrb(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbIceOrb"
        self.pName = "Spellbook of Ice Orb"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbEarthSpike(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbEarthSpike"
        self.pName = "Spellbook of Earth Avatar"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbIncinerate(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbIncinerate"
        self.pName = "Spellbook of Incinerate"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbGustOfWind(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbGustOfWind"
        self.pName = "Spellbook of Gust of Wind"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbImmolation(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbImmolation"
        self.pName = "Spellbook of Immolation"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbDancingFlame(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbDancingFlame"
        self.pName = "Spellbook of Fire Avatar"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbFlameBlade(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbFlameBlade"
        self.pName = "Spellbook of Flame Blade"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbArticCharge(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbArticCharge"
        self.pName = "Spellbook of Electric Charge"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbColdSteel(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbColdSteel"
        self.pName = "Spellbook of Cold Steel"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbSandstorm(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbSandstorm"
        self.pName = "Spellbook of Sandstorm"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbSpark(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbSpark"
        self.pName = "Spellbook of Spark"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbIceStorm(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbIceStorm"
        self.pName = "Spellbook of Ice Storm"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbFreezingWind(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbFreezingWind"
        self.pName = "Spellbook of Water Avatar"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbHurricane(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbHurricane"
        self.pName = "Spellbook of Air Avatar"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbCrawlingCharge(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbCrawlingCharge"
        self.pName = "Spellbook of Crawling Charge"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbStoning(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbStoning"
        self.pName = "Spellbook of Stoning"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbFireball(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbFireball"
        self.pName = "Spellbook of Fireball"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbLightningBolt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbLightningBolt"
        self.pName = "Spellbook of Lightning Bolt"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbFreeze(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbFreeze"
        self.pName = "Spellbook of Freeze"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbCrushingBoulder(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbCrushingBoulder"
        self.pName = "Spellbook of Crushing Boulder"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbElectricFury(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbElectricFury"
        self.pName = "Spellbook of Electric Fury"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbColdSnap(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbColdSnap"
        self.pName = "Spellbook of Cold Snap"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbEarthquake(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbEarthquake"
        self.pName = "Spellbook of Earthquake"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbDespothesWrath(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbDespothesWrath"
        self.pName = "Spellbook of Despothes' Wrath"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbHoldMonster(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbHoldMonster"
        self.pName = "Spellbook of Hold Monster"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbFumble(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbFumble"
        self.pName = "Spellbook of Fumble"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbPsychicOrb(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbPsychicOrb"
        self.pName = "Spellbook of Psychic Orb"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbConfusion(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbConfusion"
        self.pName = "Spellbook of Confusion"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbMindShackle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbMindShackle"
        self.pName = "Spellbook of Mind Shackle"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbIdentify(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbIdentify"
        self.pName = "Spellbook of Identify"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbBerserk(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbBerserk"
        self.pName = "Spellbook of Berserk"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbStun(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbStun"
        self.pName = "Spellbook of Stun"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbLoyaltyShift(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbLoyaltyShift"
        self.pName = "Spellbook of Loyalty Shift"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbWarpMind(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbWarpMind"
        self.pName = "Spellbook of Warp Mind"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

class SOBJspbEtheralize(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "spbEtheralize"
        self.pName = "Spellbook of Etherealize"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = -1
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 66


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BScroll")

StockObjList.append(SOBJMagicLockpick())
StockObjList.append(SOBJRobeOfDefense())
StockObjList.append(SOBJMagicChainPants())
StockObjList.append(SOBJMagicChainTunic())
StockObjList.append(SOBJMagicChainCowl())
StockObjList.append(SOBJEnchantedBoots())
StockObjList.append(SOBJEnchantedShield())
StockObjList.append(SOBJMagicPlatePants())
StockObjList.append(SOBJMagicPlateTunic())
StockObjList.append(SOBJOrbOfHealing())
StockObjList.append(SOBJOrbOfInvisibility())
StockObjList.append(SOBJOrbOfLightning())
StockObjList.append(SOBJOrbOfMana())
StockObjList.append(SOBJSkillbook())
StockObjList.append(SOBJskbBasketWeaving())
StockObjList.append(SOBJskbPsychology())
StockObjList.append(SOBJskbFriends())
StockObjList.append(SOBJskbShortSword())
StockObjList.append(SOBJskbShortSwordI())
StockObjList.append(SOBJskbShortSwordII())
StockObjList.append(SOBJskbShortSwordIII())
StockObjList.append(SOBJskbShortSwordIV())
StockObjList.append(SOBJskbShortSwordV())
StockObjList.append(SOBJskbLongSword())
StockObjList.append(SOBJskbLongSwordI())
StockObjList.append(SOBJskbLongSwordII())
StockObjList.append(SOBJskbLongSwordIII())
StockObjList.append(SOBJskbLongSwordIV())
StockObjList.append(SOBJskbLongSwordV())
StockObjList.append(SOBJskbTwoHandedSword())
StockObjList.append(SOBJskbTwoHandedSwordI())
StockObjList.append(SOBJskbTwoHandedSwordII())
StockObjList.append(SOBJskbTwoHandedSwordIII())
StockObjList.append(SOBJskbTwoHandedSwordIV())
StockObjList.append(SOBJskbTwoHandedSwordV())
StockObjList.append(SOBJskbDagger())
StockObjList.append(SOBJskbDaggerI())
StockObjList.append(SOBJskbDaggerII())
StockObjList.append(SOBJskbDaggerIII())
StockObjList.append(SOBJskbDaggerIV())
StockObjList.append(SOBJskbDaggerV())
StockObjList.append(SOBJskbAxe())
StockObjList.append(SOBJskbAxeI())
StockObjList.append(SOBJskbAxeII())
StockObjList.append(SOBJskbAxeIII())
StockObjList.append(SOBJskbAxeIV())
StockObjList.append(SOBJskbAxeV())
StockObjList.append(SOBJskbClub())
StockObjList.append(SOBJskbClubI())
StockObjList.append(SOBJskbClubII())
StockObjList.append(SOBJskbClubIII())
StockObjList.append(SOBJskbClubIV())
StockObjList.append(SOBJskbClubV())
StockObjList.append(SOBJskbMace())
StockObjList.append(SOBJskbMaceI())
StockObjList.append(SOBJskbMaceII())
StockObjList.append(SOBJskbMaceIII())
StockObjList.append(SOBJskbMaceIV())
StockObjList.append(SOBJskbMaceV())
StockObjList.append(SOBJskbUnarmedCombat())
StockObjList.append(SOBJskbUnarmedCombatI())
StockObjList.append(SOBJskbUnarmedCombatII())
StockObjList.append(SOBJskbUnarmedCombatIII())
StockObjList.append(SOBJskbUnarmedCombatIV())
StockObjList.append(SOBJskbUnarmedCombatV())
StockObjList.append(SOBJskbThrowingWeapon())
StockObjList.append(SOBJskbThrowingWeaponI())
StockObjList.append(SOBJskbThrowingWeaponII())
StockObjList.append(SOBJskbThrowingWeaponIII())
StockObjList.append(SOBJskbThrowingWeaponIV())
StockObjList.append(SOBJskbThrowingWeaponV())
StockObjList.append(SOBJskbAcrobatic())
StockObjList.append(SOBJskbAcrobaticI())
StockObjList.append(SOBJskbAcrobaticII())
StockObjList.append(SOBJskbAcrobaticIII())
StockObjList.append(SOBJskbAcrobaticIV())
StockObjList.append(SOBJskbAcrobaticV())
StockObjList.append(SOBJskbMaul())
StockObjList.append(SOBJskbMaulI())
StockObjList.append(SOBJskbMaulII())
StockObjList.append(SOBJskbMaulIII())
StockObjList.append(SOBJskbMaulIV())
StockObjList.append(SOBJskbMaulV())
StockObjList.append(SOBJskbSorcery())
StockObjList.append(SOBJskbSorceryI())
StockObjList.append(SOBJskbSorceryII())
StockObjList.append(SOBJskbSorceryIII())
StockObjList.append(SOBJskbSorceryIV())
StockObjList.append(SOBJskbSorceryV())
StockObjList.append(SOBJskbElementalism())
StockObjList.append(SOBJskbElementalismI())
StockObjList.append(SOBJskbElementalismII())
StockObjList.append(SOBJskbElementalismIII())
StockObjList.append(SOBJskbElementalismIV())
StockObjList.append(SOBJskbElementalismV())
StockObjList.append(SOBJskbMysticism())
StockObjList.append(SOBJskbMysticismI())
StockObjList.append(SOBJskbMysticismII())
StockObjList.append(SOBJskbMysticismIII())
StockObjList.append(SOBJskbMysticismIV())
StockObjList.append(SOBJskbMysticismV())
StockObjList.append(SOBJskbThaumaturgy())
StockObjList.append(SOBJskbThaumaturgyI())
StockObjList.append(SOBJskbThaumaturgyII())
StockObjList.append(SOBJskbThaumaturgyIII())
StockObjList.append(SOBJskbThaumaturgyIV())
StockObjList.append(SOBJskbThaumaturgyV())
StockObjList.append(SOBJskbNecromancy())
StockObjList.append(SOBJskbNecromancyI())
StockObjList.append(SOBJskbNecromancyII())
StockObjList.append(SOBJskbNecromancyIII())
StockObjList.append(SOBJskbNecromancyIV())
StockObjList.append(SOBJskbNecromancyV())
StockObjList.append(SOBJskbTheurgism())
StockObjList.append(SOBJskbTheurgismI())
StockObjList.append(SOBJskbTheurgismII())
StockObjList.append(SOBJskbTheurgismIII())
StockObjList.append(SOBJskbTheurgismIV())
StockObjList.append(SOBJskbTheurgismV())
StockObjList.append(SOBJskbAlchemy())
StockObjList.append(SOBJskbAlchemyI())
StockObjList.append(SOBJskbAlchemyII())
StockObjList.append(SOBJskbAlchemyIII())
StockObjList.append(SOBJskbAlchemyIV())
StockObjList.append(SOBJskbAlchemyV())
StockObjList.append(SOBJskbWeaponsmithing())
StockObjList.append(SOBJskbWeaponsmithingI())
StockObjList.append(SOBJskbWeaponsmithingII())
StockObjList.append(SOBJskbWeaponsmithingIII())
StockObjList.append(SOBJskbWeaponsmithingIV())
StockObjList.append(SOBJskbWeaponsmithingV())
StockObjList.append(SOBJskbArmorcrafting())
StockObjList.append(SOBJskbArmorcraftingI())
StockObjList.append(SOBJskbArmorcraftingII())
StockObjList.append(SOBJskbArmorcraftingIII())
StockObjList.append(SOBJskbArmorcraftingIV())
StockObjList.append(SOBJskbArmorcraftingV())
StockObjList.append(SOBJskbTracking())
StockObjList.append(SOBJskbTrackingI())
StockObjList.append(SOBJskbTrackingII())
StockObjList.append(SOBJskbTrackingIII())
StockObjList.append(SOBJskbTrackingIV())
StockObjList.append(SOBJskbTrackingV())
StockObjList.append(SOBJskbHealing())
StockObjList.append(SOBJskbHealingI())
StockObjList.append(SOBJskbHealingII())
StockObjList.append(SOBJskbHealingIII())
StockObjList.append(SOBJskbHealingIV())
StockObjList.append(SOBJskbHealingV())
StockObjList.append(SOBJskbPickpocketing())
StockObjList.append(SOBJskbPickpocketingI())
StockObjList.append(SOBJskbPickpocketingII())
StockObjList.append(SOBJskbPickpocketingIII())
StockObjList.append(SOBJskbPickpocketingIV())
StockObjList.append(SOBJskbPickpocketingV())
StockObjList.append(SOBJskbTraps())
StockObjList.append(SOBJskbTrapsI())
StockObjList.append(SOBJskbTrapsII())
StockObjList.append(SOBJskbTrapsIII())
StockObjList.append(SOBJskbTrapsIV())
StockObjList.append(SOBJskbTrapsV())
StockObjList.append(SOBJskbLockpicking())
StockObjList.append(SOBJskbLockpickingI())
StockObjList.append(SOBJskbLockpickingII())
StockObjList.append(SOBJskbLockpickingIII())
StockObjList.append(SOBJskbLockpickingIV())
StockObjList.append(SOBJskbLockpickingV())
StockObjList.append(SOBJskbMeditation())
StockObjList.append(SOBJskbMeditationI())
StockObjList.append(SOBJskbMeditationII())
StockObjList.append(SOBJskbMeditationIII())
StockObjList.append(SOBJskbMeditationIV())
StockObjList.append(SOBJskbMeditationV())
StockObjList.append(SOBJskbCriticalStriking())
StockObjList.append(SOBJskbCriticalStrikingI())
StockObjList.append(SOBJskbCriticalStrikingII())
StockObjList.append(SOBJskbCriticalStrikingIII())
StockObjList.append(SOBJskbCriticalStrikingIV())
StockObjList.append(SOBJskbCriticalStrikingV())
StockObjList.append(SOBJskbShieldUse())
StockObjList.append(SOBJskbShieldUseI())
StockObjList.append(SOBJskbShieldUseII())
StockObjList.append(SOBJskbShieldUseIII())
StockObjList.append(SOBJskbShieldUseIV())
StockObjList.append(SOBJskbShieldUseV())
StockObjList.append(SOBJSpellbook())
StockObjList.append(SOBJspbBlank())
StockObjList.append(SOBJspbHome())
StockObjList.append(SOBJspbKillStar())
StockObjList.append(SOBJspbUnlock())
StockObjList.append(SOBJspbDispelMagic())
StockObjList.append(SOBJspbEngrave())
StockObjList.append(SOBJspbMultiBlade())
StockObjList.append(SOBJspbGatherTheFellowship())
StockObjList.append(SOBJspbCornucopia())
StockObjList.append(SOBJspbCloudOfFog())
StockObjList.append(SOBJspbImproveArmor())
StockObjList.append(SOBJspbTeleport())
StockObjList.append(SOBJspbExtension())
StockObjList.append(SOBJspbSeeInvisibility())
StockObjList.append(SOBJspbShift())
StockObjList.append(SOBJspbInvisibility())
StockObjList.append(SOBJspbCombatTeleport())
StockObjList.append(SOBJspbTeleportGroup())
StockObjList.append(SOBJspbPermanency())
StockObjList.append(SOBJspbRust())
StockObjList.append(SOBJspbWraithform())
StockObjList.append(SOBJspbImprovedInvisibility())
StockObjList.append(SOBJspbEnchantItem())
StockObjList.append(SOBJspbMassRust())
StockObjList.append(SOBJspbElphamesJustice())
StockObjList.append(SOBJspbGreaterIdentify())
StockObjList.append(SOBJspbFireGrasp())
StockObjList.append(SOBJspbFlameOrb())
StockObjList.append(SOBJspbArticGrasp())
StockObjList.append(SOBJspbIceOrb())
StockObjList.append(SOBJspbEarthSpike())
StockObjList.append(SOBJspbIncinerate())
StockObjList.append(SOBJspbGustOfWind())
StockObjList.append(SOBJspbImmolation())
StockObjList.append(SOBJspbDancingFlame())
StockObjList.append(SOBJspbFlameBlade())
StockObjList.append(SOBJspbArticCharge())
StockObjList.append(SOBJspbColdSteel())
StockObjList.append(SOBJspbSandstorm())
StockObjList.append(SOBJspbSpark())
StockObjList.append(SOBJspbIceStorm())
StockObjList.append(SOBJspbFreezingWind())
StockObjList.append(SOBJspbHurricane())
StockObjList.append(SOBJspbCrawlingCharge())
StockObjList.append(SOBJspbStoning())
StockObjList.append(SOBJspbFireball())
StockObjList.append(SOBJspbLightningBolt())
StockObjList.append(SOBJspbFreeze())
StockObjList.append(SOBJspbCrushingBoulder())
StockObjList.append(SOBJspbElectricFury())
StockObjList.append(SOBJspbColdSnap())
StockObjList.append(SOBJspbEarthquake())
StockObjList.append(SOBJspbDespothesWrath())
StockObjList.append(SOBJspbHoldMonster())
StockObjList.append(SOBJspbFumble())
StockObjList.append(SOBJspbPsychicOrb())
StockObjList.append(SOBJspbConfusion())
StockObjList.append(SOBJspbMindShackle())
StockObjList.append(SOBJspbIdentify())
StockObjList.append(SOBJspbBerserk())
StockObjList.append(SOBJspbStun())
StockObjList.append(SOBJspbLoyaltyShift())
StockObjList.append(SOBJspbWarpMind())
StockObjList.append(SOBJspbEtheralize())
