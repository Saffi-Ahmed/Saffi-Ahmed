# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:05:04 2021

@author: smsaf
"""

# class className():
#     def __init__(self):
#         self.Attribute = 0
            
#     def AnotherFunction(self):
#         Action(s)

class Team:
    def __init__(self,Name,Origin):
        self.TeamName = Name
        self.TeamOrigin = Origin
    def DefineTeamName(self, Name):
        self.TeamName = Name
    def DefineTeamOrigin(self,Origin):
        self.TeamOrigin = Origin
Team1 = Team("Team","Team")

Team2 = Team("Hawks","New York")

print(Team1.TeamName)


Team1.DefineTeamName("Tigers")

print(Team1.TeamName)

print(Team1.TeamOrigin)

Team1.DefineTeamOrigin("Chicago")

print(Team2.TeamName)

print(Team2.TeamOrigin)