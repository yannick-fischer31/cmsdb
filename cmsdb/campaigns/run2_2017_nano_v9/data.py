# coding: utf-8

"""
CMS datasets from the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# SingleElectron
#

cpn.add_dataset(
    name="data_e_b",
    id=14226251,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=32,
    n_events=60537490,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=14226092,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=59,
    n_events=136637888,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=14227611,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=37,
    n_events=51512837,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_e_e",
    id=14226090,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=51,
    n_events=102122055,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_e_f",
    id=14226476,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=66,
    n_events=128467223,
    aux={
        "era": "F",
    },
)


#
# SingleMuon
#

cpn.add_dataset(
    name="data_mu_b",
    id=14226191,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=79,
    n_events=136300266,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=14226140,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=117,
    n_events=165652756,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14226234,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=47,
    n_events=70361660,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=14235644,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=78,
    n_events=154618774,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_2mu_b",
    id=14226183,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=115,
    n_events=242140980,
    aux={
        "era": "F",
    },
)

#
# Double Muon
#

cpn.add_dataset(
    name="data_doublemu_b",
    id=14233059,
    is_data=True,
    processes=[procs.data_doublemu],
    keys=[
        "/DoubleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=8,
    n_events=14501767,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_doublemu_c",
    id=14233377,
    is_data=True,
    processes=[procs.data_doublemu],
    keys=[
        "/DoubleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=29,
    n_events=49636525,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_doublemu_d",
    id=14233223,
    is_data=True,
    processes=[procs.data_doublemu],
    keys=[
        "/DoubleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=16,
    n_events=23075733,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_doublemu_e",
    id=14237140,
    is_data=True,
    processes=[procs.data_doublemu],
    keys=[
        "/DoubleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=34,
    n_events=51531477,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_doublemu_f",
    id=14237115,
    is_data=True,
    processes=[procs.data_doublemu],
    keys=[
        "/DoubleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=60,
    n_events=79756560,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_doublemu_g",
    id=14247095,
    is_data=True,
    processes=[procs.data_doublemu],
    keys=[
        "/DoubleMuon/Run2017G-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=157,
    n_events=892686175,
    aux={
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_doublemu_h",
    id=14233371,
    is_data=True,
    processes=[procs.data_doublemu],
    keys=[
        "/DoubleMuon/Run2017H-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=7,
    n_events=16142576,
    aux={
        "era": "H",
    },
)

#
# Double EG
#

cpn.add_dataset(
    name="data_doubleeg_b",
    id=14232887,
    is_data=True,
    processes=[procs.data_doubleeg],
    keys=[
        "/DoubleEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=29,
    n_events=58088760,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_doubleeg_c",
    id=14233479,
    is_data=True,
    processes=[procs.data_doubleeg],
    keys=[
        "/DoubleEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=44,
    n_events=65181125,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_doubleeg_d",
    id=14233182,
    is_data=True,
    processes=[procs.data_doubleeg],
    keys=[
        "/DoubleEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=14,
    n_events=25911432,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_doubleeg_e",
    id=14233016,
    is_data=True,
    processes=[procs.data_doubleeg],
    keys=[
        "/DoubleEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=32,
    n_events=56241190,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_doubleeg_f",
    id=14238185,
    is_data=True,
    processes=[procs.data_doubleeg],
    keys=[
        "/DoubleEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=54,
    n_events=74265012,
    aux={
        "era": "F",
    },
)

#
# Muon EG
#

cpn.add_dataset(
    name="data_mueg_b",
    id=14230851,
    processes=[procs.data_mueg],
    is_data=True,
    keys=[
        "/MuonEG/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa
    ],
    n_files=6,
    n_events=4453465,
    aux={
        "era": "B",
    },
)
cpn.add_dataset(
    name="data_mueg_c",
    id=14224831,
    processes=[procs.data_mueg],
    is_data=True,
    keys=[
        "/MuonEG/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa
    ],
    n_files=17,
    n_events=15595214,
    aux={
        "era": "C",
    },
)
cpn.add_dataset(
    name="data_mueg_d",
    id=14225413,
    processes=[procs.data_mueg],
    is_data=True,
    keys=[
        "/MuonEG/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa
    ],
    n_files=13,
    n_events=9164365,
    aux={
        "era": "D",
    },
)
cpn.add_dataset(
    name="data_mueg_e",
    id=14232069,
    processes=[procs.data_mueg],
    is_data=True,
    keys=[
        "/MuonEG/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa
    ],
    n_files=15,
    n_events=19043421,
    aux={
        "era": "E",
    },
)
cpn.add_dataset(
    name="data_mueg_f",
    id=14224832,
    processes=[procs.data_mueg],
    is_data=True,
    keys=[
        "/MuonEG/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",  # noqa
    ],
    n_files=23,
    n_events=25776363,
    aux={
        "era": "F",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_b",
    id=14233603,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=32,
    n_events=38158216,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_tau_c",
    id=14233706,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=45,
    n_events=55416425,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14233103,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=13,
    n_events=20530776,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_e",
    id=14302263,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017E-UL2017_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=36,
    n_events=44316628,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=14232807,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=59,
    n_events=88502118,
    aux={
        "era": "F",
    },
)


#
# MET
#

cpn.add_dataset(
    name="data_met_b",
    id=14225468,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=43,
    n_events=51623474,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_met_c",
    id=14226051,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=53,
    n_events=115906496,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=14230935,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=15,
    n_events=20075033,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_met_e",
    id=14225819,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=48,
    n_events=71418865,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_met_f",
    id=14224849,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=133,
    n_events=177521562,
    aux={
        "era": "F",
    },
)


#
# SinglePhoton
#

cpn.add_dataset(
    name="data_pho_b",
    id=14226103,
    is_data=True,
    processes=[procs.data_pho],
    keys=[
        "/SinglePhoton/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=10,
    n_events=15950935,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_pho_c",
    id=14226292,
    is_data=True,
    processes=[procs.data_pho],
    keys=[
        "/SinglePhoton/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=34,
    n_events=42182948,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_pho_d",
    id=14226047,
    is_data=True,
    processes=[procs.data_pho],
    keys=[
        "/SinglePhoton/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=7,
    n_events=9753462,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_pho_e",
    id=14226326,
    is_data=True,
    processes=[procs.data_pho],
    keys=[
        "/SinglePhoton/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=22,
    n_events=19011446,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_pho_f",
    id=14226332,
    is_data=True,
    processes=[procs.data_pho],
    keys=[
        "/SinglePhoton/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=31,
    n_events=29783015,
    aux={
        "era": "F",
    },
)


#
# JetHT
#

cpn.add_dataset(
    name="data_jetht_b",
    id=14224834,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=33,
    n_events=63043590,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_jetht_c",
    id=14224757,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=66,
    n_events=96264601,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetht_d",
    id=14227117,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=37,
    n_events=46145204,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_jetht_e",
    id=14224755,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=58,
    n_events=89630771,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_jetht_f",
    id=14224838,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=66,
    n_events=115429972,
    aux={
        "era": "F",
    },
)
