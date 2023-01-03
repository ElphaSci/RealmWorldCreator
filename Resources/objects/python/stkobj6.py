from stock_objects import StockObjList,StockObject
global StockObjList





class SOBJHeavyXmasPolarBearGift(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HeavyXmasPolarBearGift"
        self.pName = "Polar Bear Gift"
        self.loop = 0
        self.pBaseView = 50455
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 150
        self.pWeight = 10000

        self.bases.append("BDescribed")

class SOBJHeavyXmasSnowmanFamily(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HeavyXmasSnowmanFamily"
        self.pName = "Holiday Snowman Family"
        self.loop = 0
        self.pBaseView = 50457
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 150
        self.pWeight = 10000

        self.bases.append("BDescribed")

class SOBJHeavyXmasChipmunk(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HeavyXmasChipmunk"
        self.pName = "Christmas Chipmunk"
        self.loop = 0
        self.pBaseView = 50458
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 150
        self.pWeight = 10000

        self.bases.append("BDescribed")

class SOBJHeavyXmasSignSantaStop(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "HeavyXmasSignSantaStop"
        self.pName = "Christmas Gift Sign"
        self.loop = 0
        self.pBaseView = 50464
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 150
        self.pWeight = 10000

        self.bases.append("BDescribed")

class SOBJOgre(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Ogre"
        self.pName = "Ogre"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 768
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 8


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJOgreChild(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OgreChild"
        self.pName = "Ogre Child"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 24
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 8


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJUglyOgre(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "UglyOgre"
        self.pName = "Ugly Ogre"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 794
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 8


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJOgreMage(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OgreMage"
        self.pName = "Ogre Mage"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 793
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 8


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJOgreChief(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "OgreChief"
        self.pName = "Ogre Chief"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 792
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 8


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJTroll(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Troll"
        self.pName = "Troll"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJTrollArmsman(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollArmsman"
        self.pName = "Troll Armsman"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 24
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJTrollWarrior(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollWarrior"
        self.pName = "Troll Warrior"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 25
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJTrollElementalist(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollElementalist"
        self.pName = "Troll Elementalist"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 26
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJTrollSorcerer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollSorcerer"
        self.pName = "Troll Sorcerer"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 26
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJTrollKing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TrollKing"
        self.pName = "Troll King"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 1814
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRockTroll(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RockTroll"
        self.pName = "Rock Troll"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 130
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRockTrollHealer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RockTrollHealer"
        self.pName = "Rock Troll Healer"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 131
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRockTrollWarrior(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RockTrollWarrior"
        self.pName = "Rock Troll Warrior"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 132
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRockTrollHunter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RockTrollHunter"
        self.pName = "Rock Troll Hunter"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 133
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRockTrollMage(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RockTrollMage"
        self.pName = "Rock Troll Mage"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 134
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRockTrollChieftan(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RockTrollChieftan"
        self.pName = "Rock Troll Chieftan"
        self.loop = 2
        self.pBaseView = 40200
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 135
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Imp"
        self.pName = "Imp Slave"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImpCitizen(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpCitizen"
        self.pName = "Imp Citizen"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 19
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImpGuard(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpGuard"
        self.pName = "Imp Guard"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 17
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImpSlaveMaster(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpSlaveMaster"
        self.pName = "Imp Slavemaster"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 16
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImpThaumaturgist(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpThaumaturgist"
        self.pName = "Imp Thaumaturgist"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 16
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImpNecromancer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpNecromancer"
        self.pName = "Imp Necromancer"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 18
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImpWarrior(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpWarrior"
        self.pName = "Imp Warrior"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 21
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJImpKing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ImpKing"
        self.pName = "Imp King"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 20
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJIceImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "IceImp"
        self.pName = "Ice Imp"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 22
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJWaterImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WaterImp"
        self.pName = "Water Imp"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 12
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJBloodImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BloodImp"
        self.pName = "Blood Imp"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 13
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRepententImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RepententImp"
        self.pName = "Repentent Imp"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 14
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 7


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJSunImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SunImp"
        self.pName = "Sun Imp"
        self.loop = 2
        self.pBaseView = 40500
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 15
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImp"
        self.pName = "Flying Imp"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpA"
        self.pName = "Flying Imp A"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 111
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpB"
        self.pName = "Flying Imp B"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 112
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpC(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpC"
        self.pName = "Flying Imp C"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 113
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpD(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpD"
        self.pName = "Flying Imp D"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 114
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpE(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpE"
        self.pName = "Flying Imp E"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 115
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpF(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpF"
        self.pName = "Flying Imp F"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 116
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpG(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpG"
        self.pName = "Flying Imp G"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 117
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpH(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpH"
        self.pName = "Flying Imp H"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 118
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpI(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpI"
        self.pName = "Flying Imp I"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 119
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpJ(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpJ"
        self.pName = "Flying Imp J"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 120
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpK(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpK"
        self.pName = "Flying Imp K"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 121
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpL(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpL"
        self.pName = "Flying Imp L"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 122
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpM(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpM"
        self.pName = "Flying Imp M"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 123
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFlyingImpN(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FlyingImpN"
        self.pName = "Flying Imp N"
        self.loop = 2
        self.pBaseView = 42650
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 124
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJSeraph(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Seraph"
        self.pName = "Seraph"
        self.loop = 2
        self.pBaseView = 40600
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 768
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 11


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJSeraphWarrior(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SeraphWarrior"
        self.pName = "Seraph Warrior"
        self.loop = 2
        self.pBaseView = 40600
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 813
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 11


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJSeraphThaumaturgist(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SeraphThaumaturgist"
        self.pName = "Seraph Thaumaturgist"
        self.loop = 2
        self.pBaseView = 40600
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 814
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 11


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJSeraphQueen(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "SeraphQueen"
        self.pName = "Seraph Queen"
        self.loop = 2
        self.pBaseView = 40600
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 815
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 11


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJMedusa(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Medusa"
        self.pName = "Medusa"
        self.loop = 2
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 17


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2500
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJCyclops(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Cyclops"
        self.pName = "Cyclops"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 1536
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2500
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJDevil(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Devil"
        self.pName = "Devil"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 3000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJTulorTheTerrible(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "TulorTheTerrible"
        self.pName = "Tulor"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 8000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJNakedThief(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NakedThief"
        self.pName = "Thief"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJThiefA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThiefA"
        self.pName = "Thief"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJThiefB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThiefB"
        self.pName = "Thief"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJThiefC(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThiefC"
        self.pName = "Thief"
        self.loop = 2
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJThiefD(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThiefD"
        self.pName = "Thief"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJThiefE(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "ThiefE"
        self.pName = "Thief"
        self.loop = 2
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJNakedBountyHunter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NakedBountyHunter"
        self.pName = "Bounty Hunter"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1500
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJBountyHunterA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BountyHunterA"
        self.pName = "Bounty Hunter"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1500
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJBountyHunterB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BountyHunterB"
        self.pName = "Bounty Hunter"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1500
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJBountyHunterC(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BountyHunterC"
        self.pName = "Bounty Hunter"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1500
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJBountyHunterD(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BountyHunterD"
        self.pName = "Bounty Hunter"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJBountyHunterE(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BountyHunterE"
        self.pName = "Bounty Hunter"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJBountyHunterF(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "BountyHunterF"
        self.pName = "Bounty Hunter"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJNakedWarrior(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "NakedWarrior"
        self.pName = "Warrior"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJWarriorA(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WarriorA"
        self.pName = "Warrior"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJWarriorB(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WarriorB"
        self.pName = "Warrior"
        self.loop = 2
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJWarriorC(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WarriorC"
        self.pName = "Warrior"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJWarriorD(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WarriorD"
        self.pName = "Warrior"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJWarriorE(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "WarriorE"
        self.pName = "Warrior"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 2000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJCleric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Cleric"
        self.pName = "Cleric"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJLightWiz(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "LightWiz"
        self.pName = "Wizard of Light"
        self.loop = 2
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1200
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJPriestess(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Priestess"
        self.pName = "Priestess"
        self.loop = 2
        self.pBaseView = 200
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 16


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1800
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJFuloranMaul(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "FuloranMaul"
        self.pName = "Fuloran's Maul"
        self.loop = 0
        self.pBaseView = 15400
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 58
        self.pBaseBitsLo = 513
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5900

        self.bases.append("BDescribed")

        self.bases.append("BWeapon")
        self.pDamageType = 2

class SOBJFuloran(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "Fuloran"
        self.pName = "Fuloran"
        self.loop = 2
        self.pBaseView = 100
        self.pAction = 1
        self.pClutStart = -1
        self.pColor = 794
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 13


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 20000
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")

class SOBJRandomCritter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "RandomCritter"
        self.pName = "Ratling"
        self.loop = 2
        self.pBaseView = 40100
        self.pAction = 1
        self.pClutStart = 104
        self.pColor = 104
        self.pBaseBitsLo = 4162
        self.pBaseBitsHi = 64
        self.pSoundGroup = 10


        self.bases.append("BCharacter")

        self.bases.append("BContainer")
        self.pWeightCap = 1400
        self.pBulkCap = 2000

        self.bases.append("BNPC")

        self.bases.append("BDescribed")


class SOBJCRAmulet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "CRAmulet"
        self.pName = "Amulet"
        self.pIDName = "Resist Cold Amulet"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = -1
        self.pBaseBitsLo = 9
        self.pBaseBitsHi = 64


        self.bases.append("BDescribed")

        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BWearable")
        self.pLayer = 0
        self.pAreaWorn = 19
        self.pMask = -1

class SOBJQuestObject(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "QuestObject"
        self.pName = ""
        self.loop = 0
        self.pBaseView = 0
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqOrcAmulet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qOrcAmulet"
        self.pName = "Orc Amulet"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 69
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqWirkkalaRemedy(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qWirkkalaRemedy"
        self.pName = "Wirkkala's Remedy"
        self.loop = 0
        self.pBaseView = 51600
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 94
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGrandmothersLetter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGrandmothersLetter"
        self.pName = "Grandmother's Letter"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 74
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFenriTuft(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFenriTuft"
        self.pName = "Tuft of Fenri Fur"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqEugenieCandles(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qEugenieCandles"
        self.pName = "Eugenie's Candles"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCompostWorms(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCompostWorms"
        self.pName = "Compost Worms"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCarvedSalt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCarvedSalt"
        self.pName = "Carved Salt Crystal"
        self.loop = 0
        self.pBaseView = 50700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJqCactusBit(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCactusBit"
        self.pName = "Bit of Cactus"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqKaliriTreat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qKaliriTreat"
        self.pName = "Kaliri's Treat"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFaerieScrap(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFaerieScrap"
        self.pName = "Scrap of Faerie Mantle"
        self.loop = 0
        self.pBaseView = 58850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGoldNugget(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGoldNugget"
        self.pName = "The Gold Nugget"
        self.loop = 0
        self.pBaseView = 50950
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqTobacReceipt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qTobacReceipt"
        self.pName = "Tobac Leaf Delivery Receipt"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 64
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJqJannVoucher(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qJannVoucher"
        self.pName = "Jann's Voucher"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 88
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJqWaspBelly(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qWaspBelly"
        self.pName = "Pulverized Wasp's Belly"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 48
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJqSharkTooth(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSharkTooth"
        self.pName = "Shark Tooth"
        self.loop = 0
        self.pBaseView = 57800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqJaqqarsRing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qJaqqarsRing"
        self.pName = "Ring of Jaqqar's Father"
        self.loop = 0
        self.pBaseView = 51850
        self.pAction = 29
        self.pClutStart = 112
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJqDarkElvesPackage(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDarkElvesPackage"
        self.pName = "Package from the Dark Elves"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BDescribed")

class SOBJqLochDreadWater(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qLochDreadWater"
        self.pName = "Loch Dread Water"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 99
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSzumiPouch(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSzumiPouch"
        self.pName = "Szumi's Pouch"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJqAncientRune(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAncientRune"
        self.pName = "Ancient Rune from Drune"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJqAuthorization(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAuthorization"
        self.pName = "Authorization"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJqParchment(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qParchment"
        self.pName = "Parchment"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 1

        self.bases.append("BDescribed")

class SOBJqBlackDiamond(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBlackDiamond"
        self.pName = "Black Diamond"
        self.loop = 0
        self.pBaseView = 50800
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBrokenAmulet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBrokenAmulet"
        self.pName = "Broken Amulet"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 78
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqNoteSiei(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qNoteSiei"
        self.pName = "Information from Siei"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPascoCheese(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPascoCheese"
        self.pName = "Pasco's Cheese"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBurnOintment(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBurnOintment"
        self.pName = "Burn Ointment"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 53
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 2

        self.bases.append("BDescribed")

class SOBJqAncientChainMail(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAncientChainMail"
        self.pName = "Ancient Chain Mail Segment"
        self.loop = 0
        self.pBaseView = 10000
        self.pAction = 29
        self.pClutStart = 93
        self.pColor = 93
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 20

        self.bases.append("BDescribed")

class SOBJqTrollToenail(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qTrollToenail"
        self.pName = "Troll Toe"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 64
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPoppingCorn(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPoppingCorn"
        self.pName = "Flask of Popping Corn"
        self.loop = 0
        self.pBaseView = 59000
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 10

        self.bases.append("BDescribed")

class SOBJqTalismanBaroq(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qTalismanBaroq"
        self.pName = "Talisman of Baroq the Bald"
        self.loop = 0
        self.pBaseView = 51450
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 5

        self.bases.append("BDescribed")

class SOBJqPascoKnife(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPascoKnife"
        self.pName = "Pasco Knife"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFenriFang(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFenriFang"
        self.pName = "Fenri Fang"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 69
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqVigoLunch(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qVigoLunch"
        self.pName = "Vigo's Lunch"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFishSpines(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFishSpines"
        self.pName = "Fish Spinal Bones"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqHerbSeed(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qHerbSeed"
        self.pName = "Herb Seed"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqKaliriSweet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qKaliriSweet"
        self.pName = "Kaliri's Sweet"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFingerBone(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFingerBone"
        self.pName = "Skeleton Finger Bone"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 64
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCarvedCastle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCarvedCastle"
        self.pName = "Carved Stone Castle"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDriftwood(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDriftwood"
        self.pName = "Driftwood"
        self.loop = 0
        self.pBaseView = 58150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqLeftovers(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qLeftovers"
        self.pName = "Vegetable Leftovers"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBatWhisker(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBatWhisker"
        self.pName = "Bat's Whisker"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqZuzuAntique(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qZuzuAntique"
        self.pName = "Zuzu's antique"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqUskSupplies(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qUskSupplies"
        self.pName = "Supplies from Usk"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFrickMed(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFrickMed"
        self.pName = "Frick's Allergy Medicine"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 89
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGeezerNote(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGeezerNote"
        self.pName = "Note from Geezer"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGeezerAle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGeezerAle"
        self.pName = "Ale for Geezer"
        self.loop = 0
        self.pBaseView = 59000
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSkonPackage(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSkonPackage"
        self.pName = "Skon's Package"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSkonScarf(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSkonScarf"
        self.pName = "Scon's Scarf"
        self.loop = 0
        self.pBaseView = 58850
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqWolfTail(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qWolfTail"
        self.pName = "Wolf's Tail"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletTamen(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletTamen"
        self.pName = "The Amulet of Tamen"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 48
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqJeweledDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qJeweledDagger"
        self.pName = "Jeweled Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 29
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletNemat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletNemat"
        self.pName = "Amulet of Nemat"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqStenchTools(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qStenchTools"
        self.pName = "Stench's Tools"
        self.loop = 0
        self.pBaseView = 59250
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFembrelWrench(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFembrelWrench"
        self.pName = "Fembrel Wrench"
        self.loop = 0
        self.pBaseView = 58500
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletNemor(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletNemor"
        self.pName = "Amulet of Nemor"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 78
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqJelliedBerries(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qJelliedBerries"
        self.pName = "Jellied Berries"
        self.loop = 0
        self.pBaseView = 59400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGrainBread(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGrainBread"
        self.pName = "Grain Bread of Murias"
        self.loop = 0
        self.pBaseView = 52050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletRomen(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletRomen"
        self.pName = "Amulet of Romen"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqNewPattern(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qNewPattern"
        self.pName = "New Pattern"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqWoolSkein(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qWoolSkein"
        self.pName = "Wool Skeins"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDariaBelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDariaBelt"
        self.pName = "Daria's Belt"
        self.loop = 0
        self.pBaseView = 10200
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = 94
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletBaroq(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletBaroq"
        self.pName = "Amulet of Baroq"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 49
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCarvedStork(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCarvedStork"
        self.pName = "Carved Stork"
        self.loop = 0
        self.pBaseView = 59300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSharpeningStone(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSharpeningStone"
        self.pName = "Nattan's Sharpening Stone"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqRatlingToenail(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qRatlingToenail"
        self.pName = "Ratling Toenail"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 69
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFossilizedToad(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFossilizedToad"
        self.pName = "Fossilized Toad"
        self.loop = 0
        self.pBaseView = 57750
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAldonzoDagger(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAldonzoDagger"
        self.pName = "Aldonzo's Dagger"
        self.loop = 0
        self.pBaseView = 15300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPetrifiedWood(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPetrifiedWood"
        self.pName = "Petrified Wood"
        self.loop = 0
        self.pBaseView = 58150
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMishaBelt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMishaBelt"
        self.pName = "Misha's Belt"
        self.loop = 0
        self.pBaseView = 10200
        self.pAction = 29
        self.pClutStart = 78
        self.pColor = 79
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSpecialOrder(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSpecialOrder"
        self.pName = "Special Order of Fabric"
        self.loop = 0
        self.pBaseView = 58200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBansheeRelic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBansheeRelic"
        self.pName = "Banshee Relic"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMaraKey(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMaraKey"
        self.pName = "Mara's Key"
        self.loop = 0
        self.pBaseView = 54300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqHeadacheCure(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qHeadacheCure"
        self.pName = "Headache Cure"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 64
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqImpBloodstone(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qImpBloodstone"
        self.pName = "Imp Bloodstone"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 79
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqHoliphEnvelope(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qHoliphEnvelope"
        self.pName = "Envelope for Holiph"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMeegoEnvelope(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMeegoEnvelope"
        self.pName = "Envelope for Litula"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMeegoCheese(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMeegoCheese"
        self.pName = "Meego's Cheese"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGnatsEar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGnatsEar"
        self.pName = "Giant Gnat's Ear"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 49
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAncientBird(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAncientBird"
        self.pName = "Ancient Bird Bits"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGiftCoat(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGiftCoat"
        self.pName = "Coat for Geezer"
        self.loop = 0
        self.pBaseView = 10400
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 48
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqEmptySkin(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qEmptySkin"
        self.pName = "Empty Insect Skin"
        self.loop = 0
        self.pBaseView = 57900
        self.pAction = 29
        self.pClutStart = 99
        self.pColor = 89
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqKombalWine(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qKombalWine"
        self.pName = "Kombal's Wine"
        self.loop = 0
        self.pBaseView = 59000
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqKombalBag(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qKombalBag"
        self.pName = "Kombal's Bag"
        self.loop = 0
        self.pBaseView = 50100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBatHair(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBatHair"
        self.pName = "Hair of Ancient Bat"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMartiParchment(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMartiParchment"
        self.pName = "Parchment from Marti"
        self.loop = 0
        self.pBaseView = 51100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMartiLunch(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMartiLunch"
        self.pName = "Marti's Lunch"
        self.loop = 0
        self.pBaseView = 59300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDevoBook(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDevoBook"
        self.pName = "Devo's Book"
        self.loop = 0
        self.pBaseView = 51050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSeraphScroll(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSeraphScroll"
        self.pName = "Seraph Scroll Fragment"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqJolieScarf(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qJolieScarf"
        self.pName = "Jolie's Scarf"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFoodBasket(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFoodBasket"
        self.pName = "Food Basket"
        self.loop = 0
        self.pBaseView = 59400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAsgardHieroglyphic(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAsgardHieroglyphic"
        self.pName = "Ancient Hieroglyphic"
        self.loop = 0
        self.pBaseView = 51450
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 105
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFaerieParchment(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFaerieParchment"
        self.pName = "Ancient Faerie Parchment"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBlytheBoots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBlytheBoots"
        self.pName = "Minka's Boots"
        self.loop = 0
        self.pBaseView = 10600
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 94
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqUskPapyrus(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qUskPapyrus"
        self.pName = "Torn Papyrus"
        self.loop = 0
        self.pBaseView = 51000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSnakeRattle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSnakeRattle"
        self.pName = "Rattle of Snake"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 49
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAliApricots(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAliApricots"
        self.pName = "Apricots"
        self.loop = 0
        self.pBaseView = 59300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDownsCurio(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDownsCurio"
        self.pName = "Strange Curio"
        self.loop = 0
        self.pBaseView = 57900
        self.pAction = 29
        self.pClutStart = 99
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCuriousRock(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCuriousRock"
        self.pName = "Curious Desert Rock"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqKaliriCookies(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qKaliriCookies"
        self.pName = "Cookies for Kaliri"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSanriaDill(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSanriaDill"
        self.pName = "Dill for Sanria"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletLemelion(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletLemelion"
        self.pName = "Amulet of Lemelion"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAntiquatedBroach(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAntiquatedBroach"
        self.pName = "Antiquated Broach"
        self.loop = 0
        self.pBaseView = 50800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqEmbroideredFabric(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qEmbroideredFabric"
        self.pName = "Bolt of Embroidered Fabric"
        self.loop = 0
        self.pBaseView = 58200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCottonPlant(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCottonPlant"
        self.pName = "Cotton Plant"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqEnidToken(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qEnidToken"
        self.pName = "Token of Enid"
        self.loop = 0
        self.pBaseView = 51450
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPotionHolder(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPotionHolder"
        self.pName = "Potion Holder"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 69
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPotShard(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPotShard"
        self.pName = "Pot Shard"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSlugShirt(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSlugShirt"
        self.pName = "Slug's Shirt"
        self.loop = 0
        self.pBaseView = 10100
        self.pAction = 29
        self.pClutStart = 53
        self.pColor = 89
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPolishedStone(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPolishedStone"
        self.pName = "Polished Stone"
        self.loop = 0
        self.pBaseView = 50700
        self.pAction = 29
        self.pClutStart = 58
        self.pColor = 78
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBlackMushrooms(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBlackMushrooms"
        self.pName = "Black Mushrooms"
        self.loop = 0
        self.pBaseView = 59400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMeulenSupplies(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMeulenSupplies"
        self.pName = "Muelen's Supplies"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqOilLamp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qOilLamp"
        self.pName = "Ancient Oil Lamp"
        self.loop = 0
        self.pBaseView = 59300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGreenGlobe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGreenGlobe"
        self.pName = "Green Globe"
        self.loop = 0
        self.pBaseView = 51750
        self.pAction = 29
        self.pClutStart = 79
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGreenBottle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGreenBottle"
        self.pName = "Green Bottle"
        self.loop = 0
        self.pBaseView = 59100
        self.pAction = 29
        self.pClutStart = 88
        self.pColor = 83
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqWoodenPuzzle(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qWoodenPuzzle"
        self.pName = "Wooden Puzzle"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDriftwoodSupply(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDriftwoodSupply"
        self.pName = "Driftwood"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPowderedImp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPowderedImp"
        self.pName = "Powdered Imp"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDinglebean(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDinglebean"
        self.pName = "Dinglebean Extract"
        self.loop = 0
        self.pBaseView = 59200
        self.pAction = 29
        self.pClutStart = 88
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGravestoneChip(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGravestoneChip"
        self.pName = "Gravestone Chip"
        self.loop = 0
        self.pBaseView = 57850
        self.pAction = 29
        self.pClutStart = 104
        self.pColor = 100
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqWaspWing(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qWaspWing"
        self.pName = "Wasp's Wing"
        self.loop = 0
        self.pBaseView = 58000
        self.pAction = 29
        self.pClutStart = 48
        self.pColor = 63
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSmokedStripe(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSmokedStripe"
        self.pName = "Smoked Stripe"
        self.loop = 0
        self.pBaseView = 59300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFlowerSeed(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFlowerSeed"
        self.pName = "Flower Seed"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDaemonToken(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDaemonToken"
        self.pName = "Daemon Token"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMetalShielding(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMetalShielding"
        self.pName = "Metal Shielding"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBeakerWater(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBeakerWater"
        self.pName = "Distilled Water"
        self.loop = 0
        self.pBaseView = 59000
        self.pAction = 29
        self.pClutStart = 83
        self.pColor = 64
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBrownPaper(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBrownPaper"
        self.pName = "Brown Wrapping Paper"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMalinaSupplies(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMalinaSupplies"
        self.pName = "Supplies for Malina"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqMagicRock(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qMagicRock"
        self.pName = "Magic Rock"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqPetrifiedSnail(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qPetrifiedSnail"
        self.pName = "Petrified Snail"
        self.loop = 0
        self.pBaseView = 59200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqEmptyJar(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qEmptyJar"
        self.pName = "Empty Jar"
        self.loop = 0
        self.pBaseView = 59200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFossilScorpion(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFossilScorpion"
        self.pName = "Fossilized Scorpion"
        self.loop = 0
        self.pBaseView = 57750
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAimiePackage(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAimiePackage"
        self.pName = "Aimie's package."
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFrickMedicine(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFrickMedicine"
        self.pName = "Medicine for Frick"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 59
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqBlackbirdFeathers(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qBlackbirdFeathers"
        self.pName = "Blackbird Feathers"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDriftwoodFrame(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDriftwoodFrame"
        self.pName = "Driftwood Frame"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSalve(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSalve"
        self.pName = "Salve for Misha"
        self.loop = 0
        self.pBaseView = 51800
        self.pAction = 29
        self.pClutStart = 63
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqLegotiaFood(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qLegotiaFood"
        self.pName = "Legotia's Snack"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletStealth(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletStealth"
        self.pName = "Amulet of Stealth"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 98
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqRattHelp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qRattHelp"
        self.pName = "Packet for Ratt"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 94
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqElfaHelp(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qElfaHelp"
        self.pName = "Lireen's Medicinal Powder"
        self.loop = 0
        self.pBaseView = 50450
        self.pAction = 29
        self.pClutStart = 73
        self.pColor = 54
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGinkarooBark(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGinkarooBark"
        self.pName = "Ginkaroo Bark"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqZkgbContainer(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qZkgbContainer"
        self.pName = "ZKGB Contained"
        self.loop = 0
        self.pBaseView = 58000
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFreshBread(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFreshBread"
        self.pName = "Fresh Baked Bread"
        self.loop = 0
        self.pBaseView = 52050
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFishLine(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFishLine"
        self.pName = "Fishing Line"
        self.loop = 0
        self.pBaseView = 58300
        self.pAction = 29
        self.pClutStart = 54
        self.pColor = 99
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGooeyBuns(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGooeyBuns"
        self.pName = "Gooey Buns for Spidey"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSanriaPackage(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSanriaPackage"
        self.pName = "Sanria's Package"
        self.loop = 0
        self.pBaseView = 58900
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqNeedlePacket(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qNeedlePacket"
        self.pName = "Packet of Needles"
        self.loop = 0
        self.pBaseView = 60611
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCoffeeBeans(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCoffeeBeans"
        self.pName = "Coffee Beans"
        self.loop = 0
        self.pBaseView = 59200
        self.pAction = 29
        self.pClutStart = 88
        self.pColor = 59
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqLavender(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qLavender"
        self.pName = "Dried Lavender"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqInterestingPlant(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qInterestingPlant"
        self.pName = "An Interesting Plant"
        self.loop = 0
        self.pBaseView = 58100
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqLunch(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qLunch"
        self.pName = "Lalana's Lunch"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqKneeOintment(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qKneeOintment"
        self.pName = "Knee Ointment"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 84
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqLireenPackage(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qLireenPackage"
        self.pName = "Package for Lireen"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqWandaLunch(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qWandaLunch"
        self.pName = "Wanda's Lunch"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDecrepitScabbard(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDecrepitScabbard"
        self.pName = "Scrap of Decrepit Scabbard"
        self.loop = 0
        self.pBaseView = 57750
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqRennet(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qRennet"
        self.pName = "Packet of Rennet"
        self.loop = 0
        self.pBaseView = 59200
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqAmuletBlue(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qAmuletBlue"
        self.pName = "Amulet of Blue Steel"
        self.loop = 0
        self.pBaseView = 51500
        self.pAction = 29
        self.pClutStart = 122
        self.pColor = 53
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDespothesSash(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDespothesSash"
        self.pName = "Sash of Despothes"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSeaSnail(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSeaSnail"
        self.pName = "Sea Snail Fossil"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqCinnamonOil(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qCinnamonOil"
        self.pName = "Cinnamon Oil"
        self.loop = 0
        self.pBaseView = 51550
        self.pAction = 29
        self.pClutStart = 68
        self.pColor = 58
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqGhoudLunch(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qGhoudLunch"
        self.pName = "Ghoud's Lunch"
        self.loop = 0
        self.pBaseView = 59300
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqFeatherKurz(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qFeatherKurz"
        self.pName = "Feather from Kurz"
        self.loop = 0
        self.pBaseView = 50400
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqDeterrent(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qDeterrent"
        self.pName = "Pest Deterrent"
        self.loop = 0
        self.pBaseView = 59200
        self.pAction = 29
        self.pClutStart = 88
        self.pColor = 79
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqScarab(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qScarab"
        self.pName = "Scarab"
        self.loop = 0
        self.pBaseView = 50700
        self.pAction = 29
        self.pClutStart = 84
        self.pColor = 88
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

class SOBJqSpeckledMinter(StockObject):
    name = ""

    def __init__(self):
        self.bases = []
        self.name = "qSpeckledMinter"
        self.pName = "Speckled Minter"
        self.loop = 0
        self.pBaseView = 58800
        self.pAction = 29
        self.pClutStart = 0
        self.pColor = 0
        self.pBaseBitsLo = 1
        self.pBaseBitsHi = 64


        self.bases.append("BCarryable")
        self.pBulk = 0
        self.pWeight = 4

        self.bases.append("BDescribed")

StockObjList.append(SOBJHeavyXmasPolarBearGift())
StockObjList.append(SOBJHeavyXmasSnowmanFamily())
StockObjList.append(SOBJHeavyXmasChipmunk())
StockObjList.append(SOBJHeavyXmasSignSantaStop())
StockObjList.append(SOBJOgre())
StockObjList.append(SOBJOgreChild())
StockObjList.append(SOBJUglyOgre())
StockObjList.append(SOBJOgreMage())
StockObjList.append(SOBJOgreChief())
StockObjList.append(SOBJTroll())
StockObjList.append(SOBJTrollArmsman())
StockObjList.append(SOBJTrollWarrior())
StockObjList.append(SOBJTrollElementalist())
StockObjList.append(SOBJTrollSorcerer())
StockObjList.append(SOBJTrollKing())
StockObjList.append(SOBJRockTroll())
StockObjList.append(SOBJRockTrollHealer())
StockObjList.append(SOBJRockTrollWarrior())
StockObjList.append(SOBJRockTrollHunter())
StockObjList.append(SOBJRockTrollMage())
StockObjList.append(SOBJRockTrollChieftan())
StockObjList.append(SOBJImp())
StockObjList.append(SOBJImpCitizen())
StockObjList.append(SOBJImpGuard())
StockObjList.append(SOBJImpSlaveMaster())
StockObjList.append(SOBJImpThaumaturgist())
StockObjList.append(SOBJImpNecromancer())
StockObjList.append(SOBJImpWarrior())
StockObjList.append(SOBJImpKing())
StockObjList.append(SOBJIceImp())
StockObjList.append(SOBJWaterImp())
StockObjList.append(SOBJBloodImp())
StockObjList.append(SOBJRepententImp())
StockObjList.append(SOBJSunImp())
StockObjList.append(SOBJFlyingImp())
StockObjList.append(SOBJFlyingImpA())
StockObjList.append(SOBJFlyingImpB())
StockObjList.append(SOBJFlyingImpC())
StockObjList.append(SOBJFlyingImpD())
StockObjList.append(SOBJFlyingImpE())
StockObjList.append(SOBJFlyingImpF())
StockObjList.append(SOBJFlyingImpG())
StockObjList.append(SOBJFlyingImpH())
StockObjList.append(SOBJFlyingImpI())
StockObjList.append(SOBJFlyingImpJ())
StockObjList.append(SOBJFlyingImpK())
StockObjList.append(SOBJFlyingImpL())
StockObjList.append(SOBJFlyingImpM())
StockObjList.append(SOBJFlyingImpN())
StockObjList.append(SOBJSeraph())
StockObjList.append(SOBJSeraphWarrior())
StockObjList.append(SOBJSeraphThaumaturgist())
StockObjList.append(SOBJSeraphQueen())
StockObjList.append(SOBJMedusa())
StockObjList.append(SOBJCyclops())
StockObjList.append(SOBJDevil())
StockObjList.append(SOBJTulorTheTerrible())
StockObjList.append(SOBJNakedThief())
StockObjList.append(SOBJThiefA())
StockObjList.append(SOBJThiefB())
StockObjList.append(SOBJThiefC())
StockObjList.append(SOBJThiefD())
StockObjList.append(SOBJThiefE())
StockObjList.append(SOBJNakedBountyHunter())
StockObjList.append(SOBJBountyHunterA())
StockObjList.append(SOBJBountyHunterB())
StockObjList.append(SOBJBountyHunterC())
StockObjList.append(SOBJBountyHunterD())
StockObjList.append(SOBJBountyHunterE())
StockObjList.append(SOBJBountyHunterF())
StockObjList.append(SOBJNakedWarrior())
StockObjList.append(SOBJWarriorA())
StockObjList.append(SOBJWarriorB())
StockObjList.append(SOBJWarriorC())
StockObjList.append(SOBJWarriorD())
StockObjList.append(SOBJWarriorE())
StockObjList.append(SOBJCleric())
StockObjList.append(SOBJLightWiz())
StockObjList.append(SOBJPriestess())
StockObjList.append(SOBJFuloranMaul())
StockObjList.append(SOBJFuloran())
StockObjList.append(SOBJRandomCritter())
StockObjList.append(SOBJCRAmulet())
StockObjList.append(SOBJQuestObject())
StockObjList.append(SOBJqOrcAmulet())
StockObjList.append(SOBJqWirkkalaRemedy())
StockObjList.append(SOBJqGrandmothersLetter())
StockObjList.append(SOBJqFenriTuft())
StockObjList.append(SOBJqEugenieCandles())
StockObjList.append(SOBJqCompostWorms())
StockObjList.append(SOBJqCarvedSalt())
StockObjList.append(SOBJqCactusBit())
StockObjList.append(SOBJqKaliriTreat())
StockObjList.append(SOBJqFaerieScrap())
StockObjList.append(SOBJqGoldNugget())
StockObjList.append(SOBJqTobacReceipt())
StockObjList.append(SOBJqJannVoucher())
StockObjList.append(SOBJqWaspBelly())
StockObjList.append(SOBJqSharkTooth())
StockObjList.append(SOBJqJaqqarsRing())
StockObjList.append(SOBJqDarkElvesPackage())
StockObjList.append(SOBJqLochDreadWater())
StockObjList.append(SOBJqSzumiPouch())
StockObjList.append(SOBJqAncientRune())
StockObjList.append(SOBJqAuthorization())
StockObjList.append(SOBJqParchment())
StockObjList.append(SOBJqBlackDiamond())
StockObjList.append(SOBJqBrokenAmulet())
StockObjList.append(SOBJqNoteSiei())
StockObjList.append(SOBJqPascoCheese())
StockObjList.append(SOBJqBurnOintment())
StockObjList.append(SOBJqAncientChainMail())
StockObjList.append(SOBJqTrollToenail())
StockObjList.append(SOBJqPoppingCorn())
StockObjList.append(SOBJqTalismanBaroq())
StockObjList.append(SOBJqPascoKnife())
StockObjList.append(SOBJqFenriFang())
StockObjList.append(SOBJqVigoLunch())
StockObjList.append(SOBJqFishSpines())
StockObjList.append(SOBJqHerbSeed())
StockObjList.append(SOBJqKaliriSweet())
StockObjList.append(SOBJqFingerBone())
StockObjList.append(SOBJqCarvedCastle())
StockObjList.append(SOBJqDriftwood())
StockObjList.append(SOBJqLeftovers())
StockObjList.append(SOBJqBatWhisker())
StockObjList.append(SOBJqZuzuAntique())
StockObjList.append(SOBJqUskSupplies())
StockObjList.append(SOBJqFrickMed())
StockObjList.append(SOBJqGeezerNote())
StockObjList.append(SOBJqGeezerAle())
StockObjList.append(SOBJqSkonPackage())
StockObjList.append(SOBJqSkonScarf())
StockObjList.append(SOBJqWolfTail())
StockObjList.append(SOBJqAmuletTamen())
StockObjList.append(SOBJqJeweledDagger())
StockObjList.append(SOBJqAmuletNemat())
StockObjList.append(SOBJqStenchTools())
StockObjList.append(SOBJqFembrelWrench())
StockObjList.append(SOBJqAmuletNemor())
StockObjList.append(SOBJqJelliedBerries())
StockObjList.append(SOBJqGrainBread())
StockObjList.append(SOBJqAmuletRomen())
StockObjList.append(SOBJqNewPattern())
StockObjList.append(SOBJqWoolSkein())
StockObjList.append(SOBJqDariaBelt())
StockObjList.append(SOBJqAmuletBaroq())
StockObjList.append(SOBJqCarvedStork())
StockObjList.append(SOBJqSharpeningStone())
StockObjList.append(SOBJqRatlingToenail())
StockObjList.append(SOBJqFossilizedToad())
StockObjList.append(SOBJqAldonzoDagger())
StockObjList.append(SOBJqPetrifiedWood())
StockObjList.append(SOBJqMishaBelt())
StockObjList.append(SOBJqSpecialOrder())
StockObjList.append(SOBJqBansheeRelic())
StockObjList.append(SOBJqMaraKey())
StockObjList.append(SOBJqHeadacheCure())
StockObjList.append(SOBJqImpBloodstone())
StockObjList.append(SOBJqHoliphEnvelope())
StockObjList.append(SOBJqMeegoEnvelope())
StockObjList.append(SOBJqMeegoCheese())
StockObjList.append(SOBJqGnatsEar())
StockObjList.append(SOBJqAncientBird())
StockObjList.append(SOBJqGiftCoat())
StockObjList.append(SOBJqEmptySkin())
StockObjList.append(SOBJqKombalWine())
StockObjList.append(SOBJqKombalBag())
StockObjList.append(SOBJqBatHair())
StockObjList.append(SOBJqMartiParchment())
StockObjList.append(SOBJqMartiLunch())
StockObjList.append(SOBJqDevoBook())
StockObjList.append(SOBJqSeraphScroll())
StockObjList.append(SOBJqJolieScarf())
StockObjList.append(SOBJqFoodBasket())
StockObjList.append(SOBJqAsgardHieroglyphic())
StockObjList.append(SOBJqFaerieParchment())
StockObjList.append(SOBJqBlytheBoots())
StockObjList.append(SOBJqUskPapyrus())
StockObjList.append(SOBJqSnakeRattle())
StockObjList.append(SOBJqAliApricots())
StockObjList.append(SOBJqDownsCurio())
StockObjList.append(SOBJqCuriousRock())
StockObjList.append(SOBJqKaliriCookies())
StockObjList.append(SOBJqSanriaDill())
StockObjList.append(SOBJqAmuletLemelion())
StockObjList.append(SOBJqAntiquatedBroach())
StockObjList.append(SOBJqEmbroideredFabric())
StockObjList.append(SOBJqCottonPlant())
StockObjList.append(SOBJqEnidToken())
StockObjList.append(SOBJqPotionHolder())
StockObjList.append(SOBJqPotShard())
StockObjList.append(SOBJqSlugShirt())
StockObjList.append(SOBJqPolishedStone())
StockObjList.append(SOBJqBlackMushrooms())
StockObjList.append(SOBJqMeulenSupplies())
StockObjList.append(SOBJqOilLamp())
StockObjList.append(SOBJqGreenGlobe())
StockObjList.append(SOBJqGreenBottle())
StockObjList.append(SOBJqWoodenPuzzle())
StockObjList.append(SOBJqDriftwoodSupply())
StockObjList.append(SOBJqPowderedImp())
StockObjList.append(SOBJqDinglebean())
StockObjList.append(SOBJqGravestoneChip())
StockObjList.append(SOBJqWaspWing())
StockObjList.append(SOBJqSmokedStripe())
StockObjList.append(SOBJqFlowerSeed())
StockObjList.append(SOBJqDaemonToken())
StockObjList.append(SOBJqMetalShielding())
StockObjList.append(SOBJqBeakerWater())
StockObjList.append(SOBJqBrownPaper())
StockObjList.append(SOBJqMalinaSupplies())
StockObjList.append(SOBJqMagicRock())
StockObjList.append(SOBJqPetrifiedSnail())
StockObjList.append(SOBJqEmptyJar())
StockObjList.append(SOBJqFossilScorpion())
StockObjList.append(SOBJqAimiePackage())
StockObjList.append(SOBJqFrickMedicine())
StockObjList.append(SOBJqBlackbirdFeathers())
StockObjList.append(SOBJqDriftwoodFrame())
StockObjList.append(SOBJqSalve())
StockObjList.append(SOBJqLegotiaFood())
StockObjList.append(SOBJqAmuletStealth())
StockObjList.append(SOBJqRattHelp())
StockObjList.append(SOBJqElfaHelp())
StockObjList.append(SOBJqGinkarooBark())
StockObjList.append(SOBJqZkgbContainer())
StockObjList.append(SOBJqFreshBread())
StockObjList.append(SOBJqFishLine())
StockObjList.append(SOBJqGooeyBuns())
StockObjList.append(SOBJqSanriaPackage())
StockObjList.append(SOBJqNeedlePacket())
StockObjList.append(SOBJqCoffeeBeans())
StockObjList.append(SOBJqLavender())
StockObjList.append(SOBJqInterestingPlant())
StockObjList.append(SOBJqLunch())
StockObjList.append(SOBJqKneeOintment())
StockObjList.append(SOBJqLireenPackage())
StockObjList.append(SOBJqWandaLunch())
StockObjList.append(SOBJqDecrepitScabbard())
StockObjList.append(SOBJqRennet())
StockObjList.append(SOBJqAmuletBlue())
StockObjList.append(SOBJqDespothesSash())
StockObjList.append(SOBJqSeaSnail())
StockObjList.append(SOBJqCinnamonOil())
StockObjList.append(SOBJqGhoudLunch())
StockObjList.append(SOBJqFeatherKurz())
StockObjList.append(SOBJqDeterrent())
StockObjList.append(SOBJqScarab())
StockObjList.append(SOBJqSpeckledMinter())
