#!/bin/bash

# Ensure we are running under bash
if [ "$BASH_SOURCE" = "" ]; then
    /bin/bash "$0"
    exit 0
fi

# Load bash-menu script
# NOTE: Ensure this is done before using
#       or overriding menu functions/variables.
. "bash-menu.sh"


################################
## Example Menu Actions
##
## They should return 1 to indicate that the menu
## should continue, or return 0 to signify the menu
## should exit.
################################
function showBalance(){
	bal=$(<account.txt)
	echo -n 
	echo "------------------------------"
	echo "Your account balance: "$bal" €"
	echo "------------------------------"
	sleep 2
	echo ""
	read -n 1 -s -r -p "Press any key to continue ..."
	return 1
}

function deposit(){
	echo "------------------------------"
    	python stepper.py &
	python inductor.py
	python coinAI.py
	> i_status.txt
	echo "------------------------------"
	sleep 2
	echo ""
	read -n 1 -s -r -p "Press any key to continue ..."
	return 1
}

function withdraw(){
	python withdraw.py
	bal=$(<account.txt)
	echo -n 
	echo "------------------------------"
	echo "Your account balance: "$bal" €"
	echo "------------------------------"
	sleep 2
	echo ""
	read -n 1 -s -r -p "Press any key to continue ..."
	return 1
}

function reset(){
	echo "0" > account.txt
	echo "--------------------------"
	echo "Set account balance to 0 €"
	echo "--------------------------"
	sleep 2
	echo ""
	read -n 1 -s -r -p "Press any key to continue ..."
	return 1
}

function resetAcc(){
	echo "--------------------------"
	read -p "Are you sure (y/n)? " choice
	case "$choice" in
		y|Y ) reset;;
		n|N ) echo "Abort!";;
		* ) echo "Undefined!";;
	esac
	sleep 0.5
	return 1	
}

function exit(){
    	return 0
}


################################
## Setup Menu
################################
## Menu Item Text
##
## Pressing Esc will jump to last item (and
## pressing Esc while on last item will perform the
## associated action).
##
## NOTE: If these are not all the same width
##       the menu highlight will look wonky
menuItems=(
    "1. Show account balance"
    "2. Deposit money into account"
    "3. Withdraw from account"
    "4. Reset account balance"
    "Q. Exit  "
)

## Menu Item Actions
menuActions=(
    showBalance
    deposit
    withdraw
    resetAcc
    exit
)

## Override some menu defaults
menuTitle=" HS-AlbSig | ATM                         Location: Albstadt"
menuFooter=" Enter=Select, Navigate via Up/Down/First number/letter"
menuWidth=60
menuLeft=20
menuHighlight=$DRAW_COL_WHITE


################################
## Run Menu
################################
menuInit
menuLoop


exit 0
