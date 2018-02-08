import subprocess as subp
from UsefulUtilities import Utils



def run(commandToExecute):
    logger, _, _ = Utils.loggerUtil()
    try:
        ctmpsmOutput = subp.Popen(commandToExecute, stdout=subp.PIPE, stderr=subp.PIPE, shell=True)
        out, err = ctmpsmOutput.communicate()
        splittedLines = out.splitlines()
        rc = ctmpsmOutput.returncode
        if rc != 0:
            errors = "\n".join([str(x.decode('ascii')) for x in err.splitlines()])
            output = "\n".join([str(x.decode('ascii')) for x in out.splitlines()])
            if errors:
                raise Exception(errors)
            if output:
                raise Exception(output)
            if errors and output:
                raise Exception(output + "\n" + errors)
        return splittedLines
    except Exception as e:
        raise Exception("Something went wrong with the command : " + str(commandToExecute) + "\n" +
                        str(e.args[0]) + "\nExiting with code  9!", 9, logger.name)
