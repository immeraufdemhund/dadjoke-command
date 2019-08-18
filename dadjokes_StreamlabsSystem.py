#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

from Settings_Module import MySettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Dadjoke script"
Website = "https://twitch.tv/immeraufdemhund"
Description = "!dadjoke will post a joke in chat"
Creator = "immeraufdemhund"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
global SettingsFile
SettingsFile = "Settings\settings.json"
global ScriptSettings
ScriptSettings = MySettings(SettingsFile)

def Log(message):
    Parent.Log(ScriptName, message)
    return
#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    try:
        Log('Settings start off as:' + json.dumps(ScriptSettings.__dict__))
    except:
        Log('settings not defined yet')
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    Log('Checking settings directory for ' + ScriptName + ' exists? ' + directory)
    if not os.path.exists(directory):
        Log('directory does not exist, creating settings directory')
        os.makedirs(directory)

    #   Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
    Log('Loading settings for ' + ScriptName + ' found at: ' + SettingsFile)
    ScriptSettings = MySettings(SettingsFile)
    ScriptSettings.Response = "Overwritten pong! ^_^"
    Log('Settings are now:' + json.dumps(ScriptSettings.__dict__))
    return

#---------------------------
#   [Required] Execute Data / Process messages
# data properties: string User, string UserName, string Message, string RawData
# data functions:
#   bool IsChatMessage()
#   bool IsRawaData()
#   bool IsFromTwitch()
#   bool IsFromYoutube()
#   bool IsFromMixer()
#   bool IsFromDiscord()
#   bool IsWhisper()
#   string GetParam(int id)
#   string GetParamCount()
#---------------------------
def Execute(data):
    Log('Settings in use for execute:' + json.dumps(ScriptSettings.__dict__))
    if not data.IsChatMessage():
        return

    if data.GetParam(0).lower() != ScriptSettings.Command:
        return

    if Parent.IsOnUserCooldown(ScriptName,ScriptSettings.Command,data.User):
        Parent.SendStreamMessage("Time Remaining " + str(Parent.GetUserCooldownDuration(ScriptName,ScriptSettings.Command,data.User)))
        return

    if not Parent.HasPermission(data.User,ScriptSettings.Permission,ScriptSettings.Info):
        Parent.Log(ScriptName, 'user "{}" does not have permission to run script'.format(data.User))
        return

    # content = {}
    # content['Accept'] = 'text/plain'
    # result = Parent.GetRequest('https://icanhazdadjoke.com/', content)
    # joke = json.loads(result)['response']
    # Parent.SendStreamMessage(joke)    # Send your message to chat
    # Parent.AddUserCooldown(ScriptName,ScriptSettings.Command,data.User,ScriptSettings.Cooldown)  # Put the command on cooldown
    Parent.SendStreamMessage('hello everyone')
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return
