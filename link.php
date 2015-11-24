<?php
$header = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
      <style>
         table, td {border:1px solid black; padding: 10px;}
      </style>
<!--... Defining UTF-8 as our default character set, so that devanagari is displayed properly. -->
<meta charset="UTF-8">
</head> 
<body>
<table>
';

function pdflink($dict,$word)
{
	return '<a href="http://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/servepdf.php?dict='.$dict.'&key='.$word.'" target="_blank">'.$dict."</a>";
}
function Cologne_hrefyear($dict) {
// This could be written using an associative array
$dictionaryname=array("ACC","CAE","AE","AP90","AP","BEN","BHS","BOP","BOR","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","MWE","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT");
$hrefyear = array("2014","2014","2014","2014","2014","2014","2014","2014","2014","2013","2014","2014","2014","2014","2013","2014","2014","2014","2014","2014","2013","2014","2014","2014","2014","2013","2014","2014","2014","2013","2014","2013","2013","2014","2014","2014");
 $ans = '?';
 for($i=0;$i<count($dictionaryname);$i++) {
  if ($dict == $dictionaryname[$i]){
   $ans = $hrefyear[$i];
   break;
  }
 }
 return $ans;
}
function webpagelink($dict,$word)
{
	$y=Cologne_hrefyear($dict);
	return '<a href="'."http://www.sanskrit-lexicon.uni-koeln.de/scans/".$dict."Scan/".$y."/web/webtc/indexcaller.php".'?key='.$word.'&input=slp1&output=SktDevaUnicode" target="_blank">'.$word."</a>"; 
}

function linked($inputfile,$outputfile)
{
	global $header;
	$input = file($inputfile);
	$input = array_map('trim',$input);
	$outfile = fopen($outputfile,"w");
	fputs($outfile,$header);
	$counter = 1;
	foreach ($input as $value)
	{
		list($word,$dict) = explode(':',$value);
		fputs($outfile,"<tr><td>".$counter."</td><td>".webpagelink($dict,$word)."</td><td>".pdflink($dict,$word)."</td></tr>\n");
		$counter++;
	}
	fputs($outfile,"</table></body></html>");
	fclose($outfile);
	echo "Check $outputfile for testing.\n";
}
$inputfile = $argv[1];
$outputfile = $argv[2];
linked($inputfile,$outputfile);
?>
