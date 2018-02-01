from CtmJobForceOk import getNeededVarExpr
from CtmJobForceOk import updateJob
from CtmJobForceOk import sendMailNotification
from CtmJobForceOk import settings
from UsefulUtilities import Utils
import sys
import getopt
import os

def main():
    settings.init()
    argv = sys.argv[2:]
    try:
        logger,logFile, errorFile = Utils.loggerUtil()
        numOfArgs = len(sys.argv)
        if numOfArgs <= 2:
            raise Exception("no arguments sent! check it!", 9, logger.name)
        currentFileName = os.path.basename(__file__)
        try:
            opts, args = getopt.getopt(argv,'hv:', ["VarName="])
        except getopt.GetoptError as ge:
            raise Exception(ge.msg, 99, logger.name)
        if len(opts) == 0 :
            raise Exception("No Var Name sent! \'-v\' flag should be used", 9, logger.name)
        for opt, arg in opts:
            if opt == '-h':
               print (currentFileName + " -v VarName")
               sys.exit()
            elif opt in ("-v", "--VarName"):
                settings.varName = arg
                settings.varName = "%%" + settings.varName
            logger.info("< {} > ".format(settings.varName) + "*****\t\tNew request - Var name is : " + settings.varName)
        logger.info("< {} > ".format(settings.varName) + "Going to search for var : " + settings.varName + " in Global var list")
        settings.orderID = getNeededVarExpr.run()
        updateJob.run()
    except Exception as e:
        exception = e.args[0]
        returningFunction = e.args[2]
        logger.name = returningFunction
        logger.error("< {} > ".format(settings.varName) + exception, exc_info=True)
        '''
        localLogger.name = returningFunction
        localLogger.error("< {} > ".format(varName) + exception, exc_info=True)
        '''
        #print(exception)
        # Send Mail notification for exceptions with log file attached
        sendMailNotification.run(logFile, errorFile)
        if len(e.args) > 1:
            exitCode = e.args[1]
            exit(exitCode)
        else:
            raise


if __name__ == '__main__':
    main()

