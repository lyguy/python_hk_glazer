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
  Returns: config - dict with info from fp
  """
  s = fp.read()
  return input_to_dicts(s)

def input_to_dicts(s):
  """Convert a string from DEBaM/DETIM input into a python dict
  Args: s - a string
  Return: config - dict with info from s
  """

  linepos = _entry_getter(s)

  config = {}
  config["daysscreenoutput"] = int(linepos(2,0))
  config["inpath"] = str(linepos(3, 0))
  config["outpath"] = str(linepos(4, 0)) 
  config["jdbeg"] = int(linepos(5, 0))
  config["yearbeg"] = int(linepos(5, 1))
  config["jdend"] = int(linepos(6, 0))
  config["yearend"] = int(linepos(6, 1))
  config["disyes"] = int(linepos(7, 0))
  config["calcgridyes"] = int(linepos(8, 0))
  
  config["maxmeltstakes"] = int(linepos(10, 0))
  config["plusminus"] = int(linepos(11, 0))
  config["do_out"] = int(linepos(12, 0)) 

  config["shayes"] = int(linepos(14, 0))
  config["exkyes"] = int(linepos(14, 1))
  config["solyes"] = int(linepos(14, 2))
  config["diryes"] = int(linepos(14, 3))
  config["dir2yes"] = int(linepos(14, 4))
  config["difyes"] = int(linepos(14, 5))
  config["gloyes"] = int(linepos(14, 6))
  config["albyes"] = int(linepos(14, 7))
  config["swbyes"] = int(linepos(14, 8))
  config["linyes"] = int(linepos(14, 9))
  config["loutyes"] = int(linepos(14, 10))
  config["netyes"] = int(linepos(16, 0))
  config["senyes"] = int(linepos(16, 1))
  config["latyes"] = int(linepos(16, 2))
  config["raiyes"] = int(linepos(16, 3))
  config["enbyes"] = int(linepos(16, 4))
  config["melyes"] = int(linepos(16, 5))
  config["ablyes"] = int(linepos(16, 6))
  config["surftempyes"] = int(linepos(16, 7))
  config["posyes"] = int(linepos(16, 8))
  config["ddfyes"] = int(linepos(16, 9))

  config["surfyes"] = int(linepos(17, 0))
  config["snowyes"] = int(linepos(18, 0))
  config["daysnow"] = int(linepos(19, 0))
  config["numbersnowdaysout"] = int(linepos(20, 0))
  config["jdsurface"] = [int(linepos(21, 0)), int(linepos(21,1))]

  config["winterbalyes"] = int(linepos(23, 0))
  config["winterjdbeg"] = int(linepos(24, 0))
  config["winterjdend"] = int(linepos(24, 1))
  config["summerbalyes"] = int(linepos(25, 0))
  config["summerjdbeg"] = int(linepos(26, 0))
  config["summerjdend"] = int(linepos(26, 1))
  config["datesfromfileyes"] = int(linepos(27, 0))
  config["namedatesmassbal"] = str(linepos(28, 0))
  config["beltwidth"] = int(linepos(20, 0))
  config["snow2zeroeachyearyes"] = int(linepos(30, 0))
  config["snowfreeyes"] = int(linepos(31, 0))

  config["cumulmeltyes"] = int(linepos(33, 0))
  config["cm_or_m"] = int(linepos(34, 0))
  config["do_out_area"] = int(linepos(35, 0))
  config["outgridnumber"] = int(linepos(36, 0))
  
  outGridOffset = 39 + config["outgridnumber"]
  if config["outgridnumber"]:
    outgrids = []
    for grid in range(0, config["outgridnumber"]):
      line = 39 + grid
      outgrids.append({
          "name": str(linepos(line, 0)),
          "location": [int(linepos(line, 1)), int(linepos(line, 2))],
          "outglobnet": int(linepos(line, 3))
          })
    config["outgrids"] = outgrids
  else:
    config["outgrids"] = []

  lineposOffset = lambda line, pos: linepos(line + outGridOffset, pos) 
  
  config["methodinisnow"] = int(lineposOffset(1, 0))
  config["methodsnowalbedo"] = int(lineposOffset(2, 0))
  config["methodglobal"] = int(lineposOffset(3, 0))
  config["methodlonginstation"] = int(lineposOffset(4, 0))
  config["methodlongin"] = int(lineposOffset(5, 0))
  config["methodsurftempglac"] = int(lineposOffset(6, 0))

  config["methodturbul"] = int(lineposOffset(8, 0))
  config["method_z0Te"] = int(lineposOffset(9, 0))
  config["methodiceheat"] = int(lineposOffset(10, 0))
  config["methodnegbal"] = int(lineposOffset(11, 0))

  config["scalingyes"] = int(lineposOffset(13, 0))
  config["gamma"] = float(lineposOffset(14, 0))
  config["c_coefficient"] = float(lineposOffset(15, 0))

  config["namedgm"] = str(lineposOffset(17, 0))
  config["namedgmdrain"] = str(lineposOffset(18, 0))
  config["namedgmglac"] = str(lineposOffset(19, 0))
  config["namedgmslope"] = str(lineposOffset(20, 0))
  config["namedgmaspect"] = str(lineposOffset(21, 0))
  config["namedgmskyview"] = str(lineposOffset(22, 0))
  config["namedgmfirn"] = str(lineposOffset(23, 0))
  config["nameinitialsnow"] = str(lineposOffset(24, 0))
  config["nameklima"] = str(lineposOffset(25, 0))

  config["laenge"] = float(lineposOffset(27, 0))
  config["breite"] = float(lineposOffset(28, 0))
  config["reflongitude"] = float(lineposOffset(29, 0))
  config["rowclim"] = int(lineposOffset(30, 0))
  config["colclim"] = int(lineposOffset(31, 0))
  config["climoutsideyes"] = int(lineposOffset(32, 0))
  config["heightclim"] = int(lineposOffset(32, 1))
  config["gridsize"] = int(lineposOffset(33, 0))
  config["timestep"] = int(lineposOffset(34, 0))

  config["formatclimdata"] = int(lineposOffset(36, 0))
  config["maxcol"] = int(lineposOffset(37, 0))

  config["coltemp"] = int(lineposOffset(38, 0))
  config["colhum"] = int(lineposOffset(39, 0))
  config["colwind"] = int(lineposOffset(40, 0))
  config["colglob"] = int(lineposOffset(41, 0))
  config["colref"] = int(lineposOffset(42, 0))
  config["colnet"] = int(lineposOffset(43, 0))
  config["collongin"] = int(lineposOffset(44, 0))
  config["collongout"] = int(lineposOffset(45, 0))
  config["colprec"] = int(lineposOffset(46, 0))
  config["colcloud"] = int(lineposOffset(47, 0))
  config["coltempgradvarying"] = int(lineposOffset(48, 0))
  config["coldis"] = int(lineposOffset(49, 0))

  config["ERAtempshift"] = int(lineposOffset(51, 0))
  config["ERAwindshift"] = int(lineposOffset(52, 0))

  config["methodtempinterpol"] = int(lineposOffset(54, 0))
  config["tempgrad"] = float(lineposOffset(55, 0))
  config["tempscenario"] = int(lineposOffset(56, 0))
  config["precscenario"] = int(lineposOffset(57, 0))
  config["monthtempgradyes"] = int(lineposOffset(59, 0))
  config["monthtempgrad"] = [float(lineposOffset(59,x)) for x in range(1,13)]
  config["monthtempscenyes"] = int(lineposOffset(60, 0))
  config["monthtempscen"] = [float(lineposOffset(60,x)) for x in range(1,13)]
  config["monthprecipscenyes"] = int(lineposOffset(61, 0))
  config["monthprecipscen"] = [float(lineposOffset(61,x)) for x in range(1,13)]


  config["n_albfiles"] = int(lineposOffset(63, 0))
  config["albsnow"] = float(lineposOffset(64, 0))
  config["albslush"] = float(lineposOffset(56, 0))
  config["albice"] = float(lineposOffset(66, 0))
  config["albfirn"] = float(lineposOffset(67, 0))
  config["albrock"] = float(lineposOffset(68, 0))
  config["albmin"] = float(lineposOffset(69, 0))
  config["snowalbincrease"] = float(lineposOffset(70, 0))
  config["albiceproz"] = float(lineposOffset(71, 0))
  config["ndstart"] = int(lineposOffset(72, 0))

  config["split"] = int(lineposOffset(74, 0))
  config["prozdiffuse"] = float(lineposOffset(75, 0))
  config["trans"] = float(lineposOffset(76, 0))
  config["ratio"] = float(lineposOffset(77, 0))
  config["ratiodir2dir"] = float(lineposOffset(78, 0))
  config["surftemplapserate"] = float(lineposOffset(79, 0))
  config["directfromfile"] = int(lineposOffset(80, 0))
  config["pathdirectfile"] = str(lineposOffset(81, 0))
  config["daysdirect"] = int(lineposOffset(82, 0))
  config["slopestation"] = float(lineposOffset(83, 0))

  config["iterstep"] = float(lineposOffset(85, 0))
  config["z0wice"] = float(lineposOffset(86, 0))
  config["dividerz0T"] = float(lineposOffset(87, 0))
  config["dividerz0snow"] = float(lineposOffset(88, 0))
  config["z0proz"] = float(lineposOffset(89, 0))
  config["icez0min"] = float(lineposOffset(90, 0))
  config["icez0max"] = float(lineposOffset(91, 0))

  config["methodprecipinterpol"] = int(lineposOffset(93, 0))
  config["precgrad"] = float(lineposOffset(94, 0))
  config["precgradhigh"] = float(lineposOffset(95, 0))
  config["precgradelev"] = int(lineposOffset(95, 1))
  config["preccorr"] = float(lineposOffset(96, 0))
  config["snowmultiplierglacier"] = float(lineposOffset(97, 0))
  config["snowmultiplierrock"] = float(lineposOffset(98, 0))
  config["threshtemp"] = float(lineposOffset(99, 0))
  config["onlyglacieryes"] = int(lineposOffset(100, 0))
  config["glacierpart"] = float(lineposOffset(101, 0))

  config["nameqcalc"] = str(lineposOffset(103, 0))
  config["nodis"] = int(lineposOffset(104, 0))
  config["firnkons"] = int(lineposOffset(105, 0))
  config["snowkons"] = int(lineposOffset(106, 0))
  config["icekons"] = int(lineposOffset(107, 0))
  config["rockkons"] = int(lineposOffset(108, 0))

  config["qfirnstart"] = float(lineposOffset(110, 0))
  config["qsnowstart"] = float(lineposOffset(111, 0))
  config["qicestart"] = float(lineposOffset(112, 0))
  config["qrockstart"] = float(lineposOffset(113, 0))
  config["qground"] = float(lineposOffset(114, 0))
  config["jdstartr2diff"] = float(lineposOffset(115, 0))

  config["disyesopt"] = int(lineposOffset(117, 0))
  config["optkA"] = str(lineposOffset(118, 0))
  config["startopt1"] = float(lineposOffset(119, 0))
  config["stepopt1"] = float(lineposOffset(120, 0))
  config["anzahlopt1"] = int(lineposOffset(121, 0))
  config["optkB"] = str(lineposOffset(122, 0))
  config["startopt2"] = float(lineposOffset(123, 0))
  config["stepopt2"] = float(lineposOffset(124, 0))
  config["anzahlopt2"] = int(lineposOffset(125, 0))
  config["namematrix"] = str(lineposOffset(126, 0))

  config["percolationyes"] = int(lineposOffset(128, 0))
  config["slushformationyes"] = int(lineposOffset(129, 0))
  config["densificationyes"] = int(lineposOffset(130, 0))
  config["wetstartyes"] = int(lineposOffset(131, 0))
  config["ndepths"] = int(lineposOffset(132, 0))
  config["factinter"] = int(lineposOffset(133, 0))

  config["thicknessfirst"] = float(lineposOffset(135, 0))
  config["thicknessdeep"] = float(lineposOffset(136, 0))
  config["depthdeep"] = float(lineposOffset(137, 0))
  config["denssnow"] = int(lineposOffset(138, 0))
  config["irrwatercontyes"] = int(lineposOffset(139, 0))
  config["irrwatercont"] = float(lineposOffset(140, 0))

  config["factsubsurfout"] = int(lineposOffset(142, 0))
  config["offsetsubsurfout"] = int(lineposOffset(143, 0))

  config["runoffyes"] = int(lineposOffset(145, 0))
  config["superyes"] = int(lineposOffset(145, 1))
  config["wateryes"] = int(lineposOffset(145, 2))
  config["surfwateryes"] = int(lineposOffset(145, 3))
  config["slushyes"] = int(lineposOffset(145, 4))
  config["coldsnowyes"] = int(lineposOffset(145, 5))
  config["coldtotyes"] = int(lineposOffset(145, 6))

  config["ddmethod"] = int(lineposOffset(149, 0))
  config["DDFice"] = float(lineposOffset(150, 0))
  config["DDFsnow"] = float(lineposOffset(151, 0))

  config["meltfactor"] = float(lineposOffset(153, 0))
  config["radfactorice"] = float(lineposOffset(154, 0))
  config["radfactorsnow"] = float(lineposOffset(155, 0))
  config["debrisfactor"] = int(lineposOffset(156, 0))

  config["coordinatesyes"] = int(lineposOffset(158, 0))
  if config["maxmeltstakes"] > 0:
    config["stake_coords"] = [
        [lineposOffset(ii,0), lineposOffset(ii,1)] 
        for ii in range(159, 159 + config["maxmeltstakes"])]
  else:
    config["stake_coords"] = []

  return config
