# Copyright 2013 Lyman Gillispie
# This code is distributed under the MIT License
# Author: Lyman Gillispie

def _entry_getter(s):
  """Address the string s
  Args: s - Any string
  Returns: linepos(l,w) - function which returns word w on line l
  from s
  """
  lines = s.splitlines()
  def linepos(line, word):
    return lines[line].split()[word]
  return linepos


def input_to_dict(fp):
  """Takes a file-like buffer and converts it from a DEBaM/DETIM
  input file to a python dictionary
  Args: fp - a file object
  Returns: c - dict with info from fp
  """
  s = fp.read()
  return input_to_dicts(s)

def input_to_dicts(s):
  """Convert a string from DEBaM/DETIM input into a python dict
  Args: s - a string
  Return: c - dict with info from s
  """

  linepos = _entry_getter(s)

  c = {}
  c["daysscreenoutput"] = int(linepos(2,0))
  c["inpath"] = str(linepos(3, 0))
  c["outpath"] = str(linepos(4, 0)) 
  c["jdbeg"] = int(linepos(5, 0))
  c["yearbeg"] = int(linepos(5, 1))
  c["jdend"] = int(linepos(6, 0))
  c["yearend"] = int(linepos(6, 1))
  c["disyes"] = int(linepos(7, 0))
  c["calcgridyes"] = int(linepos(8, 0))
  
  c["maxmeltstakes"] = int(linepos(10, 0))
  c["plusminus"] = int(linepos(11, 0))
  c["do_out"] = int(linepos(12, 0)) 

  c["shayes"] = int(linepos(14, 0))
  c["exkyes"] = int(linepos(14, 1))
  c["solyes"] = int(linepos(14, 2))
  c["diryes"] = int(linepos(14, 3))
  c["dir2yes"] = int(linepos(14, 4))
  c["difyes"] = int(linepos(14, 5))
  c["gloyes"] = int(linepos(14, 6))
  c["albyes"] = int(linepos(14, 7))
  c["swbyes"] = int(linepos(14, 8))
  c["linyes"] = int(linepos(14, 9))
  c["loutyes"] = int(linepos(14, 10))
  c["netyes"] = int(linepos(16, 0))
  c["senyes"] = int(linepos(16, 1))
  c["latyes"] = int(linepos(16, 2))
  c["raiyes"] = int(linepos(16, 3))
  c["enbyes"] = int(linepos(16, 4))
  c["melyes"] = int(linepos(16, 5))
  c["ablyes"] = int(linepos(16, 6))
  c["surftempyes"] = int(linepos(16, 7))
  c["posyes"] = int(linepos(16, 8))
  c["ddfyes"] = int(linepos(16, 9))

  c["surfyes"] = int(linepos(17, 0))
  c["snowyes"] = int(linepos(18, 0))
  c["daysnow"] = int(linepos(19, 0))
  c["numbersnowdaysout"] = int(linepos(20, 0))
  c["jdsurface"] = [int(linepos(21, 0)), int(linepos(21,1))]

  c["winterbalyes"] = int(linepos(23, 0))
  c["winterjdbeg"] = int(linepos(24, 0))
  c["winterjdend"] = int(linepos(24, 1))
  c["summerbalyes"] = int(linepos(25, 0))
  c["summerjdbeg"] = int(linepos(26, 0))
  c["summerjdend"] = int(linepos(26, 1))
  c["datesfromfileyes"] = int(linepos(27, 0))
  c["namedatesmassbal"] = str(linepos(28, 0))
  c["beltwidth"] = int(linepos(29, 0))
  c["snow2zeroeachyearyes"] = int(linepos(30, 0))
  c["snowfreeyes"] = int(linepos(31, 0))

  c["cumulmeltyes"] = int(linepos(33, 0))
  c["cm_or_m"] = int(linepos(34, 0))
  c["do_out_area"] = int(linepos(35, 0))
  c["outgridnumber"] = int(linepos(36, 0))
  
  outGridOffset = 39 + c["outgridnumber"]
  if c["outgridnumber"]:
    outgrids = []
    for grid in range(0, c["outgridnumber"]):
      line = 39 + grid
      outgrids.append({
          "name": str(linepos(line, 0)),
          "location": [int(linepos(line, 1)), int(linepos(line, 2))],
          "outglobnet": int(linepos(line, 3))
          })
    c["outgrids"] = outgrids
  else:
    c["outgrids"] = []

  lineposOffset = lambda line, pos: linepos(line + outGridOffset, pos) 
  
  c["methodinisnow"] = int(lineposOffset(1, 0))
  c["methodsnowalbedo"] = int(lineposOffset(2, 0))
  c["methodglobal"] = int(lineposOffset(3, 0))
  c["methodlonginstation"] = int(lineposOffset(4, 0))
  c["methodlongin"] = int(lineposOffset(5, 0))
  c["methodsurftempglac"] = int(lineposOffset(6, 0))

  c["methodturbul"] = int(lineposOffset(8, 0))
  c["method_z0Te"] = int(lineposOffset(9, 0))
  c["methodiceheat"] = int(lineposOffset(10, 0))
  c["methodnegbal"] = int(lineposOffset(11, 0))

  c["scalingyes"] = int(lineposOffset(13, 0))
  c["gamma"] = float(lineposOffset(14, 0))
  c["c_coefficient"] = float(lineposOffset(15, 0))

  c["namedgm"] = str(lineposOffset(17, 0))
  c["namedgmdrain"] = str(lineposOffset(18, 0))
  c["namedgmglac"] = str(lineposOffset(19, 0))
  c["namedgmslope"] = str(lineposOffset(20, 0))
  c["namedgmaspect"] = str(lineposOffset(21, 0))
  c["namedgmskyview"] = str(lineposOffset(22, 0))
  c["namedgmfirn"] = str(lineposOffset(23, 0))
  c["nameinitialsnow"] = str(lineposOffset(24, 0))
  c["nameklima"] = str(lineposOffset(25, 0))

  c["laenge"] = float(lineposOffset(27, 0))
  c["breite"] = float(lineposOffset(28, 0))
  c["reflongitude"] = float(lineposOffset(29, 0))
  c["rowclim"] = int(lineposOffset(30, 0))
  c["colclim"] = int(lineposOffset(31, 0))
  c["climoutsideyes"] = int(lineposOffset(32, 0))
  c["heightclim"] = int(lineposOffset(32, 1))
  c["gridsize"] = int(lineposOffset(33, 0))
  c["timestep"] = int(lineposOffset(34, 0))

  c["formatclimdata"] = int(lineposOffset(36, 0))
  c["maxcol"] = int(lineposOffset(37, 0))

  c["coltemp"] = int(lineposOffset(38, 0))
  c["colhum"] = int(lineposOffset(39, 0))
  c["colwind"] = int(lineposOffset(40, 0))
  c["colglob"] = int(lineposOffset(41, 0))
  c["colref"] = int(lineposOffset(42, 0))
  c["colnet"] = int(lineposOffset(43, 0))
  c["collongin"] = int(lineposOffset(44, 0))
  c["collongout"] = int(lineposOffset(45, 0))
  c["colprec"] = int(lineposOffset(46, 0))
  c["colcloud"] = int(lineposOffset(47, 0))
  c["coltempgradvarying"] = int(lineposOffset(48, 0))
  c["coldis"] = int(lineposOffset(49, 0))

  c["ERAtempshift"] = int(lineposOffset(51, 0))
  c["ERAwindshift"] = int(lineposOffset(52, 0))

  c["methodtempinterpol"] = int(lineposOffset(54, 0))
  c["tempgrad"] = float(lineposOffset(55, 0))
  c["tempscenario"] = int(lineposOffset(56, 0))
  c["precscenario"] = int(lineposOffset(57, 0))
  c["monthtempgradyes"] = int(lineposOffset(59, 0))
  c["monthtempgrad"] = [float(lineposOffset(59,x)) for x in range(1,13)]
  c["monthtempscenyes"] = int(lineposOffset(60, 0))
  c["monthtempscen"] = [float(lineposOffset(60,x)) for x in range(1,13)]
  c["monthprecipscenyes"] = int(lineposOffset(61, 0))
  c["monthprecipscen"] = [float(lineposOffset(61,x)) for x in range(1,13)]


  c["n_albfiles"] = int(lineposOffset(63, 0))
  c["albsnow"] = float(lineposOffset(64, 0))
  c["albslush"] = float(lineposOffset(65, 0))
  c["albice"] = float(lineposOffset(66, 0))
  c["albfirn"] = float(lineposOffset(67, 0))
  c["albrock"] = float(lineposOffset(68, 0))
  c["albmin"] = float(lineposOffset(69, 0))
  c["snowalbincrease"] = float(lineposOffset(70, 0))
  c["albiceproz"] = float(lineposOffset(71, 0))
  c["ndstart"] = int(lineposOffset(72, 0))

  c["split"] = int(lineposOffset(74, 0))
  c["prozdiffuse"] = float(lineposOffset(75, 0))
  c["trans"] = float(lineposOffset(76, 0))
  c["ratio"] = float(lineposOffset(77, 0))
  c["ratiodir2dir"] = float(lineposOffset(78, 0))
  c["surftemplapserate"] = float(lineposOffset(79, 0))
  c["directfromfile"] = int(lineposOffset(80, 0))
  c["pathdirectfile"] = str(lineposOffset(81, 0))
  c["daysdirect"] = int(lineposOffset(82, 0))
  c["slopestation"] = float(lineposOffset(83, 0))

  c["iterstep"] = float(lineposOffset(85, 0))
  c["z0wice"] = float(lineposOffset(86, 0))
  c["dividerz0T"] = float(lineposOffset(87, 0))
  c["dividerz0snow"] = float(lineposOffset(88, 0))
  c["z0proz"] = float(lineposOffset(89, 0))
  c["icez0min"] = float(lineposOffset(90, 0))
  c["icez0max"] = float(lineposOffset(91, 0))

  c["methodprecipinterpol"] = int(lineposOffset(93, 0))
  c["precgrad"] = float(lineposOffset(94, 0))
  c["precgradhigh"] = float(lineposOffset(95, 0))
  c["precgradelev"] = int(lineposOffset(95, 1))
  c["preccorr"] = float(lineposOffset(96, 0))
  c["snowmultiplierglacier"] = float(lineposOffset(97, 0))
  c["snowmultiplierrock"] = float(lineposOffset(98, 0))
  c["threshtemp"] = float(lineposOffset(99, 0))
  c["onlyglacieryes"] = int(lineposOffset(100, 0))
  c["glacierpart"] = float(lineposOffset(101, 0))

  c["nameqcalc"] = str(lineposOffset(103, 0))
  c["nodis"] = int(lineposOffset(104, 0))
  c["firnkons"] = int(lineposOffset(105, 0))
  c["snowkons"] = int(lineposOffset(106, 0))
  c["icekons"] = int(lineposOffset(107, 0))
  c["rockkons"] = int(lineposOffset(108, 0))

  c["qfirnstart"] = float(lineposOffset(110, 0))
  c["qsnowstart"] = float(lineposOffset(111, 0))
  c["qicestart"] = float(lineposOffset(112, 0))
  c["qrockstart"] = float(lineposOffset(113, 0))
  c["qground"] = float(lineposOffset(114, 0))
  c["jdstartr2diff"] = float(lineposOffset(115, 0))

  c["disyesopt"] = int(lineposOffset(117, 0))
  c["optkA"] = str(lineposOffset(118, 0))
  c["startopt1"] = float(lineposOffset(119, 0))
  c["stepopt1"] = float(lineposOffset(120, 0))
  c["anzahlopt1"] = int(lineposOffset(121, 0))
  c["optkB"] = str(lineposOffset(122, 0))
  c["startopt2"] = float(lineposOffset(123, 0))
  c["stepopt2"] = float(lineposOffset(124, 0))
  c["anzahlopt2"] = int(lineposOffset(125, 0))
  c["namematrix"] = str(lineposOffset(126, 0))

  c["percolationyes"] = int(lineposOffset(128, 0))
  c["slushformationyes"] = int(lineposOffset(129, 0))
  c["densificationyes"] = int(lineposOffset(130, 0))
  c["wetstartyes"] = int(lineposOffset(131, 0))
  c["ndepths"] = int(lineposOffset(132, 0))
  c["factinter"] = int(lineposOffset(133, 0))

  c["thicknessfirst"] = float(lineposOffset(135, 0))
  c["thicknessdeep"] = float(lineposOffset(136, 0))
  c["depthdeep"] = float(lineposOffset(137, 0))
  c["denssnow"] = int(lineposOffset(138, 0))
  c["irrwatercontyes"] = int(lineposOffset(139, 0))
  c["irrwatercont"] = float(lineposOffset(140, 0))

  c["factsubsurfout"] = int(lineposOffset(142, 0))
  c["offsetsubsurfout"] = int(lineposOffset(143, 0))

  c["runoffyes"] = int(lineposOffset(145, 0))
  c["superyes"] = int(lineposOffset(145, 1))
  c["wateryes"] = int(lineposOffset(145, 2))
  c["surfwateryes"] = int(lineposOffset(145, 3))
  c["slushyes"] = int(lineposOffset(145, 4))
  c["coldsnowyes"] = int(lineposOffset(145, 5))
  c["coldtotyes"] = int(lineposOffset(145, 6))

  c["ddmethod"] = int(lineposOffset(149, 0))
  c["DDFice"] = float(lineposOffset(150, 0))
  c["DDFsnow"] = float(lineposOffset(151, 0))

  c["meltfactor"] = float(lineposOffset(153, 0))
  c["radfactorice"] = float(lineposOffset(154, 0))
  c["radfactorsnow"] = float(lineposOffset(155, 0))
  c["debrisfactor"] = int(lineposOffset(156, 0))

  c["coordinatesyes"] = int(lineposOffset(158, 0))
  if c["maxmeltstakes"] > 0:
    coordfmt = { 1: int, 2: int, 3: float}
    fmt = coordfmt[c["coordinatesyes"]]
    stake_coords = [
        map(fmt, [lineposOffset(ii,0), lineposOffset(ii,1)])
        for ii in range(159, 159 + c["maxmeltstakes"])]
    c["stake_coords"] = stake_coords
  else:
    c["stake_coords"] = []

  return c
