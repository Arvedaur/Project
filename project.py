# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
# from pprint import pprint
import pymysql.cursors
class info:
    def __init__(self,SP_name,Adress,Con_PM,SCADA_PM,turbine_quantity,loopq):
        """
        This software is intended for SCADA PM application automation
        """
        self._SP_name=SP_name
        self._Adress=Adress
        self._Con_PM=Con_PM
        self._SCADA_PM=SCADA_PM
        #self._type=self._type
        self._turbine_quantity=int(turbine_quantity)
        self._loopq=loopq
        self._type=[]
        self._licences={}
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='django',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        self._var=self.__dict__

        for x,y in enumerate(self._var):
            print(x,y)


        print(type(self.connection))

    def Scada_type(self)    :
        if self._turbine_quantity >11 :
            self._type='VOB'    
            return self._type     
        else:
            self._type='VOC'
            return self._type


    def Databaseshowdown(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `blog_item`"
            cursor.execute(sql,)
            result = cursor.fetchone()
            print((result)


    def network(self):
        print ("Number of the SFP modules are {0}".format((self._loopq)))
        Communication=[]
        if self._type=="VOC":
            Communication.append("Cisco 1921","Cisco 2901","Cisco 4321")
        else:
            Communication.append("Cisco 871")
        return Communication
    def licences(self):
        while True:
            try:
                modbus=int(input('Please kindly choose if there is Elspec or Bachmann Meter : '))
                snmp=int(input('Do you need to see the status of network devices: '))
                Ab=int(input("Do you need to send commands from Allen Bradley:"))
                excel=int(input("Do you need to send commands Excel: "))
                vobcl=int(input("Do you need extra VOB Client Licenses: "))
                lic={'modbus':modbus,'snmp':snmp,'Allen Bradbey':Ab,'Excel':excel,
                     "VOB Client":vobcl}
                order=dict
                print(self.__dict__)
                print(lic)
                break

            finally:
                print('This is the final of the software quantities of the modbus licence is {0}, snmp is {1}'.format(modbus,snmp))
                pass

            
        