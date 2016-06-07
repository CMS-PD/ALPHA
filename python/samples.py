#! /usr/bin/env python

sample = {
    'SingleMuonRun2016B-PromptReco-v1' : {
        'nevents' : 2816842,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'SingleMuonRun2016B-PromptReco-v2' : {
        'nevents' : 18201601,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    
    'DoubleMuonRun2016B-PromptReco-v1' : {
        'nevents' : 4201017,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'DoubleMuonRun2016B-PromptReco-v2' : {
        'nevents' : 19821894,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    
    'SingleElectronRun2016B-PromptReco-v1' : {
        'nevents' : 1422819,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'SingleElectronRun2016B-PromptReco-v2' : {
        'nevents' : 33670715,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    
    'DoubleEGRun2016B-PromptReco-v1' : {
        'nevents' : 5704443,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'DoubleEGRun2016B-PromptReco-v2' : {
        'nevents' : 29217360,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    
    'METRun2016B-PromptReco-v1' : {
        'nevents' : 602650,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'METRun2016B-PromptReco-v2' : {
        'nevents' : 4176245,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    
    'SinglePhotonRun2016B-PromptReco-v1' : {
        'nevents' : 1000000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'SinglePhotonRun2016B-PromptReco-v2' : {
        'nevents' : 1000000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    
    ########## MC ##########
    'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1' : {
        'nevents' : 28696958,
        'xsec'    : 6025.2,
        'kfactor' : 1.,
    },
    
    'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1' : {
        'nevents' : 49877138,
        'xsec'    : 6025.2,
        'kfactor' : 1.,
    },
    
    'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1' : {
        'nevents' : 8434125,
        'xsec'    : 6025.2,
        'kfactor' : 1.,
    },
    
    'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1' : {
        'nevents' : 8683719,
        'xsec'    : 6025.2,
        'kfactor' : 1.,
    },
    
    'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1' : {
        'nevents' : 8045263,
        'xsec'    : 6025.2,
        'kfactor' : 1.,
    },
    
    'DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1' : {
        'nevents' : 4116330,
        'xsec'    : 6025.2,
        'kfactor' : 1.,
    },
    
    'WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1' : {
        'nevents' : 9908534,
        'xsec'    : 61526.7,
        'kfactor' : 1.,
    },
    
    'TTTo2L2Nu_13TeV-powheg_v0_ext1-v1' : {
        'nevents' : 104607105,
        'xsec'    : 831.76*(3./9.)*(3./9.),
        'kfactor' : 1.,
    },
    
    'VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_v0-v1' : {
        'nevents' : 2944584,
        'xsec'    : 1,
        'kfactor' : 1.,
    },
    
    # Signal
    'BulkGravToZZToZlepZhad_narrow_M-600_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-800_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-1000_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-1200_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-1600_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-1800_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-2000_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-3000_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-3500_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-4000_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    'BulkGravToZZToZlepZhad_narrow_M-4500_13TeV-madgraph_PRIVATE-MC_v0-v1' : {
        'nevents' : 10000,
        'xsec'    : 1.,
        'kfactor' : 1.,
    },
    
}





samples = {
    'data_obs' : {
        'order' : 0,
        'files' : ['SingleMuonRun2016B-PromptReco-v1', 'SingleMuonRun2016B-PromptReco-v2', 'SingleElectronRun2016B-PromptReco-v1', 'SingleElectronRun2016B-PromptReco-v2'],
        'fillcolor' : 0,
        'fillstyle' : 1,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Data",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToLL' : {
        'order' : 1,
        'files' : ['DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1'], #'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_v0_ext1-v1', 
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z(ll) + jets",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToLL_HT' : {
        'order' : 1,
        'files' : ['DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v2', 'DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1'],
        'fillcolor' : 418,
        'fillstyle' : 1001,
        'linecolor' : 418,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z(ll) + jets",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToNuNu' : {
        'order' : 1,
        'files' : ['DYJetsToNuNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8-v1'],
        'fillcolor' : 856,
        'fillstyle' : 1001,
        'linecolor' : 856,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z(#nu#nu) + jets",
        'weight': 1.,
        'plot': True,
    },
    'DYJetsToNuNu_HT' : {
        'order' : 1,
        'files' : ['ZJetsToNuNu_HT-100To200_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-200To400_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-400To600_13TeV-madgraph-v1', 'ZJetsToNuNu_HT-600ToInf_13TeV-madgraph-v2'],
        'fillcolor' : 856,
        'fillstyle' : 1001,
        'linecolor' : 856,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "Z(#nu#nu) + jets",
        'weight': 1.,
        'plot': True,
    },
    'WJetsToLNu' : {
        'order' : 2,
        'files' : ['WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_v0-v1'],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W(l#nu) + jets",
        'weight': 1.,
        'plot': True,
    },
    'WJetsToLNu_HT' : {
        'order' : 2,
        'files' : ['WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1'],#'WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1'],
        'fillcolor' : 881,
        'fillstyle' : 1001,
        'linecolor' : 881,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "W(l#nu) + jets",
        'weight': 1.,
        'plot': True,
    },
    'TTbar' : {
        'order' : 3,
        'files' : ['TTTo2L2Nu_13TeV-powheg_v0_ext1-v1'], #, 'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8-v1', 'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8-v2'
        'fillcolor' : 798,
        'fillstyle' : 1001,
        'linecolor' : 798,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "t#bar{t}",#, single t
        'weight': 1.,
        'plot': True,
    },
    'ST' : {
        'order' : 4,
        'files' : ['ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1-v1', 'ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v1', 'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v1', 'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v1', 'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1-v2'],
        'fillcolor' : 801,
        'fillstyle' : 1001,
        'linecolor' : 801,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "ST",
        'weight': 1.,
        'plot': True,
    },
    'VV' : {
        'order' : 5,
        'files' : ['WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZZTo4L_13TeV-amcatnloFXFX-pythia8-v1', 'ZH_HToBB_ZToLL_M125_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8-v1'],
        #'files' : ['WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZZTo4L_13TeV-amcatnloFXFX-pythia8-v1', 'ZH_HToBB_ZToLL_M125_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8-v1'],
        #'files' : ['WW_TuneCUETP8M1_13TeV-pythia8-v1','WZ_TuneCUETP8M1_13TeV-pythia8-v1','ZZ_TuneCUETP8M1_13TeV-pythia8-v1', 'ZH_HToBB_ZToLL_M125_13TeV_amcatnloFXFX_madspin_pythia8-v1', 'ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8-v1'],
        'fillcolor' : 602,
        'fillstyle' : 1001,
        'linecolor' : 602,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "VV, VH",
        'weight': 1.,
        'plot': True,
    },
    'QCD' : {
        'order' : 6,
        'files' : ['QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1', 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-v1'],
        'fillcolor' : 921,
        'fillstyle' : 1001,
        'linecolor' : 921,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "multijet",
        'weight': 1.,
        'plot': True,
    },
    
    # Dummy entry for background sum
    'BkgSum' : {
        'order' : 0,
        'files' : [],
        'fillcolor' : 1,
        'fillstyle' : 3003,
        'linecolor' : 1,
        'linewidth' : 2,
        'linestyle' : 1,
        'label' : "MC stat.",
        'weight': 1.,
        'plot': True,
    },
}
