# Makefile for source rpm: system-config-keyboard
# $Id$
NAME := system-config-keyboard
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
