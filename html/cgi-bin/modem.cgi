#!/usr/bin/perl
#
# SmoothWall CGIs
#
# This code is distributed under the terms of the GPL
#
# (c) The SmoothWall Team
#
# $Id: modem.cgi,v 1.4.2.7 2005/02/22 22:21:56 gespinasse Exp $
#

use strict;

# enable only the following on debugging purpose
#use warnings;
#use CGI::Carp 'fatalsToBrowser';

require '/var/ipfire/general-functions.pl';
require "${General::swroot}/lang.pl";
require "${General::swroot}/header.pl";

my %modemsettings=();
my $errormessage = '';

&Header::showhttpheaders();

$modemsettings{'ACTION'} = '';
$modemsettings{'VALID'} = '';

&Header::getcgihash(\%modemsettings);

if ($modemsettings{'ACTION'} eq $Lang::tr{'save'})
{ 
        if (!($modemsettings{'TIMEOUT'} =~ /^\d+$/))
        {
      	 	$errormessage = $Lang::tr{'timeout must be a number'};
	 	goto ERROR;
        }
ERROR:   
        if ($errormessage) {
                $modemsettings{'VALID'} = 'no'; }
        else {
                $modemsettings{'VALID'} = 'yes'; }

	&General::writehash("${General::swroot}/modem/settings", \%modemsettings);
}

if ($modemsettings{'ACTION'} eq $Lang::tr{'restore defaults'})
{
	system('/bin/cp', "${General::swroot}/modem/defaults", "${General::swroot}/modem/settings", '-f');
}

&General::readhash("${General::swroot}/modem/settings", \%modemsettings);

&Header::openpage($Lang::tr{'modem configuration'}, 1, '');

&Header::openbigbox('100%', 'left', '', $errormessage);

if ($errormessage) {
	&Header::openbox('100%', 'left', $Lang::tr{'error messages'});
	print "<font class='base'>$errormessage&nbsp;</font>\n";
	&Header::closebox();
}

print "<form method='post' action='$ENV{'SCRIPT_NAME'}'>\n";

&Header::openbox('100%', 'left', "$Lang::tr{'modem configuration'}:");
print <<END
<table width='100%'>
<tr>
	<td width='25%' class='base'>$Lang::tr{'init string'}&nbsp;<img src='/blob.gif' alt='*' /></td>
	<td width='25%'><input type='text' name='INIT' value='$modemsettings{'INIT'}' /></td>
	<td width='25%' class='base'>$Lang::tr{'hangup string'}&nbsp;<img src='/blob.gif' alt='*' /></td>
	<td width='25%'><input type='text' name='HANGUP' value='$modemsettings{'HANGUP'}' /></td>
</tr>
<tr>
	<td class='base'>$Lang::tr{'speaker on'}&nbsp;<img src='/blob.gif' alt='*' /></td>
	<td><input type='text' name='SPEAKER_ON' value='$modemsettings{'SPEAKER_ON'}' /></td>
	<td class='base'>$Lang::tr{'speaker off'}&nbsp;<img src='/blob.gif' alt='*' /></td>
	<td><input type='text' name='SPEAKER_OFF' value='$modemsettings{'SPEAKER_OFF'}' /></td>
</tr>
<tr>
	<td class='base'>$Lang::tr{'tone dial'}&nbsp;<img src='/blob.gif' alt='*' /></td>
	<td><input type='text' name='TONE_DIAL' value='$modemsettings{'TONE_DIAL'}' /></td>
	<td class='base'>$Lang::tr{'pulse dial'}&nbsp;<img src='/blob.gif' alt='*' /></td>
	<td><input type='text' name='PULSE_DIAL' value='$modemsettings{'PULSE_DIAL'}' /></td>
</tr>
<tr>
	<td class='base'>$Lang::tr{'connect timeout'}</td>
	<td><input type='text' name='TIMEOUT' value='$modemsettings{'TIMEOUT'}' /></td>
	<td class='base'>&nbsp;</td>
	<td>&nbsp;</td>
</tr>

</table>
<table width='100%'>
<hr />
<tr>
	<td width='33%'>
		<img src='/blob.gif' align='top' alt='*' />&nbsp;
		<font class='base'>$Lang::tr{'this field may be blank'}</font>
	</td>
	<td width='33%' align='center'>
		<input type='submit' name='ACTION' value='$Lang::tr{'restore defaults'}' />
	</td>
	<td width='33%' align='center'>
		<input type='submit' name='ACTION' value='$Lang::tr{'save'}' />
	</td>
</tr>
</table>
</div>
END
;
&Header::closebox();

print "</form>\n";

&Header::closebigbox();

&Header::closepage();
