#!/usr/bin/env bash

#define functions
function showBalance(){
	bal=$(<account.txt)
	echo "Your account balance: "$bal" €"
}

function deposit(){
	python laser.py
	python stepper.py &
	python inductor.py
	python coinAI.py
	> i_status.txt
}

function withdraw(){
	python withdraw.py
	showBalance
}

function resetAcc(){
	echo "0" > account.txt
	echo "Set account balance to 0 €"
}

#define colors
green='\e[32m'
blue='\e[33m'
clear='\e[0m'

ColorGreen(){
	echo -ne $green$1$clear
}

ColorBlue(){
	echo -ne $blue$1$clear
}

#define menu
menu(){
echo -ne "
-----------------------------

== Menu ==
$(ColorGreen '1)') Show account balance
$(ColorGreen '2)') Deposit money into account
$(ColorGreen '3)') Withdraw from account
$(ColorGreen '4)') Reset account balance
$(ColorGreen '0)') Exit
$(ColorBlue 'Chosse an option: ')"
	read a
	case $a in
		1) showBalance ; menu ;;
		2) deposit ; menu ;;
		3) withdraw ; menu ;;
		4) resetAcc ; menu ;;
		0) exit 0 ;;
	*) echo -e "Option unavailable!"$clear; menu ;;
	esac
}

menu
