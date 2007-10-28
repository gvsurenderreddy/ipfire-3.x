#!/bin/bash
############################################################################
#                                                                          #
# This file is part of the IPFire Firewall.                                #
#                                                                          #
# IPFire is free software; you can redistribute it and/or modify           #
# it under the terms of the GNU General Public License as published by     #
# the Free Software Foundation; either version 2 of the License, or        #
# (at your option) any later version.                                      #
#                                                                          #
# IPFire is distributed in the hope that it will be useful,                #
# but WITHOUT ANY WARRANTY; without even the implied warranty of           #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
# GNU General Public License for more details.                             #
#                                                                          #
# You should have received a copy of the GNU General Public License        #
# along with IPFire; if not, write to the Free Software                    #
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA #
#                                                                          #
# Copyright (C) 2007 IPFire-Team <info@ipfire.org>.                        #
#                                                                          #
############################################################################
#
. /opt/pakfire/lib/functions.sh

extract_files

ln -svf  /etc/init.d/mpd /etc/rc.d/rc3.d/S65mpd
ln -svf  /etc/init.d/mpd /etc/rc.d/rc0.d/K35mpd
ln -svf  /etc/init.d/mpd /etc/rc.d/rc6.d/K35mpd
ln -svf  /var/ipfire/mpfire/mpd.conf /etc/mpd.conf

touch /var/log/mpd.error.log
touch /var/log/mpd.log

restore_backup ${NAME}

start_service --delay 60 --background ${NAME}
