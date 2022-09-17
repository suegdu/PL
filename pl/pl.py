"""
Creative Commons Legal Code
 
CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
"""
from pathlib import Path
from datetime import datetime
import sys
import requests
sysvalue = sys.exc_info()[1]
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
    #F_file:bool=True

    # Might add an optional specific path to store the log file

class Program:
    """Program frame should not be called. Maintain the functioning class."""
    @classmethod
    def R_return(self,value):
        """Will check and return optional values from the `sett` class."""
        Em:str=str()
        now = datetime.now()
        if value=="date":
         if sett.R_date==False:
            return Em
        if value=="time":
         if sett.R_time==False:
            return Em
        if value=="date":
         if sett.R_date==True:
            return f"[{datetime.date(now)}] "
        if value=="time":
         if sett.R_time==True:
            return f"[{datetime.now().time()}] "
        #if value=="file":
        #    if sett.F_file==False:
        #        return Em
        #if value=="file":
        #    if sett.F_file==True:
        #        return f"[{__file__}] "
    @classmethod
    def pl_write(self,fr:str="log",cont:str="Log from PL",lev:str="INFO",fn:str="pl_log",fl:str=str()):
        """Wrtier frame."""
        f_localrt = fl
        if fl!=str():
            f_localrt = f"[{fl}] "
        date_return = self.R_return("date")
        time_return = self.R_return("time")
        #file_return = self.R_return("file")
        defaccus = f"[{lev}] |{f_localrt}{date_return}{time_return}: {cont}" 
        defpath = Path(__file__).resolve().parent
        if sett.F_format !="log"or fr and sett.F_name !=None:
            try:
             with open(f"{defpath}\\{sett.F_name}.{sett.F_format}","a") as PLprogF:
              PLprogF.write(f"{defaccus}\n")
            except:
                print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
        elif sett.F_format =="log" and sett.F_name==None:
            try:
             with open(f"{defpath}\\{fn}.{fr}","a") as PLprogF:
              PLprogF.write(f"{defaccus}\n")
            except:
                print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
    @classmethod
    def pl_sysout(self,cont:str="Log from PL",lev:str="INFO",fl:str=str()):
        """Printer frame."""
        f_localrt = fl
        if fl!=str():
            f_localrt = f"[{fl}] "
        date_return = self.R_return("date")
        time_return = self.R_return("time")
        defaccus = f"[{lev}] |{f_localrt}{date_return}{time_return}: {cont}" 
        if sett.F_format !="log" and sett.F_name !=None:
            try:
              print(f"{defaccus}\n")
            except:
                print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
        elif sett.F_format =="log" and sett.F_name==None:
            try:
              print(f"{defaccus}\n")
            except:
                print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
    @classmethod
    def pl_dswebhook(self,cont:str="A Log from PL.",lev:str="INFO",fl:str=str(),webhook:str=None,username:str="PL Logging",avatar_url:str=None):
        """Discord Webhook frame.(Note: if you did provide an unvalid avatar_url then the webhook wont be sent without any errors.)"""
        avatar_formats = [".jpeg",".JPEG",".png",".PNG",".JPG",".webp",".WEBP",".psd",".PSD",".svg",'.SVG']
        defdefdom = "https://discord.com/api/webhooks/"
        Tav = avatar_url
        f_localrt = fl
        if fl!=str():
            f_localrt = f"[{fl}] "
        date_return = self.R_return("date")
        time_return = self.R_return("time")
        defaccus = f"[{lev}] |{f_localrt}{date_return}{time_return}: {cont}" 
        loccont  = f"```{defaccus}```"
        if avatar_url == None:
            Tav = "https://i.ibb.co/g9zjJmG/2022-09-17-22-00-51.png"
        if webhook==None:
            return print(f"{__file__}: (PL) Please provide a Webhook link.")
        elif defdefdom not in webhook:
            return print(f"{__file__}: (PL) Please provide a valid Discord Webhook link.")
        #elif avatar_url not in avatar_formats:
        #    return print(f"{__file__}: (PL) Please provide a valid 'Image' link format for the avatar_url.\nSupported formats are:  {' '.join(p for p in avatar_formats)}")
        try:
            data = {
            "content" : f"{loccont}",
            "username" : f"{username}",
            "avatar_url": f"{Tav}"
            }
            requests.post(webhook, json = data)
        except:
            print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
def Log(fr:str="log",cont:str="Log from PL.",lev:str="INFO",fn:str="pl_log",fl:str=str()):
    """
Main frame for logging.
--------
* fr: File format.  e.g: `fr="txt"`
* cont: Content to log.  e.g: `cont="Hello"`
* lev: Logging level.  e.g: `lev="INFO"`
* fn: File name.  e.g: `fn="logs"`
* fl: File trace(Path)  e.g: `fl=__file__`

For some default applies try setting the `sett` class.
    """
    try:
     Program.pl_write(fr=fr,cont=cont,lev=lev,fn=fn,fl=fl)
    except:
    
     print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
def Out(cont:str="Log from PL",lev:str="INFO",fl:str=str()):
    """
Main frame for printing logs.
---
* cont: Content to log.  e.g: `cont="Hello"`
* lev: Logging level.  e.g: `lev="INFO"`
* fl: File trace(Path)  e.g: `fl=__file__`

For some default applies try setting the `sett` class.
"""
    try:
        Program.pl_sysout(cont=cont,lev=lev,fl=fl)
    except:
     print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
def ds_webhook(cont:str="A Log from PL.",lev:str="INFO",fl:str=str(),webhook:str=None,username:str="PL Logging",avatar_url:str=None):
    """
Main frame for logging with Discord's Webhook.
---
* cont: Content to log.  e.g: `cont="Hello"`
* lev: Logging level.  e.g: `lev="INFO"`
* fl: File trace(Path)  e.g: `fl=__file__`
* webhook: A valid Discord Webhook url.
* username: A custom Discord Webhook agent username.
* avatar_url: A custom Discord Webhook agent avatar.(if you did provide an unvalid avatar url it the log wont be sent without any errors, leaves you with unknown exception.)

For some default applies try setting the `sett` class.
"""
    try:
        Program.pl_dswebhook(cont=cont,lev=lev,fl=fl,webhook=webhook,username=username,avatar_url=avatar_url)
    except:
     print(f"{__file__}: (PL) Something went wrong. Possible Tracback: {sysvalue}")
