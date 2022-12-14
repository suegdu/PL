# PL Logging
Personal Python Package for Logging.

<a href="https://github.com/suegdu/PL/releases">Releases.</a>  

<a href="https://github.com/suegdu/PL#Presentation">Initial.</a>  

<a href="https://github.com/suegdu/PL#advanced">Advanced.</a>  

<a href="https://github.com/suegdu/PL#setts-avails">Sett's avails.</a>  

<a href="https://github.com/suegdu/PL#logging-with-a-discord-webhook">Logging with a Discord Webhook.</a>  

<a href="https://github.com/suegdu/PL#print-out-logs">Printing Logs.</a>

Version: 1.0.0  
<h4>Installation:</h4>

```
pip install git+https://github.com/suegdu/PL.git
```

# Presentation
<h4>#main.py :</h4>

```py
import pl

pl.sett.F_name = "LogFile"


pl.Log(cont="Welcome",fl=__file__,lev="INFO")

```

<h4>#LogFile.log :</h4>

```log
[INFO] |[e:\CDR\PL\temp.py] [2022-09-05] [00:06:59.383794] : Welcome
```
# Advanced

<h4>#main.py :</h4>

```py
import pl

pl.sett.F_format = "log" 	# Define The File Extension.(Default: log)
pl.sett.R_date = False 	# Won't Record Date With Logging.

pl.Log(fl=__file__,cont="Welcome",lev="INFO",fn="MyLog")   # Call

```

<h4>#MyLog.log</h4>

```
[INFO] |[e:\CDR\PL\temp.py] [00:30:11.416401] : Welcome
```



For more details about customizing defaults, Check the `sett` Class

# Sett's avails
<h4>#main.py</h4>

```py
import pl


# This is a pre-definition for logging, instead of declaring variables each time while calling the Log function, Define it once at the beginning of your script. It's a sett.

pl.sett.F_format = "log"        # Define The File Extension.(Default: log)
pl.sett.R_date = True       # Will Record Date With Logging.(Default: True)
pl.sett.R_time = False      # Won't Record Time With Logging.(Default: True)
pl.sett.F_name = "Mylogs"      # Define The File Name.(Default: pl_log)

pl.Log(fl=__file__,cont="Welcome",lev="INFO") # Call
#     |
#     |
#     |
# ---------------------------------------------------------------------------------
# Didn't define 'fn' and 'fr' because it's already defined under the sett section.
# As the same role applies to 'R_time' and 'R_date'.
# ---------------------------------------------------------------------------------


```

<h4>#Mylogs.log</h4>

```log
[INFO] |[e:\CDR\PL\temp.py] [2022-09-05] : Welcome
```
# Logging with A Discord Webhook
<h4>#main.py</h4>

```py
import pl

pl.ds_webhook(webhook="i am a discord webhook url.",cont="Welcome",fl=__file__)

```

<h4>#The Discord's Channel</h4>

```log
[INFO] |[e:\CDR\PL\temp.py] [e:\CDR\PL\temp.py] [2022-09-17] [22:44:53.224367] : Welcome
```
<h4>#class: sett</h4>

```py
class sett:
    """An optional Setup for Logging with PL.
Allows you to change the following (These changes will be applied as default from the start of your script while Logging with PL. Allows you to not define these specific variables each time while calling the Logger.):
------------
* F_format(String): The file format, e.g: log.txt, log.log | `F_format = "txt" `

* F_name(String): The file name, e.g: mylogfile | `F_name = "mylogfile"`

* R_date(bool): Determine to show Date section with logging or not, Triggered by `False` / `True`

* R_time(bool): Determine to show Time section with logging or not, Triggered by `False` / `True`

(F_format) Default: `.log`
(F_name) Default: `pl_log`
(R_date) Default: `True`
(R_time) Default: `True`
"""
    F_format:str="log"
    F_name:str=None
    R_date:bool=True
    R_time:bool=True
    
```

# Log Function Definitions

```
--------
* fr: File format.  e.g: `fr="txt"`
* cont: Content to log.  e.g: `cont="Hello"`
* lev: Logging level.  e.g: `lev="INFO"`
* fn: File name.  e.g: `fn="logs"`
* fl: File trace(Path)  e.g: `fl=__file__`
```


# Print Out Logs

<h4>#main.py</h4>

```py
import pl

pl.Out(cont="Welcome",fl=__file__)      # (Basic definition. For more, The Out function does apply to everything that the Log function does, the sett way for example.)
```

<h4>#Console</h4>

```
[INFO] |[e:\CDR\PL\temp.py] [2022-09-05] [01:11:30.771624] : Welcome
```


<a href="mailto:suebusiness@proton.me">Contact</a>  
<a href="https://www.paypal.com/paypalme/suegdu">Donate</a>
