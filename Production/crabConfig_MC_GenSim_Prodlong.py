from CRABClient.UserUtilities import config 
config = config()

config.General.requestName = 'DYtoTauTautomuhad_Prodlong'
config.General.workArea = 'crab_projects'
config.General.transferLogs=True

#config.JobType.pluginName = 'Analysis'
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'Production/DYtoTauTautomuhad_cfi_GEN_SIM_VALIDATION.py'
config.JobType.generator = 'lhe'

config.Data.primaryDataset = 'DYtoTauTau'
#config.Data.inputDBS = 'global'
config.Data.splitting =  'EventBased'
config.Data.unitsPerJob = 50000
NJOBS = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFN = '/store/user/inugent/'

config.Data.publication = True
config.Data.publishDataName = 'DYtoTauTautomuhad_Prodlong'
#config.Data.ignoreLocality = True

config.User.voGroup = 'dcms'

config.Site.storageSite = 'T2_DE_RWTH'
config.Site.whitelist = ["T2_DE_RWTH"]
