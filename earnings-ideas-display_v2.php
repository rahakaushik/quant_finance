<?php
parse_str(implode('&', array_slice($argv, 1)), $_GET);
#$sector = $_GET['sector'];
$optype = $_GET['optype'];
#$mode = $_GET['mode'];
#$view = $_GET['view'];
if ($optype == "earnings") {
    
    $f = file_get_contents("earnings_weekly2.csv");
    #echo $f;
    $file_line_array = explode("\n", $f);
    $num_lines = count($file_line_array);
    $lt5K_blurb = "";
    $num_lt5k = 0;
    $lt15K_blurb = "";
    $num_lt15k = 0;
    $num_lt50k = 0;
    $lt50K_blurb = "";
    
    $num_ideas = $num_lines;
    
    for ($i=0;$i<=$num_ideas;$i++) 
    
    {
        
        if(!isset($file_line_array[$i])) { $file_line_array[$i] = null; }
        $line = $file_line_array[$i];
        #echo $line;
        if($i > 0) {
        
        $linedata = explode(",", $line);
        #echo count($linedata);
//        for($j=0;$j<=count($linedata);$j++) 
//        {
//            if(!isset($linedata[$j])) {$linedata[$j] = null;}
//        }
        if(!isset($linedata[0])) {$linedata[0] = null;}
        if(!isset($linedata[1])) {$linedata[1] = null;}
        if(!isset($linedata[2])) {$linedata[2] = null;}
        if(!isset($linedata[3])) {$linedata[3] = null;}
        if(!isset($linedata[4])) {$linedata[4] = null;}
        if(!isset($linedata[4])) {$linedata[5] = null;}
        //$income_gen = floatval($linedata[7]);
        //print "$linedata[1]\n";
        if($linedata[4] > 0.0) {
                //print($linedata[8]);
        if($linedata[2] < 7)  {
            //echo "this is $linedata[0]";
            //exit();
            $num_lt5k = $num_lt5k+1;
            $lt5K_blurb = $lt5K_blurb."<font color='black'>The stock ".$linedata[0]." will announce earnings this week on ".$linedata[1].". <b>It's price rose  ".
            $linedata[2]." out of 10 times the day after the earnings report.</b></font><font color='black' size=2> The correlation between earnings and price is ".number_format(floatval($linedata[3]),2)." "
            . ". Last price of this stock is $".number_format(floatval($linedata[4]),2)." and range is ".$linedata[5]." </font></p><p>";
            
             
        }
        
        if (nBetween($linedata[2], 8.0, 7.0))  {
            //echo "this is $linedata[0]";
            //exit();
            $num_lt15k = $num_lt15k+1;
            $lt15K_blurb = $lt15K_blurb."<font color='black'>The stock ".$linedata[0]." will announce earnings this week on ".$linedata[1].". <b>It's price rose  ".
            $linedata[2]." out of 10 times the day after earnings report.</b></font><font color='black' size=2> The correlation between earnings and price is ".number_format(floatval($linedata[3]),2)." "
            . ". Last price of this stock is $".number_format(floatval($linedata[4]),2)." and range is ".$linedata[5]." </font></p><p>";
            
             
        }
        if ($linedata[2] > 8)  {
            //echo "this is $linedata[0]";
            //exit();
            $num_lt50k = $num_lt50k+1;
            $lt50K_blurb = $lt50K_blurb."<font color='black'>The stock ".$linedata[0]." will announce earnings this week on ".$linedata[1].". <b>It's price rose  ".
            $linedata[2]." out of 10 times the day after the earnings report.</b></font><font color='black' size=2> The correlation between earnings and price is ".number_format(floatval($linedata[3]),2)." "
            . ". Last price of this stock is $".number_format(floatval($linedata[4]),2)." and range is ".$linedata[5]." </font></p><p>";
            
             
        }

        }
       }
    }
}


function nBetween($varToCheck, $high, $low) {
if($varToCheck < $low) return false;
if($varToCheck > $high) return false;
return true;
}
?>

<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>Earnings Trends</title>
		<meta name="description" content="Blueprint: Nested Accordion" />
		<meta name="keywords" content="nested, accordion, simple, vertical, web development, css3, javascript" />
		<meta name="author" content="Codrops" />
		<link rel="shortcut icon" href="../favicon.ico">
		<link rel="stylesheet" type="text/css" href="css/default.css" />
		<!--link rel="stylesheet" type="text/css" href="http://qntafi.com/wp-content/themes/quantifi/css/accordion/css/acc-component.css" /-->
		<link rel="stylesheet" type="text/css" href="css/component.css" />
                <script src="js/modernizr.custom.js"></script>
                
	</head>
	<body>
		<div class="container">
			<!--header class="clearfix">
				<span>QNTAFI</span>
				<h1>Freeview</h1>
                                
				
			</header-->	
                    
			<div class="main">
                            <!--p><font color="black">
                            Freeview features examples of our offerings but using a limited set of stock tickers or only for one exchange or sector type. While these ideas are still actionabale, to avail all our offerings without any restrictions please consider our membership options.
                            </font>
                            </p-->	
                            
                                <ul id="cbp-ntaccordion" class="cbp-ntaccordion">
					<li>
						<h3 class="cbp-nttrigger">Earnings this week</h3>
						<div class="cbp-ntcontent">
							<p>Here our bot surfaces stocks which will report earnings this coming week. Often after earnings reports stock prices show interesting
                                                        trends. Our algorithms crunch the historical earnings data and model the correlation of earnings with price. Following are stocks which have risen after earnings report if earnings beat expectations. We calcualte low, medium, and high probabilty of price movement are reported below. These are not recommendations for trading. 
                                                            
                                                        <ul class="cbp-ntsubaccordion">
								<li>
									<h4 class="cbp-nttrigger">Low Probablity of Price Rise</h4>
									<div class="cbp-ntcontent">
										<p> <?php 
                                                                                 echo $lt5K_blurb;
                                                                                        ?>
                                                                                </p>
									</div>
								</li>
								<li>
									<h4 class="cbp-nttrigger">Medium Probablity of Price Rise</h4>
									<div class="cbp-ntcontent">
										<p> <?php 
                                                                                echo $lt15K_blurb;
                                                                                        ?>
                                                                                </p>
                                                                        </div>
								</li>
								<li>
									<h4 class="cbp-nttrigger">High Probablity of Price Rise</h4>
									<div class="cbp-ntcontent">
										<p> <?php 
                                                                                 echo $lt50K_blurb;
                                                                                        ?>
                                                                                </p>
                                                                        </div>
								</li>
							</ul>
						</div>
					</li>
					<!--li>
						<h3 class="cbp-nttrigger">Find more ideas</h3>
						<div class="cbp-ntcontent">
							<p>Our members have access to many other actionable ideas generated using variety of different options strategies that are executed algorithmically on delayed and real time data.
                                                        If you already have membership please go ahead and access our Options offering. If not register with a membership plan</p>
							<ul class="cbp-ntsubaccordion">
								<li>
									<h4 class="cbp-nttrigger">Register</h4>
									<div class="cbp-ntcontent">
                                                                            <p></p>
                                                                        </div>
								</li>
								
							</ul>
						</div>
					</li-->
					
					
				</ul>
			</div>
		</div>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
		<script src="js/jquery.cbpNTAccordion.min.js"></script>
                
		<script>
			$( function() {
				/*
				- how to call the plugin:
				$( selector ).cbpNTAccordion( [options] );
				- destroy:
				$( selector ).cbpNTAccordion( 'destroy' );
				*/

				$( '#cbp-ntaccordion' ).cbpNTAccordion();

			} );
		</script>
	</body>
</html>
