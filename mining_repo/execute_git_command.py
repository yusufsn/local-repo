import subprocess, re

def execute_command(cmd, work_dir):
	"""Executes a shell command in a subprocess, waiting until it has completed.
 
    :param cmd: Command to execute.
    :param work_dir: Working directory path.
    """
	pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(out, error) = pipe.communicate()
	return out, error
	pipe.wait()

def execute_shell_command(id1, id2, cmd, work_dir):
    """Executes a shell command in a subprocess, waiting until it has completed.
 
    :param cmd: Command to execute.
    :param work_dir: Working directory path.
    """
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    return id1, id2, out, error
    pipe.wait()

repository = "/Users/YusufNugroho/local-repo/"
diff_cmd = "git log --oneline"

diffhist = []
tmp = (str(execute_command(diff_cmd, repository)).replace("(",'').replace("+",'').
	replace("-",'').replace("\\n",'').replace("b'",'').replace("(+)",'').replace("(-)",'').replace(")",'').
	replace("|",'').replace(" => ",'=>').replace("... ",'...').replace("...> ",'...>').
	replace("...=> ",'...=>').replace(" Code ","Code"))
#tmp = re.sub("([a-z])" and "([ ])", r"\1,", tmp)
diffhist.append(str(tmp))

for item in diffhist:
	print (item)