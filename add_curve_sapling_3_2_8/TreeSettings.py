from .utils import toRad


class TreeSettings:
    def __init__(self, props):
        self.levels = props.levels  #
        self.length = props.length  #
        self.lengthV = props.lengthV  #
        self.taperCrown = props.taperCrown
        self.branches = props.branches  #
        self.curveRes = props.curveRes  #
        self.curve = toRad(props.curve)  #
        self.curveV = toRad(props.curveV)  #
        self.curveBack = toRad(props.curveBack)  #
        self.baseSplits = props.baseSplits  #
        self.segSplits = props.segSplits  #
        self.splitByLen = props.splitByLen
        self.rMode = props.rMode
        self.splitStraight = props.splitStraight
        self.splitLength = props.splitLength
        self.splitAngle = toRad(props.splitAngle)  #
        self.splitAngleV = toRad(props.splitAngleV)  #
        self.scale = props.scale  #
        self.scaleV = props.scaleV  #
        self.attractUp = props.attractUp  #
        self.attractOut = props.attractOut
        self.shape = int(props.shape)  #
        self.shapeS = int(props.shapeS)  #
        self.customShape = props.customShape
        self.branchDist = props.branchDist
        self.nrings = props.nrings
        self.baseSize = props.baseSize
        self.baseSize_s = props.baseSize_s
        self.leafBaseSize = props.leafBaseSize
        self.splitHeight = props.splitHeight
        self.splitBias = props.splitBias
        self.ratio = props.ratio
        self.minRadius = props.minRadius
        self.closeTip = props.closeTip
        self.rootFlare = props.rootFlare
        self.splitRadiusRatio = props.splitRadiusRatio
        self.autoTaper = props.autoTaper
        self.taper = props.taper  #
        self.noTip = props.noTip
        self.radiusTweak = props.radiusTweak
        self.ratioPower = props.ratioPower  #
        self.downAngle = toRad(props.downAngle)  #
        self.downAngleV = toRad(props.downAngleV)  #
        self.rotate = toRad(props.rotate)  #
        self.rotateV = toRad(props.rotateV)  #
        self.scale0 = props.scale0  #
        self.scaleV0 = props.scaleV0  #
        self.prune = props.prune  #
        self.pruneWidth = props.pruneWidth  #
        self.pruneBase = props.pruneBase
        self.pruneWidthPeak = props.pruneWidthPeak  #
        self.prunePowerLow = props.prunePowerLow  #
        self.prunePowerHigh = props.prunePowerHigh  #
        self.pruneRatio = props.pruneRatio  #


        self.useOldDownAngle = props.useOldDownAngle
        self.useParentAngle = props.useParentAngle

        self.matIndex = props.matIndex

        self.bevelRes = props.bevelRes  #
        self.resU = props.resU  #

        # Some effects can be turned ON and OFF, the necessary variables are changed here
        self.bevelDepth = 0.0
        if props.bevel:
            self.bevelDepth = 1.0

        self.handles = 'VECTOR'
        if props.handleType == '0':
            self.handles = 'AUTO'