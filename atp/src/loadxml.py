import cimhub.api as cimhub
import cimhub.CIMHubConfig as CIMHubConfig
import os

CASES = [
  {'id': '1783D2A8-1204-4781-A0B4-7A73A2FA6038', 'name': 'IEEE118', 'cim': 'IEEE118_CIM.xml', 'loc': 'IEEE118_CIM_Loc.xml'},
  {'id': '2540AF5C-4F83-4C0F-9577-DEE8CC73BBB3', 'name': 'WECC240', 'cim': 'WECC240_CIM.xml', 'loc': 'IEEE118_CIM_Loc.xml'}
]

basepath = 'c:/src/cimhub/bes/'

if __name__ == '__main__':
  CIMHubConfig.ConfigFromJsonFile (basepath + 'cimhubconfig.json')
  cimhub.clear_db ()

  for row in CASES:
    for tag in ['cim', 'loc']:
      xmlpath = basepath + row[tag]
      if os.path.exists(xmlpath):
        cmd = 'curl -D- -H "Content-Type: application/xml" --upload-file ' + xmlpath + ' -X POST ' + CIMHubConfig.blazegraph_url
        #    print (cmd)
        os.system (cmd)

  cimhub.list_bes ()

