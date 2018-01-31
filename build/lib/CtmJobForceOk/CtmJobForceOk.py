#varName = ''
#orderID = ''

# def commandExecuter(commandToExecute):
#     logger, _, _ = Utils.loggerUtil()
#     try:
#         ctmpsmOutput = subp.Popen(commandToExecute, stdout=subp.PIPE, stderr=subp.PIPE, shell=True)
#         out, err = ctmpsmOutput.communicate()
#         splittedLines = out.splitlines()
#         rc = ctmpsmOutput.returncode
#         if rc != 0 :
#             errors = "\n".join([str(x.decode('ascii')) for x in err.splitlines()])
#             output = "\n".join([str(x.decode('ascii')) for x in out.splitlines()])
#             if errors:
#                 raise Exception(errors)
#             if output:
#                 raise Exception(output)
#             if errors and output:
#                 raise Exception(output + "\n" + errors)
#         return splittedLines
#     except Exception as e:
#         raise Exception("Something went wrong with the command : " + str(commandToExecute) + "\n" +
#                         str(e.args[0]) + "\nExiting with code  9!", 9, logger.name)

# def getNeededVarExpr():
#     logger, logFile, errorFile = Utils.loggerUtil()
#     ctmvarCommand = ['ctmvar', '-action', 'list']
#     neededVarExpr = ''
#     try:
#         splittedLines = commandExecuter(ctmvarCommand)
#         if isinstance(splittedLines, list):
#             splittedLines = splittedLines[5:-3]
#             #varsTable = []
#             isFound = False
#             for line in splittedLines:
#                 try:
#                     line = line.decode('ascii').split()
#                     #varsTable.append(line)
#                     if line:  # Check if the line is not empty
#                         if settings.varName == line[0]:  # Every line (which not empty includes the var name at the first field)
#                             isFound = True
#                             logger.info("< {} > ".format(settings.varName) + "Found the following line : " + str(line))
#                             neededVarExpr = line[1]
#                             pass
#                     else:
#                         continue
#                 except Exception as e:
#                     logger.warn("< {} > {} for line : \n {} ".format(settings.varName, e, line) )
#                     sendMailNotification(logFile, errorFile)
#                     continue
#             if not isFound:
#                 raise Exception("Something went wrong! no matching found...Exiting with code 4!", 4, logger.name)
#             else:
#                 return(neededVarExpr)
#         else:
#             raise Exception("Returned empty list from command : {}".format(ctmvarCommand), logger.name )
#     except Exception as e:
#         raise

# def updateJob():
#     logger, _, _ = Utils.loggerUtil()
#     logger.info("< {} > ".format(settings.varName) + "Going to Send ForceOK to OrderID : " + settings.orderID)
#     ctmpsmUpdateCommand = ['ctmpsm', '-updateajf', settings.orderID, 'FORCEOK']
#     try:
#         splittedLines = commandExecuter(ctmpsmUpdateCommand)
#         logger.info("< {} > ".format(settings.varName) + "\n".join([str(x.decode('ascii')) for x in splittedLines]))
#     except Exception as e:
#         raise


# def sendMailNotification(i_LogFile, i_ErrorFile):
#     blatPath = "D:\\ControlM\\Blat250\\full\\"
#     blatCommand = [blatPath + "blat.exe", blatPath + "alerts.txt", "-subject", "Prod-Force-Ok-Failed! WF = " +
#                    settings.varName + " OrderID = " + settings.orderID,
#                   "-to", "Control-m-open@isracard.co.il", "-attach", i_LogFile, i_ErrorFile ]
#     try:
#         splittedLines = commandExecuter(blatCommand)
#     except Exception as e:
#         pass


# if __name__ == "__main__":
#     localLogger, logFile, errorFile = Utils.loggerUtil()
#     main(sys.argv[1:])
