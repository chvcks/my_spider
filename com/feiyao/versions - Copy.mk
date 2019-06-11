##############################################################
# VERSIONS & PATHES FOR ALL PRODUCTS: 
# VERSIONS = R.RV.VF : RR= Release identifier (40 for NOE-3G R100)
#                      VV= Version  (0..99)
#                      F = Fix      (0..9)
##############################################################

########################################
# VERSION NUMBERS
########################################

# WARNING: !!! DO NOT CHANGE FORMAT OR REMOVE BLANKS

# Main versions for A & B/C
# identify the product release
VERSION_MAIN_A= 4.00.00
VERSION_MAIN_B= 4.11.88

# Binary versions 
# identify the binaries for download
VERSION_SOFT= 4.11.88
VERSION_DATA= 4.11.88

# internal components
# !!WARNING !!! CHANGE ONLY IF MODIFICATIONS
# NEW BOOT MUST BE COMPATIBLE WITH OLDER ONES
VERSION_BOOT= 4.00.30

# manufactory initial (NOE2G)
VERSION_FAB=  0.01.00

#################################################################
# Only to use an existing released soft binary (B/C only)
# if binary copy then set the USE flag to 1 and give the
# main version of the release containing the binary
#################################################################
# USE only for fix releases , R.VV.FF (R.VV must match with data)
#################################################################
ifndef USE_RELEASED_SOFT
USE_RELEASED_SOFT= 0
VERSION_RELEASED_SOFT_MAIN= 4.11.88
endif

#################################################################
# Only to use an existing released datas binary (B/C only)
# if binary copy then set the USE flag to 1 and give the
# main version of the release containing the binary
#################################################################
# USE only for fix releases , R.VV.FF (R.VV must match with soft)
#################################################################
ifndef USE_RELEASED_DATA
USE_RELEASED_DATA= 0
VERSION_RELEASED_DATA_MAIN= 4.11.88
endif

#################################################################
# Only to use an existing released font binary (B/C only)
# if binary copy then set the USE flag to 1 and give the
# version of the release containing the binary
# (BUILD_L10N allows to never use released version when called 
# directly by "build L10N")
# USE_RELEASED_L10N = 0   | 1          (use released file or not)
# PROJ_RELEASED_L10N= 2G  | 3G         (NOE or NOE-3G delivery)
# NAME_RELEASED_L10N= chi | jpn | kor  (one of ...)
#################################################################
ifndef BUILD_L10N
ifndef USE_RELEASED_L10N
USE_RELEASED_L10N= 1
PROJ_RELEASED_L10N= 2G
NAME_RELEASED_L10N= chi
VERSION_RELEASED_L10N= 2.01.01
endif
endif

#################################################################
# Only to use an existing released font binary (B/C only)
# if binary copy then set the USE flag to 1 and give the
# version of the release containing the binary
# (BUILD_CUST allows to never use released version when called 
# directly by "build CUST")
# USE_RELEASED_CUST = 0  | 1
# PROJ_RELEASED_CUST= 2G | 3G  
#################################################################
ifndef BUILD_CUST
ifndef USE_RELEASED_CUST
USE_RELEASED_CUST= 0
PROJ_RELEASED_CUST= 2G
NAME_RELEASED_CUST= caixa
VERSION_RELEASED_CUST= 1.00.00
endif
endif

#################################################################
# localization & customization versions (not released)
#################################################################
ifeq ($(UAPROD), B)
ifneq ($(USE_RELEASED_L10N), 1)
include $(L10FUL_B)/version.mk
endif
ifneq ($(USE_RELEASED_CUST), 1)
include $(CUSFUL_B)/version.mk
endif
endif

#################################################################
#################################################################
include versions_path.mk
include versions_comp.mk
