from datetime import date
import os

#
# Configuration Parameters
#

#data_dir 	= "/Volumes/MacBay3/landslide/data"
#data_dir 	= "/Users/patricecappelaere/landslide/data"

#DATA_DIR					= os.environ['WORKSHOP_DIR'] + "/data"
DATA_DIR					= os.environ['DATA_DIR']
data_dir					= DATA_DIR

# Set if you want to use AWS S3 for persistent storage of products
USING_AWS_S3_FOR_STORAGE	= 1

# This would be an alternate way to store process data (but may not scale well)
USING_LOCAL_DIR_FOR_STORAGE	= 0
LOCAL_DIR_STORAGE			= "/Users/patricecappelaere/Development/ojo/tmp"

# Set to get emails during processing... You will have to set some additional envs
# FASTMAIL_USER, FASTMAIL_PASSWORD, FASTMAIL_SMTP
SEND_EMAIL					= 1

# Number of days to keep data for (kept an extra day for regional landslide processing than needs 60 days of data)
DAYS_KEEP					= 61

#
# Data Directories
#
LANDSAT8_DIR				= os.path.join(DATA_DIR, "l8")
RADARSAT2_DIR				= os.path.join(DATA_DIR, "radarsat2")
MODIS_DIR					= os.path.join(DATA_DIR, "modis")
MODIS_ACTIVE_FIRES_DIR		= os.path.join(DATA_DIR, "modis_af")
MODIS_BURNEDAREAS_DIR		= os.path.join(DATA_DIR, "modis_burnedareas")
EO1_DIR						= os.path.join(DATA_DIR, "eo1_ali")
DFO_DIR						= os.path.join(DATA_DIR, "dfo")
PALSAR2_DIR					= os.path.join(DATA_DIR, "palsar2")
FROST_DIR					= os.path.join(DATA_DIR, "frost")
DIGIGLOBE_DIR				= os.path.join(DATA_DIR, "digiglobe")
VIIRS_DIR					= os.path.join(DATA_DIR, "viirs")
CSV_DIR						= os.path.join(DATA_DIR, "csv")
EF5_DIR						= os.path.join(DATA_DIR, "ef5")
MAXQ_DIR					= os.path.join(DATA_DIR, "maxq")
MAXSWE_DIR					= os.path.join(DATA_DIR, "maxswe")
SM_DIR						= os.path.join(DATA_DIR, "sm")
TRMM_DIR					= os.path.join(DATA_DIR, "trmm_24")
GPM_DIR						= os.path.join(DATA_DIR, "gpm_24")
LS_DIR						= os.path.join(DATA_DIR, "ls")
QUAKES_DIR					= os.path.join(DATA_DIR, "quakes")
VIIRS_CHLA_DIR				= os.path.join(DATA_DIR, "viirs_chla")
VIIRS_ACTIVE_FIRES_DIR		= os.path.join(DATA_DIR, "viirs_af")
CHIRPS_PRELIM_DIR			= os.path.join(DATA_DIR, "chirps2_prelim")
GEOS5_DIR					= os.path.join(DATA_DIR, "geos5")
GEOS5_SAT_DIR				= os.path.join(DATA_DIR, "geos5_sat")


today 		= date.today()
year		= today.year
month		= today.month
day			= today.day

#
# Hardcoded day for now so we can all agree
#

#year		= 2014
#month		= 06
#day		= 03

ym	 		= "%d%02d" % (year, month)
ymd 		= "%d%02d%02d" % (year, month, day)

# BBOX of interest
#bbox		= [-94, 19, -76, 6]
#bbox[0] 	+= 360
#bbox[2] 	+= 360

# Rainfall limits in mm/day fo rthe landslide model
rainfall_red_limit 		= 75
rainfall_orange_limit	= 50
rainfall_yellow_limit	= 35

# wrf bboxes lllon,lllat,urlon,urlat
# D02 1872x1438
#Upper Left  ( -92.6931093,  19.0872388) ( 92d41'35.19"W, 19d 5'14.06"N)
#Lower Left  ( -92.6931093,   6.1466768) ( 92d41'35.19"W,  6d 8'48.04"N)
#Upper Right ( -75.8469813,  19.0872388) ( 75d50'49.13"W, 19d 5'14.06"N)
#Lower Right ( -75.8469813,   6.1466768) ( 75d50'49.13"W,  6d 8'48.04"N)
#Center      ( -84.2700453,  12.6169578) ( 84d16'12.16"W, 12d37' 1.05"N)

# D03 1109x567
#Upper Left  ( -74.9570600,  21.4358479) ( 74d57'25.42"W, 21d26' 9.05"N)
#Lower Left  ( -74.9570600,  16.3334149) ( 74d57'25.42"W, 16d20' 0.29"N)
#Upper Right ( -64.9771690,  21.4358479) ( 64d58'37.81"W, 21d26' 9.05"N)
#Lower Right ( -64.9771690,  16.3334149) ( 64d58'37.81"W, 16d20' 0.29"N)
#Center      ( -69.9671145,  18.8846314) ( 69d58' 1.61"W, 18d53' 4.67"N)

regions		= {
	'global': {
		'global':		"World",
		'bbox': 		[-180, -50, 180, 50 ],
		'bucket':		"ojo-global",
		'pixelsize':	0.008333333333330,
		'thn_width':	720,
		'thn_height':	240,
        'tiles-zoom':   "s3rccp"
	
	},
	'd02': {
		'name':			"Central America",
		'bbox': 		[-92.6833333,   6.1666667, -75.8500000,  19.0833333],
		'centerlat':	12.625,
		'centerlon':	-84.26666665,
		'pixelsize':	0.008333333333330,
		'columns': 		2020,
		'rows': 		1550,
		'thn_width':	389,
		'thn_height':	298,
		'thn_zoom': 	5,
		'bucket':		"s3rccp",
		'modis_tiles':  [
			"100W020N",
			"090W020N",
			"090W010N"	
		],
		'hydroshed_tiles': [
			"CA/n15w095",
			"CA/n10w095",
			"CA/n15w090",
			"CA/n10w090",
			"CA/n05w090",
			"CA/n15w085",
			"CA/n10w085",
			"CA/n05w085",
			"CA/n15w080",
			"CA/n10w080",
			"CA/n05w080",
		],
		'tiles-zoom':	"6-14",
		'modis-win': 	"Win04"		# MCD45 Window (MODIS Burned Areas)
	},
	'd03': {
		'name':			"Hispaniola",
		'bbox': 		[-74.9416667, 16.3500000, -64.9750000,  21.4250000],
		'centerlat':	18.8875,
		'centerlon':	-69.95833335,
		'pixelsize':	0.008333333333330,
		'columns': 		1196,
		'rows': 		609,
		'thn_width':	400,
		'thn_height':	204,
		'thn_zoom': 	6,
		'bucket':		"ojo-d3",
		'modis_tiles':  [
			"080W020N",
			"070W020N"
		],
		'hydroshed_tiles': [
			"CA/n20w075",
			"CA/n15w075",
			"CA/n15w070"
		],
		'tiles-zoom':    "6-14",
		'modis-win': 	"Win04"		# MCD45 Window (MODIS Burned Areas)
	},
	'd04': {
		'name':			"Namibia",
		'bbox': 		[18, -21, 26, -17 ],
		'centerlat':	-18,
		'centerlon':	21,
		'bucket':		"ojo-d4",
		'thn_zoom': 	6
	},
	'd05': {
		'name':			"RCMRD",
		'bbox': 		[29, -8, 42, 4 ],
		'centerlat':	-2,
		'centerlon':	36,
		'bucket':		"ojo-d5",
		'thn_zoom': 	6
	},
	'd07': {
		'name':			"India",
		'bbox': 		[60.5, 6.7917, 97.383224, 38.375],
		'centerlat':	22.6333603,
		'centerlon':	78.9415631,
		'pixelsize':	0.008333333333330,
		'columns': 		4426,
		'rows': 		3802,
		'thn_width':	443,
		'thn_height':	380,
		'bucket':		"ojo-d7",
		'thn_zoom': 	5,
		'tiles-zoom':    "6-14"
	},
	'd08': {
		'name':			"Nepal",
		'bbox': 		[72.9998988,  25.9916923, 97.3832321,  38.4750256],
		'centerlat':	32.2333589,
		'centerlon':	85.1915655,  
		'pixelsize':	0.008333333333330,
		'columns': 		2926,
		'rows': 		1498,
		'thn_width':	583,
		'thn_height':	300,
		'bucket':		"ojo-d8",
		'thn_zoom': 	5,
		'tiles-zoom':    "6-14"
	},
	'd09': {
		'name':			"Peru",
		'bbox': 		[-81.3583333, -18.3499400, -68.6666667,  -0.0332733],
		'centerlat':	-9.1916067,
		'centerlon':	-75.0125000,  
		'pixelsize':	0.008333333333330,
		'columns': 		1523,
		'rows': 		2198,
		'thn_width':	304,
		'thn_height':	439,
		'bucket':		"ojo-d9",
		'thn_zoom': 	5,
		'tiles-zoom':    "6-14"
	},
	'd10': {
		'name':			"Rio2016",
		'bbox': 		[-45.0, -23.37494, -39,  -17.8916067],
		'centerlat':	-20.6332733,
		'centerlon':	-42.0,  
		'pixelsize':	0.008333333333330,
		'columns': 		720,
		'rows': 		658,
		'thn_width':	720,
		'thn_height':	658,
		'bucket':		"ojo-d10",
		'thn_zoom': 	8,
		'tiles-zoom':    "8-18"
	}
}

# Landslide database csv
db_csv 		= "db2.csv"
db_xml 		= "db2.xml"
db_osm		= "db2.osm"
db_geojson	= "db2.geojson"
