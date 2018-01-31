from CtmJobForceOk import commandExecuter
from CtmJobForceOk import settings

def run(i_LogFile, i_ErrorFile):
    blatPath = "D:\\ControlM\\Blat250\\full\\"
    blatCommand = [blatPath + "blat.exe", blatPath + "alerts.txt", "-subject", "Prod-Force-Ok-Failed! WF = " +
                   settings.varName + " OrderID = " + settings.orderID,
                  "-to", "Control-m-open@isracard.co.il", "-attach", i_LogFile, i_ErrorFile ]
    try:
        splittedLines = commandExecuter.run(blatCommand)
    except Exception as e:
        pass