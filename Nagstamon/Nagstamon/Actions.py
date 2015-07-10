# encoding: utf-8

# Nagstamon - Nagios status monitor for your desktop
# Copyright (C) 2008-2014 Henri Wahl <h.wahl@ifw-dresden.de> et al.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

import threading
import time
import datetime
import webbrowser
import subprocess
import re
import sys
import traceback

# import md5 for centreon url autologin encoding
from hashlib import md5

# flag which indicates if already rechecking all
RecheckingAll = False


def StartRefreshLoop(servers=None, output=None, conf=None):
    """
    the everlasting get_status cycle - starts get_status cycle for every server as thread
    """

    for server in servers.values():
        if str(conf.servers[server.get_name()].enabled) == "True":
            server.thread = RefreshLoopOneServer(server=server, output=output, conf=conf)
            server.thread.start()


class RefreshLoopOneServer(threading.Thread):
    """
    one thread for one server per loop
    """
    # kind of a stop please flag, if set to True run() should run no more
    stopped = False
    # Check flag, if set and thread recognizes do a get_status, set to True at the beginning
    doRefresh = True

    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        # include threading mechanism
        threading.Thread.__init__(self, name=self.server.get_name())
        self.setDaemon(1)

    def Stop(self):
        # simply sets the stopped flag to True to let the above while stop this thread when checking next
        self.stopped = True

    def Refresh(self):
        # simply sets the stopped flag to True to let the above while stop this thread when checking next
        self.doRefresh = True

    def run(self):
        """
        loop until end of eternity or until server is stopped
        """
        # do stuff like getting server version and setting some URLs
        self.server.init_config()

        while self.stopped == False:
            # check if we have to leave update interval sleep
            if self.server.count > int(self.conf.update_interval_seconds): self.doRefresh = True

            # self.doRefresh could also been changed by RefreshAllServers()
            if self.doRefresh == True:
                # reset server count
                self.server.count = 0
                # check if server is already checked
                if self.server.isChecking == False:
                    # set server status for status field in popwin
                    self.server.status = "Refreshing (last updated %s)" % time.ctime()
                    gobject.idle_add(self.output.popwin.UpdateStatus, self.server)
                    # get current status
                    server_status = self.server.GetStatus(output=self.output)
                    # GTK/Pango does not like tag brackets < and >, so clean them out from description
                    server_status.error = server_status.error.replace("<", "").replace(">", "").replace("\n", " ")
                    # debug
                    if str(self.conf.debug_mode) == "True":
                        self.server.Debug(server=self.server.get_name(), debug="server return values: " + str(server_status.result) + " " + str(server_status.error))
                    if server_status.error != "":
                        # set server status for status field in popwin
                        self.server.status = "ERROR"
                        # give server status description for future usage
                        self.server.status_description = str(server_status.error)
                        gobject.idle_add(self.output.popwin.UpdateStatus, self.server)
                        # tell gobject to care about GUI stuff - get_status display status
                        # use a flag to prevent all threads at once to write to statusbar label in case
                        # of lost network connectivity - this leads to a mysterious pango crash
                        if self.output.statusbar.isShowingError == False:
                            gobject.idle_add(self.output.RefreshDisplayStatus)
                            if str(self.conf.fullscreen) == "True":
                                gobject.idle_add(self.output.popwin.RefreshFullscreen)
                            # wait a moment
                            time.sleep(5)
                            # change statusbar to the following error message
                            # show error message in statusbar
                            # shorter error message - see https://sourceforge.net/tracker/?func=detail&aid=3017044&group_id=236865&atid=1101373
                            gobject.idle_add(self.output.statusbar.ShowErrorMessage, {"True":"ERROR", "False":"ERR"}[str(self.conf.long_display)])
                            # wait some seconds
                            time.sleep(5)
                            # set statusbar error message status back
                            self.output.statusbar.isShowingError = False
                        # wait a moment
                        time.sleep(10)
                    else:
                        # set server status for status field in popwin
                        self.server.status = "Connected (last updated %s)" % time.ctime()
                        # tell gobject to care about GUI stuff - get_status display status
                        gobject.idle_add(self.output.RefreshDisplayStatus)
                        if str(self.conf.fullscreen) == "True":
                            gobject.idle_add(self.output.popwin.RefreshFullscreen)
                        # wait for the doRefresh flag to be True, if it is, do a get_status
                        if self.doRefresh == True:
                            if str(self.conf.debug_mode) == "True":
                                self.server.Debug(server=self.server.get_name(), debug="Refreshing output - server is already checking: " + str(self.server.isChecking))
                            # reset get_status flag
                            self.doRefresh = False
                            # call Hook() for extra action
                            self.server.Hook()

            else:
                # sleep and count
                time.sleep(1)
                self.server.count += 1
                # call Hook() for extra action
                self.server.Hook()
                # get_status fullscreen window - maybe somehow raw approach
                if str(self.conf.fullscreen) == "True":
                    gobject.idle_add(self.output.popwin.RefreshFullscreen)


def RefreshAllServers(servers=None, output=None, conf=None):
    """
    one refreshing action, starts threads, one per polled server
    """
    # first delete all freshness flags
    output.UnfreshEventHistory()

    for server in servers.values():
        # check if server is already checked
        if server.isChecking == False and str(conf.servers[server.get_name()].enabled) == "True":
            #debug
            if str(conf.debug_mode) == "True":
                server.Debug(server=server.get_name(), debug="Checking server...")

            server.thread.Refresh()

            # set server status for status field in popwin
            server.status = "Refreshing"
            gobject.idle_add(output.popwin.UpdateStatus, server)


class DebugLoop(threading.Thread):
    """
    run and empty debug_queue into debug log file
    """
    # stop flag
    stopped = False

    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]

        # check if DebugLoop is already looping - if it does do not run another one
        for t in threading.enumerate():
            if t.getName() == "DebugLoop":
                # loop gets stopped as soon as it starts - maybe waste
                self.stopped = True

        # initiate Loop
        try:
            threading.Thread.__init__(self, name="DebugLoop")
            self.setDaemon(1)
        except Exception as err:
            print(err)

        # open debug file if needed
        if str(self.conf.debug_to_file) == "True" and self.stopped == False:
            try:
                self.debug_file = open(self.conf.debug_file, "w")
            except Exception as err:
                # if path to file does not exist tell user
                self.output.Dialog(message=err)


    def run(self):
        # as long as debugging is wanted do it
        while self.stopped == False and str(self.conf.debug_mode) == "True":
            # .get() waits until there is something to get - needs timeout in case no debug messages fly in
            debug_string = ""

            try:
                debug_string = self.debug_queue.get(True, 1)
                print(debug_string)
                if str(self.conf.debug_to_file) == "True" and self.__dict__.has_key("debug_file") and debug_string != "":
                    self.debug_file.write(debug_string + "\n")
            except:
                pass

            # if no debugging is needed anymore stop it
            if str(self.conf.debug_mode) == "False": self.stopped = True


    def Stop(self):
        # simply sets the stopped flag to True to let the above while stop this thread when checking next
        self.stopped = True


class Recheck(threading.Thread):
    """
    recheck a clicked service/host
    """
    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        threading.Thread.__init__(self, name=self.server.get_name() + "-Recheck")
        self.setDaemon(1)


    def run(self):
        try:
            self.server.set_recheck(self)
        except:
            self.server.Error(sys.exc_info())


class RecheckAll(threading.Thread):
    """
    recheck all services/hosts
    """
    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        threading.Thread.__init__(self, name="RecheckAll")
        self.setDaemon(1)


    def run(self):
        # get RecheckingAll flag to decide if rechecking all is possible (only if not already running)
        global RecheckingAll

        if RecheckingAll == False:
            RecheckingAll = True
            # put all rechecking threads into one dictionary
            rechecks_dict = dict()
            try:
                # debug
                if str(self.conf.debug_mode) == "True":
                    # workaround, take Debug method from first server reachable
                    self.servers.values()[0].Debug(debug="Recheck all: Rechecking all services on all hosts on all servers...")
                for server in self.servers.values():
                    # only test enabled servers and only if not already
                    if str(self.conf.servers[server.get_name()].enabled) == "True":
                        # set server status for status field in popwin
                        server.status = "Rechecking all started"
                        gobject.idle_add(self.output.popwin.UpdateStatus, server)

                        # special treatment for Check_MK Multisite because there is only one URL call necessary
                        if server.type != "Check_MK Multisite":
                            for host in server.hosts.values():
                                # construct an unique key which refers to rechecking thread in dictionary
                                rechecks_dict[server.get_name() + ": " + host.get_name()] = Recheck(server=server, host=host.get_name(), service="")
                                rechecks_dict[server.get_name() + ": " + host.get_name()].start()
                                # debug
                                if str(self.conf.debug_mode) == "True":
                                    server.Debug(server=server.get_name(), host=host.get_name(), debug="Rechecking...")
                                for service in host.services.values():
                                    # dito
                                    if service.is_passive_only() == True:
                                        continue
                                    rechecks_dict[server.get_name() + ": " + host.get_name() + ": " + service.get_name()] = Recheck(server=server, host=host.get_name(), service=service.get_name())
                                    rechecks_dict[server.get_name() + ": " + host.get_name() + ": " + service.get_name()].start()
                                    # debug
                                    if str(self.conf.debug_mode) == "True":
                                        server.Debug(server=server.get_name(), host=host.get_name(), service=service.get_name(), debug="Rechecking...")
                        else:
                            # Check_MK Multisite does it its own way
                            server.recheck_all()
                # wait until all rechecks have been done
                while len(rechecks_dict) > 0:
                    # debug
                    if str(self.conf.debug_mode) == "True":
                        # once again taking .Debug() from first server
                        self.servers.values()[0].Debug(server=server.get_name(), debug="Recheck all: # of checks which still need to be done: " + str(len(rechecks_dict)))

                    for i in rechecks_dict.copy():
                        # if a thread is stopped pop it out of the dictionary
                        if rechecks_dict[i].isAlive() == False:
                            rechecks_dict.pop(i)
                    # wait a second
                    time.sleep(1)

                # debug
                if str(self.conf.debug_mode) == "True":
                    # once again taking .Debug() from first server
                    self.servers.values()[0].Debug(server=server.get_name(), debug="Recheck all: All servers, hosts and services are rechecked.")
                # reset global flag
                RecheckingAll = False

                # after all and after a short delay to let the monitor apply the recheck requests get_status all to make changes visible soon
                time.sleep(5)
                RefreshAllServers(servers=self.servers, output=self.output, conf=self.conf)
                # do some cleanup
                del rechecks_dict

            except:
                RecheckingAll = False
        else:
            # debug
            if str(self.conf.debug_mode) == "True":
                # once again taking .Debug() from first server
                self.servers.values()[0].Debug(debug="Recheck all: Already rechecking all services on all hosts on all servers.")


class Acknowledge(threading.Thread):
    """
    exceute remote cgi command with parameters from acknowledge dialog
    """
    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        threading.Thread.__init__(self)
        self.setDaemon(1)

    def run(self):
        self.server.set_acknowledge(self)


class Downtime(threading.Thread):
    """
    exceute remote cgi command with parameters from acknowledge dialog
    """
    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        threading.Thread.__init__(self)
        self.setDaemon(1)

    def run(self):
        self.server.set_downtime(self)

"""
def Downtime_get_start_end(server, host):
    # get start and end time from Nagios as HTML - the objectified HTML does not contain the form elements :-(
    # this used to happen in GUI.action_downtime_dialog_show but for a more strict separation it better stays here
    return server.get_start_end(host)
"""

class SubmitCheckResult(threading.Thread):
    """
    exceute remote cgi command with parameters from submit check result dialog
    """
    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        threading.Thread.__init__(self)
        self.setDaemon(1)

    def run(self):
        self.server.set_submit_check_result(self)


class CheckForNewVersion(threading.Thread):
    """
        Check for new version of nagstamon using connections of configured servers
    """
    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        threading.Thread.__init__(self)
        self.setDaemon(1)


    def run(self):
        """
        try all servers respectively their net connections, one of them should be able to connect
        to nagstamon.sourceforge.net
        """

        # debug
        if str(self.output.conf.debug_mode) == "True":
            # once again taking .Debug() from first server
            self.servers.values()[0].Debug(debug="Checking for new version...")


        for s in self.servers.values():
            # if connecton of a server is not yet used do it now
            if s.CheckingForNewVersion == False:
                # set the flag to lock that connection
                s.CheckingForNewVersion = True
                # use IFW server to speed up request and secure via https
                result = s.FetchURL("https://nagstamon.ifw-dresden.de/files-nagstamon/latest_version_" +\
                                     self.output.version, giveback="raw", no_auth=True)
                # remove newline
                version, error = result.result.split("\n")[0], result.error

                # debug
                if str(self.output.conf.debug_mode) == "True":
                    # once again taking .Debug() from first server
                    self.servers.values()[0].Debug(debug="Latest version: " + str(version))

                # if we got a result notify user
                if error == "":
                    if version == self.output.version:
                        version_status = "latest"
                    else:
                        version_status = "out_of_date"
                    # if we got a result reset all servers checkfornewversion flags,
                    # notify the user and break out of the for loop
                    for s in self.servers.values(): s.CheckingForNewVersion = False
                    # do not tell user that the version is latest when starting up nagstamon
                    if not (self.mode == "startup" and version_status == "latest"):
                        # gobject.idle_add is necessary to start gtk stuff from thread
                        gobject.idle_add(self.output.CheckForNewVersionDialog, version_status, version)
                    break
                # reset the servers CheckingForNewVersion flag to allow a later check
                s.CheckingForNewVersion = False


class Notification(threading.Thread):
    """
        Flash statusbar in a threadified way to omit hanging gui
    """
    def __init__(self, **kwds):
        # add all keywords to object, every mode searchs inside for its favorite arguments/keywords
        for k in kwds: self.__dict__[k] = kwds[k]
        threading.Thread.__init__(self)
        self.setDaemon(1)


    def run(self):
        # counter for repeated sound
        soundcount = 0
        # in case of notifying in statusbar do some flashing and honking
        while self.output.Notifying == True:
            # as long as flashing flag is set statusbar flashes until someone takes care
            if self.output.statusbar.Flashing == True:
                if self.output.statusbar.isShowingError == False:
                    # check again because in the mean time this flag could have been changed by NotificationOff()
                    gobject.idle_add(self.output.statusbar.Flash)
            # Ubuntu AppIndicator simulates flashing by brute force
            if str(self.conf.appindicator) == "True":
                if self.output.appindicator.Flashing == True:
                    gobject.idle_add(self.output.appindicator.Flash)
            # if wanted play notification sound, if it should be repeated every minute (2*interval/0.5=interval) do so.
            if str(self.conf.notification_sound) == "True":
                if soundcount == 0:
                    sound = PlaySound(sound=self.sound, Resources=self.Resources, conf=self.conf, servers=self.servers)
                    sound.start()
                    soundcount += 1
                elif str(self.conf.notification_sound_repeat) == "True" and\
                        soundcount >= 2*int(self.conf.update_interval_seconds) and\
                        len([k for k,v in self.output.events_history.items() if v == True]) != 0:
                    soundcount = 0
                else:
                    soundcount += 1
            time.sleep(0.5)
        # reset statusbar
        self.output.statusbar.Label.set_markup(self.output.statusbar.statusbar_labeltext)


def not_empty(x):
    '''
        tiny helper function for BeautifulSoup in GenericServer.py to filter text elements
    '''
    return bool(x.replace('&nbsp;', '').strip())


def OpenNagstamonDownload(output=None):
    """
        Opens Nagstamon Download page after being offered by update check
    """
    # first close popwin
    output.popwin.Close()
    # start browser with URL
    webbrowser.open("https://nagstamon.ifw-dresden.de/download")


def IsFoundByRE(string, pattern, reverse):
    """
    helper for context menu actions in context menu - hosts and services might be filtered out
    also useful for services and hosts and status information
    """
    pattern = re.compile(pattern)
    if len(pattern.findall(string)) > 0:
        if str(reverse) == "True":
            return False
        else:
            return True
    else:
        if str(reverse) == "True":
            return True
        else:
            return False


def HostIsFilteredOutByRE(host, conf=None):
    """
        helper for applying RE filters in Generic.GetStatus()
    """
    try:
        if str(conf.re_host_enabled) == "True":
            return IsFoundByRE(host, conf.re_host_pattern, conf.re_host_reverse)
        # if RE are disabled return True because host is not filtered
        return False
    except:
        import traceback
        traceback.print_exc(file=sys.stdout)


def ServiceIsFilteredOutByRE(service, conf=None):
    """
        helper for applying RE filters in Generic.GetStatus()
    """
    try:
        if str(conf.re_service_enabled) == "True":
            return IsFoundByRE(service, conf.re_service_pattern, conf.re_service_reverse)
        # if RE are disabled return True because host is not filtered
        return False
    except:
        import traceback
        traceback.print_exc(file=sys.stdout)


def StatusInformationIsFilteredOutByRE(status_information, conf=None):
    """
        helper for applying RE filters in Generic.GetStatus()
    """
    try:
        if str(conf.re_status_information_enabled) == "True":
            return IsFoundByRE(status_information, conf.re_status_information_pattern, conf.re_status_information_reverse)
        # if RE are disabled return True because host is not filtered
        return False
    except:
        import traceback
        traceback.print_exc(file=sys.stdout)


def CriticalityIsFilteredOutByRE(criticality, conf=None):
    """
        helper for applying RE filters in Generic.GetStatus()
    """
    try:
        if str(conf.re_criticality_enabled) == "True":
            return IsFoundByRE(criticality, conf.re_criticality_pattern, conf.re_criticality_reverse)
        # if RE are disabled return True because host is not filtered
        return False
    except:
        import traceback
        traceback.print_exc(file=sys.stdout)


def HumanReadableDurationFromSeconds(seconds):
    """
    convert seconds given by Opsview to the form Nagios gives them
    like 70d 3h 34m 34s
    """
    timedelta = str(datetime.timedelta(seconds=int(seconds)))
    try:
        if timedelta.find("day") == -1:
            hms = timedelta.split(":")
            if len(hms) == 1:
                return "0d 0h 0m %ss" % (hms[0])
            elif len(hms) == 2:
                return "0d 0h %sm %ss" % (hms[0], hms[1])
            else:
                return "0d %sh %sm %ss" % (hms[0], hms[1], hms[2])
        else:
            # waste is waste - does anyone need it?
            days, waste, hms = str(timedelta).split(" ")
            hms = hms.split(":")
            return "%sd %sh %sm %ss" % (days, hms[0], hms[1], hms[2])
    except:
        # in case of any error return seconds we got
        return seconds


def HumanReadableDurationFromTimestamp(timestamp):
    """
    Thruk server supplies timestamp of latest state change which
    has to be subtracted from .now()
    """
    try:
        td = datetime.datetime.now() - datetime.datetime.fromtimestamp(int(timestamp))
        h = int(td.seconds / 3600)
        m = int(td.seconds % 3600 / 60)
        s = int(td.seconds % 60)
        return "%sd %sh %sm %ss" % (td.days, h, m ,s)
    except:
        import traceback
        traceback.print_exc(file=sys.stdout)


def MachineSortableDate(raw):
    """
    Monitors gratefully show duration even in weeks and months which confuse the
    sorting of popup window sorting - this functions wants to fix that
    """
    # dictionary for duration date string components
    d = {"M":0, "w":0, "d":0, "h":0, "m":0, "s":0}

    # if for some reason the value is empty/none make it compatible: 0s
    if raw == None: raw = "0s"

    # strip and replace necessary for Nagios duration values,
    # split components of duration into dictionary
    for c in raw.strip().replace("  ", " ").split(" "):
        number, period = c[0:-1],c[-1]
        d[period] = int(number)
        del number, period
    # convert collected duration data components into seconds for being comparable
    return 16934400 * d["M"] + 604800 * d["w"] + 86400 * d["d"] + 3600 * d["h"] + 60 * d["m"] + d["s"]


def MachineSortableDateMultisite(raw):
    """
    Multisite dates/times are so different to the others so it has to be handled separately
    """

    # dictionary for duration date string components
    d = {"M":0, "d":0, "h":0, "m":0, "s":0}

    # if for some reason the value is empty/none make it compatible: 0 sec
    if raw == None: raw = "0 sec"

    # check_mk has different formats - if duration takes too long it changes its scheme
    if "-" in raw and ":" in raw:
        datepart, timepart = raw.split(" ")
        # need to convert years into months for later comparison
        Y, M, D = datepart.split("-")
        d["M"] = int(Y) * 12 + int(M)
        d["d"] = int(D)
        # time does not need to be changed
        h, m, s = timepart.split(":")
        d["h"], d["m"], d["s"] = int(h), int(m), int(s)
        del datepart, timepart, Y, M, D, h, m, s
    else:
        # recalculate a timedelta of the given value
        if "sec" in raw:
            d["s"] = raw.split(" ")[0]
            delta = datetime.datetime.now() - datetime.timedelta(seconds=int(d["s"]))
        elif "min" in raw:
            d["m"] = raw.split(" ")[0]
            delta = datetime.datetime.now() - datetime.timedelta(minutes=int(d["m"]))
        elif "hrs" in raw:
            d["h"] = raw.split(" ")[0]
            delta = datetime.datetime.now() - datetime.timedelta(hours=int(d["h"]))
        elif "days" in raw:
            d["d"] = raw.split(" ")[0]
            delta = datetime.datetime.now() - datetime.timedelta(days=int(d["d"]))
        else:
            delta = datetime.datetime.now()

        Y, M, d["d"], d["h"], d["m"], d["s"] = delta.strftime("%Y %m %d %H %M %S").split(" ")
        # need to convert years into months for later comparison
        d["M"] = int(Y) * 12 + int(M)

    # int-ify d
    for i in d: d[i] = int(d[i])

    # convert collected duration data components into seconds for being comparable
    return 16934400 * d["M"] + 86400 * d["d"] + 3600 * d["h"] + 60 * d["m"] + d["s"]


# unified machine readable date might go back to module Actions
def UnifiedMachineSortableDate(raw):
    """
    Try to compute machine readable date for all types of monitor servers
    """
    # dictionary for duration date string components
    d = {"M":0, "w":0, "d":0, "h":0, "m":0, "s":0}

    # if for some reason the value is empty/none make it compatible: 0s
    if raw == None: raw = "0s"

    # Check_MK style
    if ("-" in raw and ":" in raw) or ("sec" in raw or "min" in raw or "hrs" in raw or "days" in raw):
        # check_mk has different formats - if duration takes too long it changes its scheme
        if "-" in raw and ":" in raw:
            datepart, timepart = raw.split(" ")
            # need to convert years into months for later comparison
            Y, M, D = datepart.split("-")
            d["M"] = int(Y) * 12 + int(M)
            d["d"] = int(D)
            # time does not need to be changed
            h, m, s = timepart.split(":")
            d["h"], d["m"], d["s"] = int(h), int(m), int(s)
            del datepart, timepart, Y, M, D, h, m, s
        else:
            # recalculate a timedelta of the given value
            if "sec" in raw:
                d["s"] = raw.split(" ")[0]
                delta = datetime.datetime.now() - datetime.timedelta(seconds=int(d["s"]))
            elif "min" in raw:
                d["m"] = raw.split(" ")[0]
                delta = datetime.datetime.now() - datetime.timedelta(minutes=int(d["m"]))
            elif "hrs" in raw:
                d["h"] = raw.split(" ")[0]
                delta = datetime.datetime.now() - datetime.timedelta(hours=int(d["h"]))
            elif "days" in raw:
                d["d"] = raw.split(" ")[0]
                delta = datetime.datetime.now() - datetime.timedelta(days=int(d["d"]))
            else:
                delta = datetime.datetime.now()

            Y, M, d["d"], d["h"], d["m"], d["s"] = delta.strftime("%Y %m %d %H %M %S").split(" ")
            # need to convert years into months for later comparison
            d["M"] = int(Y) * 12 + int(M)

        # int-ify d
        for i in d: d[i] = int(d[i])
    else:
        # strip and replace necessary for Nagios duration values,
        # split components of duration into dictionary
        for c in raw.strip().replace("  ", " ").split(" "):
            number, period = c[0:-1],c[-1]
            d[period] = int(number)
            del number, period

    # convert collected duration data components into seconds for being comparable
    return 16934400 * d["M"] + 604800 * d["w"] + 86400 * d["d"] + 3600 * d["h"] + 60 * d["m"] + d["s"]


def MD5ify(string):
    """
    makes something md5y of a given username or password for Centreon web interface access
    """
    return md5(string).hexdigest()


def RunNotificationAction(action):
    """
    run action for notification
    """
    subprocess.Popen(action, shell=True)
