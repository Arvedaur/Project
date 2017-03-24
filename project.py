import os
from pprint import pprint as pp
import pymysql.cursors


class Project:
    def __init__(self, sp_name, location, con_pm, scada_pm, turbine_quantity, turbine_type):
        """
        This software is intended for SCADA PM application automation
        """
        # self._type=[]
        # self._licences={}
        self._SP_name=sp_name
        self._SCADA_PM=scada_pm
        self._Turbine_type=turbine_type
        self._Location=location
        self._Con_PM=con_pm
        self._Turbine_quantity=int(turbine_quantity)
        self._Connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='django',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        # print({k:v for k,v in self.__dict__.items()})
        for x in self.__dict__:
            print(x,self.__dict__[x],sep='<=====>')



    def scada_type(self):
        self._scada_inp=str(input('Please kindly choose one  '
                            'VOB MK4 or VOC '))
        return self._scada_inp

        # if self._Turbine_quantity >11 :
        #     self._type='VOB MK4 Server'
        #     return self._type
        # else:
        #     self._type='VOC'
        #     return self._type

    def ppc_type(self):

        self._ppc_inp=str(input('Please kindly choose one'
                               'PPC MK4 or PPC MK3 '))
        return self._ppc_inp

    def Databaseshowdown(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "select item_code,short_description from blog_item";
            cursor.execute(sql, )
            result = cursor.fetchall()
            print((result))

    def network(self):
        self._loop_inp=int('Please kindly write the number of loops: ')
        print ("Number of the SFP modules are {0}".format((self._loop_inp)))
        self._router={}
        if self._scada_inp[:3]=="VOB":
            while True:
                if self._scada_inp[4:]=='MK4':
            Communication.append("Cisco 1921","Cisco 2901","Cisco 4321")
        else:
            Communication.append("Cisco 871")
        return Communication

    def licences(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "select item_code,short_description from blog_item";
            cursor.execute(sql, )
            result = cursor.fetchall()
            print((result))

        # while True:
        #     try:
        #         modbus=int(input('Please kindly choose if there is Elspec or Bachmann Meter : '))
        #         snmp=int(input('Do you need to see the status of network devices: '))
        #         Ab=int(input("Do you need to send commands from Allen Bradley:"))
        #         excel=int(input("Do you need to send commands Excel: "))
        #         vobcl=int(input("Do you need extra VOB Client Licenses: "))
        #         lic={'modbus':modbus,'snmp':snmp,'Allen Bradbey':Ab,'Excel':excel,
        #              "VOB Client":vobcl}
        #         order=dict
        #         print(self.__dict__)
        #         print(lic)
        #         break
        #
        #     finally:
        #         print('This is the final of the software quantities of the modbus licence is {0}, snmp is {1}'.format(modbus,snmp))
        #         pass
        #
        #
        #