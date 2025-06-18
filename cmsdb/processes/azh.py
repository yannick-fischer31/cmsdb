# coding: utf-8

"""
azh resonance search signal process definitions
"""

__all__ = [
    "azh",
    "azh_htt_zll",
    "azh_htt_zll_a1000_h330",
    "azh_htt_zll_a1000_h350",
    "azh_htt_zll_a1000_h400",
    "azh_htt_zll_a1000_h450",
    "azh_htt_zll_a1000_h500",
    "azh_htt_zll_a1000_h550",
    "azh_htt_zll_a1000_h600",
    "azh_htt_zll_a1000_h650",
    "azh_htt_zll_a1000_h700",
    "azh_htt_zll_a1000_h750",
    "azh_htt_zll_a1000_h800",
    "azh_htt_zll_a1000_h850",
    "azh_htt_zll_a1000_h900",
    "azh_htt_zll_a1050_h330",
    "azh_htt_zll_a1050_h350",
    "azh_htt_zll_a1050_h400",
    "azh_htt_zll_a1050_h450",
    "azh_htt_zll_a1050_h500",
    "azh_htt_zll_a1050_h550",
    "azh_htt_zll_a1050_h600",
    "azh_htt_zll_a1050_h650",
    "azh_htt_zll_a1050_h700",
    "azh_htt_zll_a1050_h750",
    "azh_htt_zll_a1050_h800",
    "azh_htt_zll_a1050_h850",
    "azh_htt_zll_a1050_h900",
    "azh_htt_zll_a1050_h950",
    "azh_htt_zll_a1100_h1000",
    "azh_htt_zll_a1100_h330",
    "azh_htt_zll_a1100_h350",
    "azh_htt_zll_a1100_h400",
    "azh_htt_zll_a1100_h450",
    "azh_htt_zll_a1100_h500",
    "azh_htt_zll_a1100_h550",
    "azh_htt_zll_a1100_h600",
    "azh_htt_zll_a1100_h650",
    "azh_htt_zll_a1100_h700",
    "azh_htt_zll_a1100_h750",
    "azh_htt_zll_a1100_h800",
    "azh_htt_zll_a1100_h850",
    "azh_htt_zll_a1100_h900",
    "azh_htt_zll_a1100_h950",
    "azh_htt_zll_a1150_h1050",
    "azh_htt_zll_a1150_h330",
    "azh_htt_zll_a1150_h350",
    "azh_htt_zll_a1150_h400",
    "azh_htt_zll_a1150_h450",
    "azh_htt_zll_a1150_h500",
    "azh_htt_zll_a1150_h550",
    "azh_htt_zll_a1150_h600",
    "azh_htt_zll_a1150_h650",
    "azh_htt_zll_a1150_h700",
    "azh_htt_zll_a1150_h750",
    "azh_htt_zll_a1150_h800",
    "azh_htt_zll_a1150_h850",
    "azh_htt_zll_a1150_h900",
    "azh_htt_zll_a1150_h950",
    "azh_htt_zll_a1150_h1000",
    "azh_htt_zll_a1200_h1000",
    "azh_htt_zll_a1200_h1050",
    "azh_htt_zll_a1200_h1100",
    "azh_htt_zll_a1200_h330",
    "azh_htt_zll_a1200_h350",
    "azh_htt_zll_a1200_h400",
    "azh_htt_zll_a1200_h450",    
    "azh_htt_zll_a1200_h500",
    "azh_htt_zll_a1200_h550",
    "azh_htt_zll_a1200_h600",
    "azh_htt_zll_a1200_h650",
    "azh_htt_zll_a1200_h700",
    "azh_htt_zll_a1200_h750",
    "azh_htt_zll_a1200_h800",
    "azh_htt_zll_a1200_h850",
    "azh_htt_zll_a1200_h900",
    "azh_htt_zll_a1200_h950",
    "azh_htt_zll_a1250_h330",
    "azh_htt_zll_a1250_h350",
    "azh_htt_zll_a1250_h400",
    "azh_htt_zll_a1250_h450",
    "azh_htt_zll_a1250_h500",
    "azh_htt_zll_a1250_h550",
    "azh_htt_zll_a1250_h600",
    "azh_htt_zll_a1250_h650",
    "azh_htt_zll_a1250_h700",
    "azh_htt_zll_a1250_h750",
    "azh_htt_zll_a1250_h800",
    "azh_htt_zll_a1250_h850",
    "azh_htt_zll_a1250_h900",
    "azh_htt_zll_a1250_h950",
    "azh_htt_zll_a1250_h1000",
    "azh_htt_zll_a1250_h1050",
    "azh_htt_zll_a1250_h1100",
    "azh_htt_zll_a1250_h1150",
    "azh_htt_zll_a1250_h1000",
    "azh_htt_zll_a1300_h1000",
    "azh_htt_zll_a1300_h1100",
    "azh_htt_zll_a1300_h1200",
    "azh_htt_zll_a1300_h350",
    "azh_htt_zll_a1300_h400",
    "azh_htt_zll_a1300_h500",
    "azh_htt_zll_a1300_h600",
    "azh_htt_zll_a1300_h700",
    "azh_htt_zll_a1300_h800",
    "azh_htt_zll_a1300_h900",
    "azh_htt_zll_a1400_h1000",
    "azh_htt_zll_a1400_h1100",
    "azh_htt_zll_a1400_h1200",
    "azh_htt_zll_a1400_h1300",
    "azh_htt_zll_a1400_h350",
    "azh_htt_zll_a1400_h400",
    "azh_htt_zll_a1400_h500",
    "azh_htt_zll_a1400_h600",
    "azh_htt_zll_a1400_h700",
    "azh_htt_zll_a1400_h800",
    "azh_htt_zll_a1400_h900",
    "azh_htt_zll_a1500_h1000",
    "azh_htt_zll_a1500_h1100",
    "azh_htt_zll_a1500_h1200",
    "azh_htt_zll_a1500_h1300",
    "azh_htt_zll_a1500_h1400",
    "azh_htt_zll_a1500_h350",
    "azh_htt_zll_a1500_h400",
    "azh_htt_zll_a1500_h500",
    "azh_htt_zll_a1500_h600",
    "azh_htt_zll_a1500_h700",
    "azh_htt_zll_a1500_h800",
    "azh_htt_zll_a1500_h900",
    "azh_htt_zll_a1600_h1000",
    "azh_htt_zll_a1600_h1100",
    "azh_htt_zll_a1600_h1200",
    "azh_htt_zll_a1600_h1300",
    "azh_htt_zll_a1600_h1400",
    "azh_htt_zll_a1600_h1500",
    "azh_htt_zll_a1600_h350",
    "azh_htt_zll_a1600_h400",
    "azh_htt_zll_a1600_h500",
    "azh_htt_zll_a1600_h600",
    "azh_htt_zll_a1600_h700",
    "azh_htt_zll_a1600_h800",
    "azh_htt_zll_a1600_h900",
    "azh_htt_zll_a1700_h1000",
    "azh_htt_zll_a1700_h1100",
    "azh_htt_zll_a1700_h1200",
    "azh_htt_zll_a1700_h1300",
    "azh_htt_zll_a1700_h1400",
    "azh_htt_zll_a1700_h1500",
    "azh_htt_zll_a1700_h1600",
    "azh_htt_zll_a1700_h350",
    "azh_htt_zll_a1700_h400",
    "azh_htt_zll_a1700_h500",
    "azh_htt_zll_a1700_h600",
    "azh_htt_zll_a1700_h700",
    "azh_htt_zll_a1700_h800",
    "azh_htt_zll_a1700_h900",
    "azh_htt_zll_a1800_h1000",
    "azh_htt_zll_a1800_h1100",
    "azh_htt_zll_a1800_h1200",
    "azh_htt_zll_a1800_h1300",
    "azh_htt_zll_a1800_h1400",
    "azh_htt_zll_a1800_h1500",
    "azh_htt_zll_a1800_h1600",
    "azh_htt_zll_a1800_h1700",
    "azh_htt_zll_a1800_h350",
    "azh_htt_zll_a1800_h400",
    "azh_htt_zll_a1800_h500",
    "azh_htt_zll_a1800_h600",
    "azh_htt_zll_a1800_h700",
    "azh_htt_zll_a1800_h800",
    "azh_htt_zll_a1800_h900",
    "azh_htt_zll_a1900_h1000",
    "azh_htt_zll_a1900_h1100",
    "azh_htt_zll_a1900_h1200",
    "azh_htt_zll_a1900_h1300",
    "azh_htt_zll_a1900_h1400",
    "azh_htt_zll_a1900_h1500",
    "azh_htt_zll_a1900_h1600",
    "azh_htt_zll_a1900_h1700",
    "azh_htt_zll_a1900_h1800",
    "azh_htt_zll_a1900_h350",
    "azh_htt_zll_a1900_h400",
    "azh_htt_zll_a1900_h500",
    "azh_htt_zll_a1900_h600",
    "azh_htt_zll_a1900_h700",
    "azh_htt_zll_a1900_h800",
    "azh_htt_zll_a1900_h900",
    "azh_htt_zll_a2000_h1000",
    "azh_htt_zll_a2000_h1100",
    "azh_htt_zll_a2000_h1200",
    "azh_htt_zll_a2000_h1300",
    "azh_htt_zll_a2000_h1400",
    "azh_htt_zll_a2000_h1500",
    "azh_htt_zll_a2000_h1600",
    "azh_htt_zll_a2000_h1700",
    "azh_htt_zll_a2000_h1800",
    "azh_htt_zll_a2000_h1900",
    "azh_htt_zll_a2000_h350",
    "azh_htt_zll_a2000_h400",
    "azh_htt_zll_a2000_h500",
    "azh_htt_zll_a2000_h600",
    "azh_htt_zll_a2000_h700",
    "azh_htt_zll_a2000_h800",
    "azh_htt_zll_a2000_h900",
    "azh_htt_zll_a2100_h1000",
    "azh_htt_zll_a2100_h1100",
    "azh_htt_zll_a2100_h1200",
    "azh_htt_zll_a2100_h1300",
    "azh_htt_zll_a2100_h1400",
    "azh_htt_zll_a2100_h1500",
    "azh_htt_zll_a2100_h1600",
    "azh_htt_zll_a2100_h1700",
    "azh_htt_zll_a2100_h1800",
    "azh_htt_zll_a2100_h1900",
    "azh_htt_zll_a2100_h2000",
    "azh_htt_zll_a2100_h350",
    "azh_htt_zll_a2100_h400",
    "azh_htt_zll_a2100_h500",
    "azh_htt_zll_a2100_h600",
    "azh_htt_zll_a2100_h700",
    "azh_htt_zll_a2100_h800",
    "azh_htt_zll_a2100_h900",
    "azh_htt_zll_a430_h330",
    "azh_htt_zll_a450_h330",
    "azh_htt_zll_a450_h350",
    "azh_htt_zll_a500_h330",
    "azh_htt_zll_a500_h350",
    "azh_htt_zll_a500_h370",
    "azh_htt_zll_a500_h400",
    "azh_htt_zll_a550_h330",
    "azh_htt_zll_a550_h350",
    "azh_htt_zll_a550_h400",
    "azh_htt_zll_a550_h450",
    "azh_htt_zll_a600_h330",
    "azh_htt_zll_a600_h350",
    "azh_htt_zll_a600_h400",
    "azh_htt_zll_a600_h450",
    "azh_htt_zll_a600_h500",
    "azh_htt_zll_a650_h330",
    "azh_htt_zll_a650_h350",
    "azh_htt_zll_a650_h400",
    "azh_htt_zll_a650_h450",
    "azh_htt_zll_a650_h500",
    "azh_htt_zll_a650_h550",
    "azh_htt_zll_a700_h330",
    "azh_htt_zll_a700_h350",
    "azh_htt_zll_a700_h370",
    "azh_htt_zll_a700_h400",
    "azh_htt_zll_a700_h450",
    "azh_htt_zll_a700_h500",
    "azh_htt_zll_a700_h550",
    "azh_htt_zll_a700_h600",
    "azh_htt_zll_a750_h330",
    "azh_htt_zll_a750_h350",
    "azh_htt_zll_a750_h400",
    "azh_htt_zll_a750_h450",
    "azh_htt_zll_a750_h500",
    "azh_htt_zll_a750_h550",
    "azh_htt_zll_a750_h600",
    "azh_htt_zll_a750_h650",
    "azh_htt_zll_a800_h330",
    "azh_htt_zll_a800_h350",
    "azh_htt_zll_a800_h400",
    "azh_htt_zll_a800_h450",
    "azh_htt_zll_a800_h500",
    "azh_htt_zll_a800_h550",
    "azh_htt_zll_a800_h600",
    "azh_htt_zll_a800_h650",
    "azh_htt_zll_a800_h700",
    "azh_htt_zll_a850_h330",
    "azh_htt_zll_a850_h350",
    "azh_htt_zll_a850_h400",
    "azh_htt_zll_a850_h450",
    "azh_htt_zll_a850_h500",
    "azh_htt_zll_a850_h550",
    "azh_htt_zll_a850_h600",
    "azh_htt_zll_a850_h650",
    "azh_htt_zll_a850_h700",
    "azh_htt_zll_a850_h750",
    "azh_htt_zll_a900_h330",
    "azh_htt_zll_a900_h350",
    "azh_htt_zll_a900_h370",
    "azh_htt_zll_a900_h400",
    "azh_htt_zll_a900_h450",
    "azh_htt_zll_a900_h550",
    "azh_htt_zll_a900_h500",
    "azh_htt_zll_a900_h600",
    "azh_htt_zll_a900_h650",
    "azh_htt_zll_a900_h700",
    "azh_htt_zll_a900_h750",
    "azh_htt_zll_a900_h800",
    "azh_htt_zll_a950_h330",
    "azh_htt_zll_a950_h350",
    "azh_htt_zll_a950_h400",
    "azh_htt_zll_a950_h450",
    "azh_htt_zll_a950_h500",
    "azh_htt_zll_a950_h550",
    "azh_htt_zll_a950_h600",
    "azh_htt_zll_a950_h650",
    "azh_htt_zll_a950_h700",
    "azh_htt_zll_a950_h750",
    "azh_htt_zll_a950_h800",
    "azh_htt_zll_a950_h850",
]

from order import Process


azh = Process(
    name="azh",
    label=r"AtoZH",
    id=1000000,
<<<<<<< HEAD
    xsecs={
    13: Number(0.1),
    13.6: Number(0.1)
},  # TODO
=======
>>>>>>> Update
)

#
# A->ZH->lltt
#

azh_htt_zll = azh.add_process(
    name="azh_htt_zll",
    label=azh.label,
    id=1000001,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 330$ GeV)",
    id=1000002,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 350$ GeV)",
    id=1000003,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 400$ GeV)",
    id=1000004,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 450$ GeV)",
    id=1000005,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 500$ GeV)",
    id=1000006,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 550$ GeV)",
    id=1000007,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 600$ GeV)",
    id=1000008,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 650$ GeV)",
    id=1000009,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 700$ GeV)",
    id=1000010,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 750$ GeV)",
    id=1000011,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 800$ GeV)",
    id=1000012,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 850$ GeV)",
    id=1000013,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 900$ GeV)",
    id=1000014,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 330$ GeV)",
    id=1000015,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 350$ GeV)",
    id=1000016,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 400$ GeV)",
    id=1000017,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 450$ GeV)",
    id=1000018,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 500$ GeV)",
    id=1000019,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 550$ GeV)",
    id=1000020,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 600$ GeV)",
    id=1000021,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1050_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 650$ GeV)",
    id=1000264,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 700$ GeV)",
    id=1000022,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 750$ GeV)",
    id=1000023,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 800$ GeV)",
    id=1000024,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 850$ GeV)",
    id=1000025,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 900$ GeV)",
    id=1000026,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1050_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 950$ GeV)",
    id=1000027,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 1000$ GeV)",
    id=1000028,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 330$ GeV)",
    id=1000029,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 350$ GeV)",
    id=1000030,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 400$ GeV)",
    id=1000031,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 450$ GeV)",
    id=1000032,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 500$ GeV)",
    id=1000033,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 550$ GeV)",
    id=1000034,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 600$ GeV)",
    id=1000035,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 650$ GeV)",
    id=1000036,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 700$ GeV)",
    id=1000037,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 750$ GeV)",
    id=1000038,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 800$ GeV)",
    id=1000039,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 850$ GeV)",
    id=1000040,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 900$ GeV)",
    id=1000041,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1100_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 950$ GeV)",
    id=1000042,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 1050$ GeV)",
    id=1000043,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 330$ GeV)",
    id=1000044,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 350$ GeV)",
    id=1000045,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1150_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 400$ GeV)",
    id=1000266,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 450$ GeV)",
    id=1000046,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1150_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 500$ GeV)",
    id=1000267,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 550$ GeV)",
    id=1000047,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1150_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 600$ GeV)",
    id=1000268,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 650$ GeV)",
    id=1000048,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1150_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 700$ GeV)",
    id=1000269,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 750$ GeV)",
    id=1000049,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1150_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 800$ GeV)",
    id=1000270,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 850$ GeV)",
    id=1000050,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1150_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 900$ GeV)",
    id=1000271,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1150_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 950$ GeV)",
    id=1000051,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1150_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 1000$ GeV)",
    id=1000272,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1000$ GeV)",
    id=1000052,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1200_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1050$ GeV)",
    id=1000273,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1100$ GeV)",
    id=1000053,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 330$ GeV)",
    id=1000054,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 350$ GeV)",
    id=1000055,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 400$ GeV)",
    id=1000056,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1200_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 450$ GeV)",
    id=1000274,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 500$ GeV)",
    id=1000057,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1200_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 550$ GeV)",
    id=1000275,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 600$ GeV)",
    id=1000058,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1200_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 650$ GeV)",
    id=1000276,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 700$ GeV)",
    id=1000059,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1200_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 750$ GeV)",
    id=1000277,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 800$ GeV)",
    id=1000060,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 850$ GeV)",
    id=1000061,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1200_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 900$ GeV)",
    id=1000062,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1200_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 950$ GeV)",
    id=1000278,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 330$ GeV)",
    id=1000283,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 350$ GeV)",
    id=1000284,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 400$ GeV)",
    id=1000285,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 450$ GeV)",
    id=1000286,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 500$ GeV)",
    id=1000287,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 550$ GeV)",
    id=1000288,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 600$ GeV)",
    id=1000289,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 650$ GeV)",
    id=1000290,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 700$ GeV)",
    id=1000291,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 750$ GeV)",
    id=1000292,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 800$ GeV)",
    id=1000293,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 850$ GeV)",
    id=1000294,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 900$ GeV)",
    id=1000295,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 950$ GeV)",
    id=1000296,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1000$ GeV)",
    id=1000279,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1050$ GeV)",
    id=1000280,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1100$ GeV)",
    id=1000281,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1250_h1150 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1150",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1150$ GeV)",
    id=1000282,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1000$ GeV)",
    id=1000063,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1100$ GeV)",
    id=1000064,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1200$ GeV)",
    id=1000065,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 350$ GeV)",
    id=1000066,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 400$ GeV)",
    id=1000067,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 500$ GeV)",
    id=1000068,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 600$ GeV)",
    id=1000069,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 700$ GeV)",
    id=1000070,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 800$ GeV)",
    id=1000071,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1300_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 900$ GeV)",
    id=1000072,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1000$ GeV)",
    id=1000073,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1100$ GeV)",
    id=1000074,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1200$ GeV)",
    id=1000075,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1300$ GeV)",
    id=1000076,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 350$ GeV)",
    id=1000077,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 400$ GeV)",
    id=1000078,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 500$ GeV)",
    id=1000079,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 600$ GeV)",
    id=1000080,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 700$ GeV)",
    id=1000081,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 800$ GeV)",
    id=1000082,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1400_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 900$ GeV)",
    id=1000083,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1000$ GeV)",
    id=1000084,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1100$ GeV)",
    id=1000085,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1200$ GeV)",
    id=1000086,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1300$ GeV)",
    id=1000087,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1400$ GeV)",
    id=1000088,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 350$ GeV)",
    id=1000089,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 400$ GeV)",
    id=1000090,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 500$ GeV)",
    id=1000091,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 600$ GeV)",
    id=1000092,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 700$ GeV)",
    id=1000093,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1500_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 800$ GeV)",
    id=1000297,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1500_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 900$ GeV)",
    id=1000094,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1000$ GeV)",
    id=1000095,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1100$ GeV)",
    id=1000096,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1200$ GeV)",
    id=1000097,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1300$ GeV)",
    id=1000098,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1400$ GeV)",
    id=1000099,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1500$ GeV)",
    id=1000100,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 350$ GeV)",
    id=1000101,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 400$ GeV)",
    id=1000102,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 500$ GeV)",
    id=1000103,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 600$ GeV)",
    id=1000104,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1600_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 700$ GeV)",
    id=1000298,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a1600_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 800$ GeV)",
    id=1000299,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1600_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 900$ GeV)",
    id=1000105,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1000$ GeV)",
    id=1000106,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1100$ GeV)",
    id=1000107,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1200$ GeV)",
    id=1000108,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1300$ GeV)",
    id=1000109,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1400$ GeV)",
    id=1000110,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1500$ GeV)",
    id=1000111,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1600$ GeV)",
    id=1000112,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 350$ GeV)",
    id=1000113,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 400$ GeV)",
    id=1000114,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 500$ GeV)",
    id=1000115,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 600$ GeV)",
    id=1000116,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 700$ GeV)",
    id=1000117,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 800$ GeV)",
    id=1000118,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1700_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 900$ GeV)",
    id=1000119,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1000$ GeV)",
    id=1000120,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1100$ GeV)",
    id=1000121,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1200$ GeV)",
    id=1000122,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1300$ GeV)",
    id=1000123,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1400$ GeV)",
    id=1000124,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1500$ GeV)",
    id=1000125,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1600$ GeV)",
    id=1000126,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1700$ GeV)",
    id=1000127,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 350$ GeV)",
    id=1000128,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 400$ GeV)",
    id=1000129,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 500$ GeV)",
    id=1000130,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 600$ GeV)",
    id=1000131,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 700$ GeV)",
    id=1000132,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 800$ GeV)",
    id=1000133,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1800_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 900$ GeV)",
    id=1000134,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1000$ GeV)",
    id=1000135,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1100$ GeV)",
    id=1000136,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1200$ GeV)",
    id=1000137,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1300$ GeV)",
    id=1000138,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1400$ GeV)",
    id=1000139,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1500$ GeV)",
    id=1000140,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1600$ GeV)",
    id=1000141,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1700$ GeV)",
    id=1000142,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1800$ GeV)",
    id=1000143,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 350$ GeV)",
    id=1000144,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 400$ GeV)",
    id=1000145,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 500$ GeV)",
    id=1000146,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 600$ GeV)",
    id=1000147,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 700$ GeV)",
    id=1000148,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 800$ GeV)",
    id=1000149,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a1900_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 900$ GeV)",
    id=1000150,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1000$ GeV)",
    id=1000151,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1100$ GeV)",
    id=1000152,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1200$ GeV)",
    id=1000153,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1300$ GeV)",
    id=1000154,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1400$ GeV)",
    id=1000155,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a2000_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1500$ GeV)",
    id=1000300,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1600$ GeV)",
    id=1000156,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1700$ GeV)",
    id=1000157,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1800$ GeV)",
    id=1000158,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1900$ GeV)",
    id=1000159,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 350$ GeV)",
    id=1000160,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 400$ GeV)",
    id=1000161,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 500$ GeV)",
    id=1000162,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 600$ GeV)",
    id=1000163,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 700$ GeV)",
    id=1000164,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 800$ GeV)",
    id=1000165,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 900$ GeV)",
    id=1000166,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1000$ GeV)",
    id=1000167,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1100$ GeV)",
    id=1000168,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1200$ GeV)",
    id=1000169,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1300$ GeV)",
    id=1000170,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1400$ GeV)",
    id=1000171,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1500$ GeV)",
    id=1000172,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a2100_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1600$ GeV)",
    id=1000301,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1700$ GeV)",
    id=1000173,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1800$ GeV)",
    id=1000174,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1900$ GeV)",
    id=1000175,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h2000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h2000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 2000$ GeV)",
    id=1000176,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 350$ GeV)",
    id=1000177,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 400$ GeV)",
    id=1000178,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 500$ GeV)",
    id=1000179,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 600$ GeV)",
    id=1000180,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 700$ GeV)",
    id=1000181,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 800$ GeV)",
    id=1000182,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a2100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 900$ GeV)",
    id=1000183,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a430_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a430_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 430$ GeV, $m_H = 330$ GeV)",
    id=1000184,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a450_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 330$ GeV)",
    id=1000185,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a450_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 350$ GeV)",
    id=1000186,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a500_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 330$ GeV)",
    id=1000187,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 350$ GeV)",
    id=1000188,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a500_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 370$ GeV)",
    id=1000189,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 400$ GeV)",
    id=1000190,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a550_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 330$ GeV)",
    id=1000191,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a550_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 350$ GeV)",
    id=1000192,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a550_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 400$ GeV)",
    id=1000193,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a550_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 450$ GeV)",
    id=1000194,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a600_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 330$ GeV)",
    id=1000195,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 350$ GeV)",
    id=1000196,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 400$ GeV)",
    id=1000197,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a600_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 450$ GeV)",
    id=1000198,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 500$ GeV)",
    id=1000199,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a650_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 330$ GeV)",
    id=1000200,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a650_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 350$ GeV)",
    id=1000201,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a650_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 400$ GeV)",
    id=1000202,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a650_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 450$ GeV)",
    id=1000203,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a650_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 500$ GeV)",
    id=1000204,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a650_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 550$ GeV)",
    id=1000205,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a700_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 330$ GeV)",
    id=1000206,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 350$ GeV)",
    id=1000207,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a700_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 370$ GeV)",
    id=1000208,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 400$ GeV)",
    id=1000209,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a700_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 450$ GeV)",
    id=1000210,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 500$ GeV)",
    id=1000211,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a700_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 550$ GeV)",
    id=1000212,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
)

azh_htt_zll_a700_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 600$ GeV)",
    id=1000302,
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 330$ GeV)",
    id=1000213,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 350$ GeV)",
    id=1000214,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 400$ GeV)",
    id=1000215,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 450$ GeV)",
    id=1000216,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 500$ GeV)",
    id=1000217,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 550$ GeV)",
    id=1000218,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 600$ GeV)",
    id=1000219,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a750_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 650$ GeV)",
    id=1000220,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 330$ GeV)",
    id=1000221,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 350$ GeV)",
    id=1000222,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 400$ GeV)",
    id=1000223,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 450$ GeV)",
    id=1000224,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 500$ GeV)",
    id=1000225,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 550$ GeV)",
    id=1000226,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 600$ GeV)",
    id=1000227,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 650$ GeV)",
    id=1000228,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 700$ GeV)",
    id=1000229,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 330$ GeV)",
    id=1000230,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 350$ GeV)",
    id=1000231,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 400$ GeV)",
    id=1000232,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 450$ GeV)",
    id=1000233,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 500$ GeV)",
    id=1000234,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 550$ GeV)",
    id=1000235,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 600$ GeV)",
    id=1000236,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 650$ GeV)",
    id=1000237,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 700$ GeV)",
    id=1000238,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a850_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 750$ GeV)",
    id=1000239,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 330$ GeV)",
    id=1000240,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 350$ GeV)",
    id=1000241,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 370$ GeV)",
    id=1000242,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 400$ GeV)",
    id=1000243,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 450$ GeV)",
    id=1000244,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 550$ GeV)",
    id=1000245,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 500$ GeV)",
    id=1000246,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 600$ GeV)",
    id=1000247,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 650$ GeV)",
    id=1000248,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 700$ GeV)",
    id=1000249,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 750$ GeV)",
    id=1000250,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 800$ GeV)",
    id=1000251,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 330$ GeV)",
    id=1000252,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 350$ GeV)",
    id=1000253,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 400$ GeV)",
    id=1000254,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 450$ GeV)",
    id=1000255,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 500$ GeV)",
    id=1000256,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 550$ GeV)",
    id=1000257,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 600$ GeV)",
    id=1000258,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 650$ GeV)",
    id=1000259,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 700$ GeV)",
    id=1000260,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 750$ GeV)",
    id=1000261,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 800$ GeV)",
    id=1000262,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)

azh_htt_zll_a950_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 850$ GeV)",
    id=1000263,
<<<<<<< HEAD
    xsecs={
        13: Number(0.1),
        13.6: Number(0.1)
    },  # TODO
=======
>>>>>>> Update
)
