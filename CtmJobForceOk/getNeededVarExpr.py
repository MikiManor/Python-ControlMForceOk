from UsefulUtilities import Utils
from CtmJobForceOk import settings
from CtmJobForceOk import commandExecuter
from CtmJobForceOk import sendMailNotification

def run():
    logger, logFile, errorFile = Utils.loggerUtil()
    ctmvarCommand = ['ctmvar', '-action', 'list']
    neededVarExpr = ''
    try:
        splittedLines = commandExecuter.run(ctmvarCommand)
        if isinstance(splittedLines, list):
            splittedLines = splittedLines[5:-3]
            #varsTable = []
            isFound = False
            for line in splittedLines:
                try:
                    line = line.decode('ascii').split()
                    #varsTable.append(line)
                    if line:  # Check if the line is not empty
                        # Every line (which not empty includes the var name at the first field)
                        if settings.varName == line[0]:
                            isFound = True
                            logger.info("< {} > ".format(settings.varName) + "Found the following line : " + str(line))
                            neededVarExpr = line[1]
                            pass
                    else:
                        continue
                except Exception as e:
                    logger.warn("< {} > {} for line : \n {} ".format(settings.varName, e, line) )
                    sendMailNotification.run(logFile, errorFile)
                    continue
            if not isFound:
                raise Exception("Something went wrong! no matching found...Exiting with code 4!", 4, logger.name)
            else:
                return(neededVarExpr)
        else:
            raise Exception("Returned empty list from command : {}".format(ctmvarCommand), logger.name)
    except Exception as e:
        raise
