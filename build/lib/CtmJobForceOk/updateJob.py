from UsefulUtilities import Utils
from CtmJobForceOk import settings
from CtmJobForceOk import commandExecuter

def run():
    logger, _, _ = Utils.loggerUtil()
    logger.info("< {} > ".format(settings.varName) + "Going to Send ForceOK to OrderID : " + settings.orderID)
    ctmpsmUpdateCommand = ['ctmpsm', '-updateajf', settings.orderID, 'FORCEOK']
    try:
        splittedLines = commandExecuter.run(ctmpsmUpdateCommand)
        logger.info("< {} > ".format(settings.varName) + "\n".join([str(x.decode('ascii')) for x in splittedLines]))
    except Exception as e:
        raise